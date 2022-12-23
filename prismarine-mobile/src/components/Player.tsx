import { useContext, useEffect, useRef, useState } from "react";
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
  }, [isPaused, playback.state]);

  useEffect(() => {
    if (!playback.current) {
      navigator.mediaSession.metadata = null;
    } else {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: playback.current.title,
        artist: playback.current.artist,
        album: playback.current.album,
        artwork: artworkUrl
          ? [
              {
                src: artworkUrl,
                sizes: "32x32",
                type: "image/png",
              },
              {
                src: artworkUrl,
                sizes: "256x256",
                type: "image/png",
              },
              {
                src: artworkUrl,
                sizes: "512x512",
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
  }, [
    playback.current,
    isPaused,
    navigator.mediaSession.metadata,
    audioElement.current,
    artworkUrl,
  ]);

  usePreloadedTrack(
    playback.queue.length > 0 ? playback.queue[0].id : undefined
  );

  function updatePlayerStatus() {
    setPaused(audioElement.current?.paused || false);
  }
  function togglePlayPause() {
    if (audioElement.current?.paused) {
      audioElement.current.play();
    } else {
      audioElement.current?.pause();
    }
  }

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
            onEnded={() => playback.advance()}
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
