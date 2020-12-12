<template>
  <div class="bounding-box">
    <div class="album-artwork" v-if="imageUrl !== ''"  v-bind:class="{'playing-album-artwork': isPlaying}">
      <img v-bind:src="albumAtwork" class="image"/>
    </div>
    <div v-if="imageUrl === ''" class="album-artwork" v-bind:class="{'playing-album-artwork': isPlaying}">
      <i class="material-icons md-48 placeholder">music_note</i>
    </div>
  </div>
</template>

<script>
import { waveformServer } from "../config";

export default {
  props: ["imageUrl", "isPlaying"],
  computed: {
    albumAtwork() {
      return `${waveformServer}${this.imageUrl}`;
    }
  }
};
</script>

<style scoped lang="scss">
@import "../styles.sass";

.album-artwork {
    border: 3px solid $border;
    box-shadow: 8px 10px 10px 2px $menu-background;
}

.playing-album-artwork {
    border: 3px solid $accent-secondary;
    color: $accent-secondary;
}

.placeholder {
    font-size: 96px;
    text-align: center;
    padding-top: 35%;
    padding-bottom: 35%;
    width: 100%;
}

</style>
