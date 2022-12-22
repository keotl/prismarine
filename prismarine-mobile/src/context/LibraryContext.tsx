import {
  createContext,
  ReactNode,
  useContext,
  useEffect,
  useState,
} from "react";
import { Album, AlbumSummary } from "../api";
import { SavedMediaContext } from "./SavedMediaContext";

export type LibraryContextType = {
  albums: AlbumSummary[];
  albumDetails: { [albumId: string]: Album };
};

export const LibraryContext = createContext<LibraryContextType>({
  albums: [],
  albumDetails: {},
});

export function LibraryContextProvider({ children }: { children: ReactNode }) {
  const [albums, setAlbums] = useState<AlbumSummary[]>([]);
  const [albumDetails, setAlbumDetails] = useState<{ [id: string]: Album }>({});
  const savedMedia = useContext(SavedMediaContext);

  // useEffect(() => {
  //   savedMedia.listAlbums().then((r) => setAlbums(r));
  //   return () => setAlbums([]);
  // }, [setAlbums, savedMedia.listAlbums]);

  useEffect(() => {
    const interval = setTimeout(() => {
      savedMedia
        .listAlbums()
        .then((r) =>
          setAlbums(
            r.sort((a, b) =>
              a.artist === b.artist
                ? a.name.localeCompare(b.name)
                : a.artist.localeCompare(b.artist)
            )
          )
        );
    }, 100);
    return () => clearTimeout(interval);
  }, [setAlbums, savedMedia]);

  return (
    <LibraryContext.Provider value={{ albums, albumDetails }}>
      {children}
    </LibraryContext.Provider>
  );
}
