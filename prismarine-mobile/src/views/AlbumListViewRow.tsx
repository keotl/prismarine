import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AlbumSummary } from "../api";
import { SavedMediaContext, useArtworkUrl } from "../context/SavedMediaContext";
import styles from "./AlbumListViewRow.module.css";

type Props = {
  album: AlbumSummary;
  hideUnsaved?: boolean;
  onNavigate: () => void;
};

export function AlbumListViewRow({ album: a, hideUnsaved, onNavigate }: Props) {
  const navigate = useNavigate();
  const [isSaved, setIsSaved] = useState(false);
  const savedMedia = useContext(SavedMediaContext);
  const artworkUrl = useArtworkUrl(a.id);

  useEffect(() => {
    savedMedia.fetchAlbumState(a.id).then(setIsSaved);
    return () => setIsSaved(false);
  }, [a.id, savedMedia.fetchAlbumState]);

  if (hideUnsaved && !isSaved) {
    return <></>;
  }
  return (
    <div
      className={styles.row}
      onClick={() => {
        onNavigate();
        navigate("/albums/" + a.id + window.location.search);
      }}
    >
      {artworkUrl ? (
        <img className={styles.thumbnail} src={artworkUrl} />
      ) : (
        <div className={styles.thumbnail + " " + styles.placeholder}>
          <span className="material-symbols-rounded">music_note</span>
        </div>
      )}
      <div className={styles.title}>{a.name}</div>
      <div className={styles.actionsContainer}>
        {isSaved && (
          <span className={"material-symbols-rounded " + styles.downloadIcon}>
            download
          </span>
        )}
        {/*<ActionButton icon="favorite" />
        <ActionButton icon="more_horiz" />*/}
      </div>
    </div>
  );
}
