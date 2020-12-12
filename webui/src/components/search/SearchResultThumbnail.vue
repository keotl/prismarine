<template>
  <div class="image is-48x48">
    <img v-bind:src="url" style="max-height: none" v-if="url !== ''" />
  </div>
</template>

<script>
import { waveformServer } from "../../config";

export default {
  props: ["imagePath"],
  data: () => ({
    url: ""
  }),
  created() {
    this.updateUrl();
  },
  methods: {
    updateUrl() {
      if (this.imagePath !== "") {
        this.url = `${waveformServer}${this.imagePath}`;
      } else {
        this.url = "";
      }
    }
  },
  watch: {
    imagePath(newVal) {
      this.url = newVal;
      this.updateUrl();
    }
  }
};
</script>

<style scoped lang="scss">
</style>
