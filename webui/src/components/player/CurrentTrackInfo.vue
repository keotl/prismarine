<template>
<div class="playback-info-container">
  <router-link v-if="track.artwork_url !== ''" tag="img" class="playback-thumbnail" v-bind:src="trackArtwork(track.artwork_url)" v-bind:to="`/album/${track.album_id}`"/>
  <router-link v-if="track.artwork_url === ''" tag="div" class="playback-thumbnail placeholder" v-bind:to="`/album/${track.album_id}`">
  <i class="material-icons">music_note</i>
  </router-link>
  <div class="track-infobox">
    <div>
      {{ track.title }}
    </div>
    <div class="artist-name"> {{ track.artist }} – {{ track.album }}</div>
  </div>
</div>
</template>

<script>
import {
  waveformServer
} from '../../config';

export default {
  props: ['track'],
  methods: {
    trackArtwork(path) {
      return `${waveformServer}${path}`;
    }
  }
}
</script>

<style scoped lang="scss">
@import '../../styles.sass';

.playback-info-container {
    height: 100%;
    display: flex;
    flex: 1;
}
.playback-thumbnail {
    max-height: 100%;
    cursor: pointer;
}
.placeholder {
    width: 72px;
    border: solid 3px $text-light;
    color: $text-light;
    display: flex;
    justify-content: center;
    align-items: center;
    transition-property: color border;
    transition-duration: 0.2s;
}
.placeholder:hover {
    color: $border;
    border-color: $border;
}
.artist-name {
    color: $text-light;
}
.track-infobox {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-left: 0.8rem;
}
</style>
