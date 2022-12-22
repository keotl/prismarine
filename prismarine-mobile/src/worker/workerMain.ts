import { MediaRepository } from "./mediaRepository";

export {};

if (!navigator.locks) {
  // @ts-ignore
  navigator.locks = {
    // @ts-ignore
    request: (name, a, b) => {
      if (b) {
        b("dummy");
      } else {
        a("dummy");
      }
    },
  };
}

const mediaRepository = new MediaRepository();

type SaveMediaMessage = {
  command: "saveMedia";
  mediaId: string;
};

type InitializeMessage = {
  command: "initialize";
};

type UpdateLibraryMetadataMessage = {
  command: "updateLibraryMetadata";
};

type SaveAlbumMessage = {
  command: "saveAlbum";
  albumId: string;
};

type CloseDbMessage = {
  command: "closeDb";
};

type WorkerMessage =
  | SaveMediaMessage
  | InitializeMessage
  | UpdateLibraryMetadataMessage
  | SaveAlbumMessage
  | CloseDbMessage;

onmessage = (e: MessageEvent<WorkerMessage>) => {
  console.log("worker got message ", e.data?.command, e.data);
  switch (e.data.command) {
    case "initialize":
      mediaRepository
        .init()
        .then(() => mediaRepository.reloadIncomplete())
        .then(() => setInterval(() => mediaRepository.poll(), 1000));
      break;
    case "saveMedia":
      mediaRepository.queueDownload(e.data.mediaId);
      break;
    case "updateLibraryMetadata":
      mediaRepository.updateLibraryMetadata();
      break;
    case "saveAlbum":
      mediaRepository.saveAlbum(e.data.albumId);
      break;
    case "closeDb":
      mediaRepository.closeDb();
      break;
    default:
      console.log("worker got unknown message ", e);
  }
};
