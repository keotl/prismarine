<template>
  <div class="bounding-box">
    <div class="album-artwork" v-if="imageUrl !== ''" >
      <img v-bind:src="albumAtwork" class="image"/>
    </div>
    <div v-if="imageUrl === ''" class="album-artwork">
      <i class="material-icons md-48 placeholder">music_note</i>
    </div>
  </div>
</template>

<script>
import { waveformServer } from "../../config";

export default {
  props: ["imageUrl"],
  computed: {
    albumAtwork() {
      return `${waveformServer}${this.imageUrl}`;
    }
  }
};
</script>

<style scoped lang="scss">
@import "../../styles.sass";

.bounding-box {
  width: 12rem;
  height: 12rem;
  display: flex;
  align-items: center;
}

.album-artwork {
  border: 3px solid $text-light;
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  transition: 0.2s;
  transition-property: color, border;
}

.album-artwork:hover {
  border: 3px solid $border;
  transform: scale(1.02);
}

.placeholder {
  flex: 1;
  margin-top: 4.2rem;
  margin-bottom: 4.2rem;
  text-align:center;
  font-size: 50px;
  transition: 0.2s;
  transition-property: color, border;
  color: $text-light;
}

.album-artwork:hover .placeholder {
  color: white;
  transition: 0.2s;
  transition-property: color, border;
  transform: scale(1.02);
}
</style>
