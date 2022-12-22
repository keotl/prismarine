import { ReactNode, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Track } from "../api";
import { Artwork } from "./Artwork";
import styles from "./ExpandedPlayer.module.css";

type Props = {
  expanded: boolean;
  onClose: () => void;
  audioElement: ReactNode;
  imageUrl: string | null;
  track: Track | null;
  isPaused: boolean;
  onPrevious: () => void;
  togglePlayPause: () => void;
  onNext: () => void;
};

export function ExpandedPlayer({
  expanded,
  onClose,
  audioElement,
  imageUrl,
  track,
  isPaused,
  ...props
}: Props) {
  const navigate = useNavigate();
  return (
    <div className={styles.anchor + (expanded ? "" : " " + styles.collapsed)}>
      <div
        className={styles.container + (expanded ? "" : " " + styles.collapsed)}
      >
        <div className={styles.closeButton} onClick={onClose}>
          <span className={"material-symbols-rounded " + styles.buttonIcon}>
            close
          </span>
        </div>

        <div
          className={styles.artworkContainer}
          onClick={() => {
            onClose();
            navigate(`/albums/${track?.album_id}`);
          }}
        >
          <Artwork imageUrl={imageUrl} />
        </div>

        <div className={styles.trackDescription}>
          <div className={styles.title}>{track?.title}</div>
          <div className={styles.artist}>{track?.artist}</div>
        </div>

        {audioElement}

        <div className={styles.buttonContainer}>
          <div className={styles.button} onClick={props.onPrevious}>
            <span className={"material-symbols-rounded " + styles.buttonIcon}>
              fast_rewind
            </span>
          </div>
          <div className={styles.button} onClick={props.togglePlayPause}>
            <span className={"material-symbols-rounded " + styles.buttonIcon}>
              {isPaused ? "play_arrow" : "pause"}
            </span>
          </div>
          <div className={styles.button} onClick={props.onNext}>
            <span className={"material-symbols-rounded " + styles.buttonIcon}>
              fast_forward
            </span>
          </div>
        </div>

        {/*<div className={styles.playingNextContainer}>
	  <div className={styles.playingNextTitle}>Playing Next</div>
	  </div>*/}
      </div>
    </div>
  );
}
