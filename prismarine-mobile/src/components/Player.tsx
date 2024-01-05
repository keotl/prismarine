import { useCallback, useContext, useEffect, useRef, useState } from "react";
import { PlaybackContext } from "../context/PlaybackContext";
import { useArtworkUrl, useMedia } from "../context/SavedMediaContext";
import { ActionButton } from "./ActionButton";
import { Artwork } from "./Artwork";
import { ExpandedPlayer } from "./ExpandedPlayer";

import styles from "./Player.module.css";

export function Player() {
  const playback = useContext(PlaybackContext);

  const mediaUrl = useMedia(playback.current?.id);
  const [isPaused, setPaused] = useState(false);
  const audioElement = useRef<HTMLAudioElement>(null);
  const artworkUrl = useArtworkUrl(playback.current?.album_id);
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    if (playback.state === "playing" || playback.state === "paused") {
      navigator.mediaSession.playbackState = playback.state;
    } else {
      navigator.mediaSession.playbackState = "none";
    }
    return () => {
      navigator.mediaSession.playbackState = "none";
    };
  }, [isPaused, playback.state]);

  // const img96 = useResizedImage(artworkUrl, 96);
  const img384 = useResizedImage(artworkUrl, 384);

  const updatePlayerStatus = useCallback(() => {
    setPaused(audioElement.current?.paused || false);
  }, [audioElement]);
  const togglePlayPause = useCallback(() => {
    if (audioElement.current?.paused) {
      audioElement.current.play();
    } else {
      audioElement.current?.pause();
    }
  }, [audioElement]);

  useEffect(() => {
    if (!playback.current) {
      navigator.mediaSession.metadata = null;
    } else {
      navigator.mediaSession.metadata = null;
      navigator.mediaSession.metadata = new MediaMetadata({
        title: playback.current.title,
        artist: playback.current.artist,
        album: playback.current.album,
        artwork: artworkUrl
          ? [
              // {
              //   // Works in the small preview window on iPhone iOS 16+
              //   // But makes the artwork blurry when expanded, even if other sizes are available
              //   src: img96,
              //   sizes: "96x96",
              //   type: "image/png",
              // },
              {
                // This is the highest that seems to work on the iPhone iOS 16+
                // Works when the artwork is expanded, but doesn't in the small preview
                src: img384,
                sizes: "384x384",
                type: "image/png",
              },
            ]
          : [],
      });
      navigator.mediaSession.setActionHandler("play", togglePlayPause);
      navigator.mediaSession.setActionHandler("pause", togglePlayPause);
      navigator.mediaSession.setActionHandler("nexttrack", playback.advance);
      navigator.mediaSession.setActionHandler(
        "previoustrack",
        playback.reverse
      );
    }
    return () => {
      navigator.mediaSession.metadata = null;
    };
  }, [
    playback.current,
    isPaused,
    navigator.mediaSession.metadata,
    audioElement.current,
    artworkUrl,
    togglePlayPause,
    playback.advance,
    // img96,
    img384,
  ]);

  usePreloadedTrack(
    playback.queue.length > 0 ? playback.queue[0].id : undefined
  );

  return (
    <>
      {/* expanded view modal */}
      <ExpandedPlayer
        expanded={expanded}
        onClose={() => setExpanded(false)}
        imageUrl={artworkUrl}
        track={playback.current}
        isPaused={isPaused}
        onPrevious={playback.reverse}
        onNext={playback.advance}
        togglePlayPause={togglePlayPause}
        audioElement={
          <audio
            autoPlay
            ref={audioElement}
            src={mediaUrl}
            onEnded={playback.advance}
            onAbort={updatePlayerStatus}
            onPlay={updatePlayerStatus}
            onPause={updatePlayerStatus}
            onPlaying={updatePlayerStatus}
            id="audio"
            controls
          />
        }
      />
      {playback.current && (
        <div className={styles.container} onClick={() => setExpanded(true)}>
          <Artwork size={48} imageUrl={artworkUrl} />
          <div className={styles.title}>{playback.current?.title}</div>
          <div className={styles.buttonContainer}>
            <ActionButton
              icon={isPaused ? "play_arrow" : "pause"}
              active
              onClick={togglePlayPause}
            />
            <ActionButton
              icon="fast_forward"
              active
              onClick={playback.advance}
            />
          </div>
        </div>
      )}
    </>
  );
}

function usePreloadedTrack(trackId: string | undefined) {
  const nextTrackUrl = useMedia(trackId);
  useEffect(() => {
    if (!nextTrackUrl || nextTrackUrl.startsWith("blob")) {
      console.log("skiping", nextTrackUrl);
      return;
    }

    const timeoutId = setTimeout(() => {
      fetch(nextTrackUrl).catch((_) => undefined /* ignored */);
    }, 5000);

    return () => clearTimeout(timeoutId);
  }, [nextTrackUrl]);
}

function useResizedImage(artworkUrl: string | null, size: number) {
  const [resized, setResized] = useState<string>("");
  useEffect(() => {
    if (!artworkUrl) {
      return;
    }
    const img = new Image();
    img.src = artworkUrl;
    img.onload = () => {
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");
      if (img.naturalWidth < size && img.naturalHeight < size) {
        setResized(artworkUrl);
        return;
      }
      if (img.naturalWidth > img.naturalHeight) {
        canvas.width = size;
        canvas.height = (img.naturalHeight / img.naturalWidth) * size;
      } else {
        canvas.height = size;
        canvas.width = (img.naturalWidth / img.naturalHeight) * size;
      }
      ctx!.drawImage(img, 0, 0, canvas.width, canvas.height);

      setResized(canvas.toDataURL("image/png"));
    };
  }, [artworkUrl, size]);

  return resized;
}
