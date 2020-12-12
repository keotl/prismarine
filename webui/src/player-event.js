import Vue from 'vue';
export const PlayerEventBus = new Vue();

export let currentlyPlaying = '';
PlayerEventBus.$on('playing', trackId => {
    currentlyPlaying = trackId;
});
