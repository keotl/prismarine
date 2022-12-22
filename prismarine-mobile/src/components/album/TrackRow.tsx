import { useContext, useEffect, useState } from "react";
import { Track } from "../../api";
import { SavedMediaContext } from "../../context/SavedMediaContext";
import { ActionButton } from "../ActionButton";
import styles from "./TrackRow.module.css";

type Props = {
  track: Track;
  onClick?: () => void;
};

export function TrackRow(props: Props) {
  const savedMedia = useContext(SavedMediaContext);
  const [isSaved, setIsSaved] = useState(false);
  useEffect(() => {
    savedMedia
      .fetchMedia(props.track.id)
      .then((t) => setIsSaved(t?.status === "saved"));
    return () => setIsSaved(false);
  }, [props.track, setIsSaved]);

  return (
    <div className={styles.container} onClick={props.onClick}>
      <div className={styles.trackNumber}>{props.track.track_number}</div>
	  <div className={styles.title}>{props.track.title}</div>
      <div className={styles.buttonContainer}>
        <div>
          {isSaved && (
            <span
              className={"material-symbols-rounded " + styles.downloadIcon}
            >
              download
            </span>
          )}
        </div>
        <ActionButton icon="more_horiz" />
      </div>
    </div>
  );
}
