import { useContext, useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import { HeaderContext } from "../context/HeaderContext";
import { LibraryContext } from "../context/LibraryContext";
import { AlbumListViewRow } from "./AlbumListViewRow";

export function AlbumsListView() {
  const library = useContext(LibraryContext);
  const [searchParams, setSearchParams] = useSearchParams();
  const filterSaved = searchParams.get("saved") === "true";

  const header = useContext(HeaderContext);
  useEffect(() => {
    header.update({
      visible: true,
      title: "Albums",
      action: {
        text: "Saved",
        onClick: () => {
          setSearchParams((x) => {
            x.set("saved", filterSaved ? "false" : "true");
            return x;
          });
        },
      },
    });
  }, [header.update, setSearchParams]);

  useEffect(() => {
    const scrollPos = searchParams.get("scroll");
    if (!scrollPos) {
      return;
    }
    setTimeout(() => {
      document.querySelector(".main-content")!.scrollTo({
        top: parseFloat(scrollPos),
      });
    }, 100);
    setSearchParams((x) => {
      x.delete("scroll");
      return x;
    });
  }, [searchParams, setSearchParams]);

  if (library.albums.length === 0) {
    return (
      <div>There is nothing here. Try refreshing the library from the Settings tab.</div>
    );
  }

  return (
    <>
      {library.albums.map((a) => (
        <AlbumListViewRow
          key={a.id}
          album={a}
          hideUnsaved={filterSaved}
          onNavigate={() => {
            setSearchParams((x) => {
              x.set(
                "scroll",
                document.querySelector(".main-content")!.scrollTop.toString()
              );
              return x;
            });
          }}
        />
      ))}
    </>
  );
}
