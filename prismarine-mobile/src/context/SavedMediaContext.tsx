import {
  createContext,
  ReactNode,
  useContext,
  useEffect,
  useState,
} from "react";
import { Album, AlbumSummary, trackUrl } from "../api";
import {
  DownloadingMedia,
  PendingMedia,
  SavedMedia,
} from "../worker/mediaRepository";

export type SavedMediaContextValue = {
  db: IDBDatabase | null;
  fetchMedia: (
    mediaId: string
  ) => Promise<SavedMedia | PendingMedia | DownloadingMedia | null>;
  listAlbums: () => Promise<AlbumSummary[]>;
  fetchAlbumDetails: (albumId: string) => Promise<Album | null>;
  fetchAlbumState: (albumId: string) => Promise<boolean>;
  fetchAlbumArtwork: (albumId: string) => Promise<Blob | null>;
  close: () => void;
};

export const SavedMediaContext = createContext<SavedMediaContextValue>({
  db: null,
  fetchMedia: () => Promise.resolve(null),
  listAlbums: () => Promise.resolve([]),
  fetchAlbumDetails: () => Promise.resolve(null),
  fetchAlbumState: () => Promise.resolve(false),
  fetchAlbumArtwork: () => Promise.resolve(null),
  close: () => undefined,
});

export function SavedMediaContextProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [db, setDb] = useState<IDBDatabase | null>(null);

  useEffect(() => {
    const request = indexedDB.open("cache");
    request.onupgradeneeded = () => {
      request.result.createObjectStore("media");
      request.result.createObjectStore("artwork");
      request.result.createObjectStore("albumSummary");
      request.result.createObjectStore("albumDetails");
      request.result.createObjectStore("albumState");
    };
    request.onsuccess = () => {
      setDb(request.result);
    };
    request.onerror = () => {
      console.log("error when loading db, saving anyway", request.result);
      setDb(request.result);
    };
  }, []);

  function fetchMedia(mediaId: string) {
    if (!db) {
      return Promise.resolve(null);
    }
    const tx = db.transaction("media", "readonly");
    const store = tx.objectStore("media");
    return new Promise((r) => {
      const op = store.get(mediaId);
      op.onsuccess = (ev) => r(op.result);
    }) as any;
  }
  function close() {
    if (!db) {
      return;
    }
    db.close();
    console.log("closed db in savedMediaContext");
  }

  function listAlbums() {
    if (!db) {
      return Promise.resolve(null);
    }
    const tx = db.transaction("albumSummary", "readonly");
    const store = tx.objectStore("albumSummary");
    return new Promise((r) => {
      const op = store.getAll();
      op.onsuccess = (ev) => r(op.result);
    }) as any;
  }

  function fetchAlbumDetails(albumId: string) {
    if (!db) {
      return Promise.resolve(null);
    }
    const tx = db.transaction("albumDetails", "readonly");
    const store = tx.objectStore("albumDetails");
    return new Promise((r) => {
      const op = store.get(albumId);
      op.onsuccess = (ev) => r(op.result);
    }) as any;
  }
  function fetchAlbumState(albumId: string) {
    if (!db) {
      return Promise.resolve(false);
    }
    const tx = db.transaction("albumState", "readonly");
    const store = tx.objectStore("albumState");
    return new Promise((r) => {
      const op = store.get(albumId);
      op.onsuccess = (ev) => r(op.result ? true : false);
    }) as any;
  }
  function fetchAlbumArtwork(albumId: string) {
    if (!db) {
      return Promise.resolve(null);
    }
    const tx = db.transaction("artwork", "readonly");
    const store = tx.objectStore("artwork");
    return new Promise((r) => {
      const op = store.get(albumId);
      op.onsuccess = (ev) => r(op.result ? op.result : null);
    }) as any;
  }

  return (
    <SavedMediaContext.Provider
      value={{
        db,
        fetchMedia,
        listAlbums,
        fetchAlbumDetails,
        fetchAlbumState,
        fetchAlbumArtwork,
        close,
      }}
    >
      {children}
    </SavedMediaContext.Provider>
  );
}

export function useMedia(mediaId: string | undefined | null) {
  const [url, setUrl] = useState("");
  const savedMedia = useContext(SavedMediaContext);

  useEffect(() => {
    if (!mediaId) {
      return;
    }
    savedMedia.fetchMedia(mediaId).then((r) => {
      // console.log("resolved media from db ", r, mediaId);
      if (r && r.status === "saved") {
        setUrl(URL.createObjectURL(r.blob));
      } else {
        setUrl(trackUrl(mediaId));
      }
    });
    return () => setUrl("");
  }, [mediaId, savedMedia.fetchMedia]);

  return url;
}

export function useArtworkUrl(albumId: string | undefined) {
  const [url, setUrl] = useState<string | null>(null);
  const savedMedia = useContext(SavedMediaContext);
  useEffect(() => {
    if (!albumId) {
      return;
    }
    savedMedia.fetchAlbumArtwork(albumId).then((r) => {
      if (r) {
        setUrl(URL.createObjectURL(r));
      }
    });
    return () => setUrl(null);
  }, [albumId, savedMedia.fetchMedia]);

  return url;
}
