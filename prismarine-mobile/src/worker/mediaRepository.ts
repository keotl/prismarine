import { Album, fetchArtwork, getAlbum, listAlbums, trackUrl } from "../api";

export type SavedMedia = {
  status: "saved";
  key: string;
  blob: Blob;
};

export type PendingMedia = {
  status: "pending";
  key: string;
};
export type DownloadingMedia = {
  status: "downloading";
  key: string;
};

export class MediaRepository {
  private queue: string[];
  private db: IDBDatabase | undefined;

  constructor() {
    this.queue = [];
    this.db = undefined;
  }

  init() {
    let completed = false;
    navigator.locks.request("queue", (lock) => {
      const request = indexedDB.open("cache");
      request.onupgradeneeded = () => {
        request.result.createObjectStore("media");
        request.result.createObjectStore("artwork");
        request.result.createObjectStore("albumSummary");
        request.result.createObjectStore("albumDetails");
        request.result.createObjectStore("albumState");
      };

      request.onsuccess = () => {
        console.log("successfully initialized IndexedDB");
        this.db = request.result;
        completed = true;
      };
    });

    return new Promise((r) => {
      setTimeout(() => {
        if (completed) {
          r("ok");
        }
      }, 1000);
    });
  }
  closeDb() {
    this.db?.close();
  }

  async updateLibraryMetadata() {
    if (!this.db) {
      throw Error("db not open");
    }

    await navigator.locks.request("queue", async (lock) => {
      if (!this.db || !lock) {
        return;
      }
      console.log("updating library metadata...");
      const albums = (await listAlbums()).albums;
      let tx = this.db.transaction("albumSummary", "readwrite");
      let store = tx.objectStore("albumSummary");
      store.delete(IDBKeyRange.lowerBound(""));

      for (const a of albums) {
        store.put(a, a.id);
      }
      tx.commit();
      const albumDetails = [];
      const artwork: { [key: string]: Blob } = {};
      for (const a of albums) {
        const details = await getAlbum(a.id);
        albumDetails.push(details);
        const albumArtwork = await fetchArtwork(a.artwork_url);
        if (albumArtwork) {
          artwork[a.id] = albumArtwork;
        }
      }

      tx = this.db.transaction(["albumDetails", "artwork"], "readwrite");
      store = tx.objectStore("albumDetails");
      const artworkStore = tx.objectStore("artwork");
      for (const a of albumDetails) {
        if (artwork[a.id]) {
          artworkStore.put(artwork[a.id], a.id);
        }
        store.put(a, a.id);
      }
      tx.commit();
      console.log("done-updating library metadata");
    });
  }

  fetchMedia(
    mediaId: string
  ): Promise<SavedMedia | PendingMedia | DownloadingMedia | null> {
    if (!this.db) {
      return Promise.reject("db not open");
    }
    const tx = this.db.transaction("media", "readonly");
    const store = tx.objectStore("media");
    return new Promise((r) => {
      const op = store.get(mediaId);
      op.onsuccess = (ev) => r(op.result);
    }) as any;
  }

  reloadIncomplete() {
    if (!this.db) {
      throw Error("db not open");
    }
    const tx = this.db.transaction("media", "readonly");
    const store = tx.objectStore("media");
    const request = store.getAll();
    request.onsuccess = () => {
      for (const e of request.result) {
        if (e.status !== "saved") {
          this.queueDownload(e.key);
        }
      }
    };
  }
  async queueDownload(mediaId: string) {
    if (!this.db) {
      throw Error("db not open");
    }

    const existing = await this.fetchMedia(mediaId);
    if (existing && existing.status === "saved") {
      return;
    }
    await navigator.locks.request("queue", (lock) => {
      if (!this.db || !lock) {
        return;
      }
      const tx = this.db.transaction("media", "readwrite");
      const store = tx.objectStore("media");
      store.put({ status: "pending", key: mediaId }, mediaId);
      if (!this.queue.includes(mediaId)) {
        this.queue.push(mediaId);
        console.log(this.queue);
      }
    });
  }

  saveAlbum(albumId: string) {
    if (!this.db) {
      throw Error("db not open");
    }
    const tx = this.db.transaction("albumState", "readwrite");
    const store = tx.objectStore("albumState");
    store.put({ status: "saved", key: albumId }, albumId);
    this.fetchAlbumDetails(albumId).then((a) => {
      if (!a) {
        return;
      }
      a.tracks.forEach((t) => this.queueDownload(t.id));
    });
  }
  fetchAlbumDetails(albumId: string): Promise<Album | null> {
    if (!this.db) {
      return Promise.resolve(null);
    }
    const tx = this.db.transaction("albumDetails", "readonly");
    const store = tx.objectStore("albumDetails");
    return new Promise((r) => {
      const op = store.get(albumId);
      op.onsuccess = (ev) => r(op.result);
    }) as any;
  }

  poll() {
    navigator.locks.request("queue", { ifAvailable: true }, async (lock) => {
      if (!lock || !this.db) {
        return;
      }
      if (this.queue.length === 0) {
        return;
      }

      const mediaId = this.queue.shift()!;
      console.log("starting download for ", mediaId);
      let tx = this.db.transaction("media", "readwrite");
      let store = tx.objectStore("media");
      store.put({ status: "downloading", key: mediaId }, mediaId);
      tx.commit();

      const blob = await fetch(trackUrl(mediaId)).then((r) => {
        if (r.status > 300) {
          throw Error(
            "got invalid response while fetching " + trackUrl(mediaId)
          );
        }
        return r.blob();
      });

      tx = this.db.transaction("media", "readwrite");
      store = tx.objectStore("media");
      store.put({ status: "saved", blob, key: mediaId }, mediaId);
      tx.commit();
      console.log("completed job for ", mediaId);
    });
  }
}
