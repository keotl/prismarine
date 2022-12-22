import { createContext, ReactNode, useReducer } from "react";
import { Track } from "../api";

type State = {
  state: "playing" | "paused" | "stopped";
  current: Track | null;
  queue: Track[];
  previous: Track[];
};
export type PlaybackContextValue = State & {
  playTracks: (tracks: Track[], previous: Track[]) => void;
  advance: () => void;
  reverse: () => void;
};

export const PlaybackContext = createContext<PlaybackContextValue>({
  state: "stopped",
  current: null,
  queue: [],
  previous: [],
  playTracks: () => undefined,
  advance: () => undefined,
  reverse: () => undefined,
});

type PlayAlbumAction = {
  type: "playAlbum";
  first: Track;
  next: Track[];
  previous: Track[];
};
type AdvanceAction = {
  type: "advance";
};
type ReverseAction = {
  type: "reverse";
};
type Action = PlayAlbumAction | AdvanceAction | ReverseAction;

function reduce(state: State, action: Action): State {
  switch (action.type) {
    case "playAlbum":
      return {
        state: "playing",
        current: action.first,
        queue: action.next,
        previous: action.previous,
      };
    case "advance":
      if (state.queue.length === 0) {
        return {
          state: "stopped",
          current: null,
          queue: [],
          previous: state.previous,
        };
      } else {
        return {
          state: state.state,
          current: state.queue[0],
          queue: state.queue.slice(1),
          previous: state.current
            ? [...state.previous, state.current]
            : state.previous,
        };
      }
    case "reverse":
      if (state.previous.length === 0) {
        return state;
      }
      return {
        state: state.state,
        current: state.previous[state.previous.length - 1],
        queue: state.current ? [state.current, ...state.queue] : state.queue,
        previous: state.previous.slice(0, state.previous.length - 1),
      };
    default:
      return state;
  }
}
export function PlaybackContextProvider(props: { children: ReactNode }) {
  const [state, dispatch] = useReducer(reduce, {
    state: "stopped",
    current: null,
    queue: [],
    previous: [],
  });

  function playTracks(tracks: Track[], previous: Track[]) {
    dispatch({
      type: "playAlbum",
      first: tracks[0],
      next: tracks.slice(1),
      previous,
    });

    // @ts-ignore
    document.getElementById("audio")!.load(); // Preload in the onclick callback, to workaround autoplay
  }
  function advance() {
    dispatch({ type: "advance" });
  }
  function reverse() {
    dispatch({ type: "reverse" });
  }

  return (
    <PlaybackContext.Provider
      value={{ ...state, playTracks, advance, reverse }}
    >
      {props.children}
    </PlaybackContext.Provider>
  );
}
