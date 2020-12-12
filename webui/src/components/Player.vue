<template>
<div v-if="currentTrack !== undefined" style="z-index: 100">
  <audio v-bind:src="audioUrl" ref="audiotag" v-on:ended="advanceTrack" v-on:timeupdate="updateSeekBar" autoplay/>
  <div class="progress-slider" v-on:mousedown="startSeeking" v-on:mouseup="stopSeeking" v-on:click="seek">
    <div class="progress" v-bind:style="{width: playedPercentage + '%'}" />
    <div class="playback-pin" />
    <div class="loaded" v-bind:style="{width: bufferedPercentage + '%'}" />
  </div>
  <div class="bottom-bar">
    <CurrentTrackInfo v-bind:track="currentTrack" />

    <PlaybackControls v-bind:isPlaying="isPlaying()" v-on:next="advanceTrack" v-on:play="play" v-on:stop="stopPlayback" v-on:previous="backTrack" v-on:pause="pause" />
    <div class="time-info">
      <VolumeControl v-on:volume="updateVolume" />
      <div>
        {{currentTime}} / {{ totalTime }}
      </div>
    </div>
  </div>
</div>
</template>

<script>
import {
  PlayerEventBus
} from '../player-event';
import {
  waveformServer
} from '../config';
import {
  MouseEventBus
} from '../mouse-event-bus';
import {
  formatDuration
} from '../util/formatting';

import PlaybackControls from './player/PlaybackControls';
import CurrentTrackInfo from './player/CurrentTrackInfo';
import VolumeControl from './player/VolumeControl';

export default {
  components: {
    CurrentTrackInfo,
    PlaybackControls,
    VolumeControl
  },
  data: () => ({
    currentTrack: undefined,
    playQueue: [],
    previousTracks: [],
    playedPercentage: 0,
    bufferedPercentage: 0,
    isSeeking: false,
    currentTime: 0,
    totalTime: 0
  }),

  methods: {
    playTrack(track) {
      this.currentTrack = track;
      PlayerEventBus.$emit('playing', track.id);
    },
    queueTracks(tracks) {
      for (let track of tracks) {
        this.playQueue.push(track);
      }
      if (!this.isPlaying()) {
        this.advanceTrack();
      }
    },
    async squashQueueTracks(tracks) {
      this.stopPlayback();
      await new Promise(resolve => setTimeout(resolve, 30));
      this.queueTracks(tracks);
    },
    stopPlayback() {
      this.currentTrack = undefined;
      this.playQueue = [];
    },
    handleMousePosition(event) {
      if (this.isSeeking && MouseEventBus.isMouseDown()) {
        this.seek(event);
      } else {
        this.isSeeking = false;
      }
    },
    seek(event) {
      const screenWidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;
      const seekPosition = event.x / screenWidth * this.$refs.audiotag.duration;
      this.$refs.audiotag.currentTime = seekPosition;
    },
    startSeeking() {
      this.isSeeking = true;
    },
    stopSeeking() {
      this.isSeeking = false;
    },
    play() {
      this.$refs.audiotag.play();
    },
    pause() {
      this.$refs.audiotag.pause();
    },
    advanceTrack() {
      this.previousTracks.push(this.currentTrack);
      this.playTrack(this.playQueue.shift());
    },
    backTrack() {
      if (this.$refs.audiotag.currentTime < 5) {
        this.playQueue.unshift(this.currentTrack);
        this.playTrack(this.previousTracks.pop());
      } else {
        this.$refs.audiotag.currentTime = 0;
      }
    },
    isPlaying() {
      try {
        return !this.$refs.audiotag.paused;
      } catch (Exception) {
        return false;
      }
    },
    updateSeekBar() {
      if (!this.$refs.audiotag) {
        return;
      }
      const currentTime = this.$refs.audiotag.currentTime;
      const totalDuration = this.$refs.audiotag.duration;
      this.currentTime = formatDuration(currentTime);
      this.totalTime = formatDuration(totalDuration);

      this.playedPercentage = currentTime / totalDuration * 100;
      const timeRangeLength = this.$refs.audiotag.buffered.length;
      let currentBufferRange = 0;
      for (let range = 0; range < timeRangeLength; range++) {
        const rangeStartTime = this.$refs.audiotag.buffered.start(range);
        const rangeEndTime = this.$refs.audiotag.buffered.end(range);
        if (currentTime >= rangeStartTime && currentTime < rangeEndTime) {
          currentBufferRange = range;
        }
      }
      this.bufferedPercentage = (this.$refs.audiotag.buffered.end(currentBufferRange) - currentTime) / totalDuration * 100;
    },
    updateVolume(volume) {
      this.$refs.audiotag.volume = volume;
    },
    updateWindowTitle() {
      if (this.currentTrack !== undefined) {
        document.title = `${this.currentTrack.artist} - ${this.currentTrack.title} - ${this.isPlaying() ? '' : 'Paused - '}Prismarine`;
      } else {
        document.title = "Prismarine Player";

      }
    }
  },
  computed: {
    audioUrl() {
      return `${waveformServer}/media/track/${this.currentTrack.id}`;
    },
  },
  created() {
    PlayerEventBus.$on('play-track', track => this.playTrack(track));
    PlayerEventBus.$on('queue-tracks', tracks => this.queueTracks(tracks));
    PlayerEventBus.$on('squash-queue-tracks', tracks => this.squashQueueTracks(tracks));
    PlayerEventBus.$on('volume', volume => this.updateVolume(volume));
    MouseEventBus.$on('mouse-move', (event) => this.handleMousePosition(event));
  },
  updated() {
    this.updateWindowTitle();
    if (this.currentTrack === undefined) {
    	PlayerEventBus.$emit('stopped');
    }
  },
  mounted() {
    this.updateWindowTitle();
  }
}
</script>

<style scoped lang="scss">
@import '../styles.sass';

* {
    @extend .no-select;
}
.bottom-bar {
    display: flex;
    background-color: $menu-background;
    color: $text;
    height: 72px;
    z-index: -1;
    justify-content: space-between;
}

.progress-slider:hover {
    height: 8px;
    transition: 0.2s;
    transition-property: height;
}
.progress-slider:hover > .playback-pin {
    top: -1px;
    transition: 0.2s;
    transition-property: top;
}

.progress-slider {
    display: flex;
    width: 100%;
    height: 4px;
    background-color: $menu-accent-background;
    box-shadow: 0 -2px 2px 0 $menu-accent-background;
    transition: 0.2s;
    transition-property: box-shadow;
    cursor: pointer;
}
.progress {
    height: 100%;
    background-color: $accent;
    box-shadow: 0 -2px 2px 0 $accent;
    border-radius: 0;
    transition-property: width;
    transition: 0.2s;
}
.loaded {
    height: 100%;
    background-color: $text-light;
    box-shadow: 0 -2px 2px 0 $text-light;
    border-radius: 0;
    transition-property: width;
    transition: 0.2s;
}
.playback-pin {
    background-color: $accent-secondary;
    height: 8px;
    width: 8px;
    border-radius: 8px;
    top: -3px;
    left: -4px;
    position: relative;
    display: inline-block;
    box-shadow: 0 0 1px 6px $accent-secondary;
    z-index: 1000;
}
.time-info {
    color: $text-light;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-right: 1rem;
    flex: 1;
    text-align: right;
    align-items: center;
}
</style>
