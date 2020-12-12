<template>
<div class="table-row" v-on:click="play" v-bind:class="{'playing-table-row': isPlaying}">
  <div class="track-number-button">
    {{ info.track_number }}
  </div>
  <div style="flex: 1">
    {{ info.title }} <span class="artist"> - {{ info.artist }} </span>
  </div>
  <div class="duration">
    {{ formattedDuration }}
  </div>
</div>
</template>

<script>
import {
  formatDuration
} from '../util/formatting';

import {
  PlayerEventBus,
  currentlyPlaying
} from '../player-event';

export default {
  props: ['info'],
  data: () => ({
    isPlaying: false
  }),
  methods: {
    play() {
      this.$emit('play-track', this.info.id);
    },
  },
  computed: {
    formattedDuration() {
      return formatDuration(this.info.length);
    }
  },
  created() {
    this.isPlaying = (this.info.id === currentlyPlaying);
    PlayerEventBus.$on('playing', trackId => this.isPlaying = (trackId === this.info.id));
    PlayerEventBus.$on('stopped', () => this.isPlaying = false);
  }
}
</script>

<style scoped lang="scss">
@import '../styles.sass';
.table-row {
    display: flex;
    padding-top: 0.5em;
    vertical-align: middle;
    color: $text;
    border-radius: 6px;
}
.playing-table-row {
    color: $accent-secondary;
    background-color: $content-card-accent-background;
}
.table-row:hover {
    background-color: $content-card-accent-background;
    cursor: pointer;
}
.artist {
    color: $text-light;
}
.track-number-button {
    width: 1.5rem;
    height: 2rem;
    margin-right: 0.8rem;
    color: $text-light;
    text-align: right;
}
.duration {
    color: $text-light;
    margin-right: 0.75rem;
}
</style>
