import { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Album } from "../api";
import { ActionButton } from "../components/ActionButton";
import { TrackRow } from "../components/album/TrackRow";
import { Artwork } from "../components/Artwork";
import { HeaderContext } from "../context/HeaderContext";
import { PlaybackContext } from "../context/PlaybackContext";
import { SavedMediaContext, useArtworkUrl } from "../context/SavedMediaContext";
import { WORKER_INSTANCE } from "../worker/worker";
import styles from "./AlbumView.module.css";

export function AlbumView() {
  const { albumId } = useParams();
  const savedMedia = useContext(SavedMediaContext);
  const playback = useContext(PlaybackContext);
  const [album, setAlbum] = useState<Album | null>(null);
  const [isDownloaded, setIsDownloaded] = useState(false);
  useEffect(() => {
    savedMedia.fetchAlbumDetails(albumId!).then(setAlbum);
    savedMedia.fetchAlbumState(albumId!).then(setIsDownloaded);
    return () => {
      setAlbum(null);
      setIsDownloaded(false);
    };
  }, [setAlbum, savedMedia.fetchAlbumDetails, albumId]);
  const artworkUrl = useArtworkUrl(album?.id);
  const header = useContext(HeaderContext);
  useEffect(() => {
    header.update({ visible: false });
  }, [header.update]);

  if (!album) {
    return <></>;
  }

  return (
    <div className={styles.container}>
      <div className={styles.navigationBar}>
        <div>
          <ActionButton
            color="var(--action)"
            icon="arrow_back_ios"
            onClick={() => window.history.back()}
          />
        </div>
        <div>
          <ActionButton
            icon="cloud_download"
            active={isDownloaded}
            onClick={() =>
              WORKER_INSTANCE.postMessage({ command: "saveAlbum", albumId })
            }
          />
        </div>
      </div>
      <div>
        <div className={styles.header}>
          <Artwork imageUrl={artworkUrl} />
          <div>{album.name}</div>
          <div className={styles.subtitle}>{album.artist}</div>
          <div className={styles.subtext}>
            {album.genre} • {album.year}
          </div>
        </div>

        <div className={styles.buttonContainer}>
          <div
            className={styles.button}
            onClick={() => playback.playTracks(album.tracks, [])}
          >
            <span className="material-symbols-rounded">play_arrow</span>
            Play
          </div>
          <div
            className={styles.button}
            onClick={() => {
              const shuffled = [...album.tracks];
              shuffled.sort(() => Math.random() - 0.5);
              playback.playTracks(shuffled, []);
            }}
          >
            <span className="material-symbols-rounded">shuffle</span> Shuffle
          </div>
        </div>

        <div>
          {album.tracks.map((t, i) => (
            <TrackRow
              track={t}
              key={t.id}
              onClick={() =>
                playback.playTracks(
                  album.tracks.slice(i),
                  album.tracks.slice(0, i)
                )
              }
            />
          ))}
        </div>
      </div>
    </div>
  );
}
