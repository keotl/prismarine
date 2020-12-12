<template>
<div>
  <router-link :to="albumLink"> {{ info.artist }} {{ info.name }} </router-link>
</div>
</template>

<script>
import {
  getAlbumInfo
} from '../api/waveform'

export default {
  props: ['albumId'],
  data: () => ({
    info: {}
  }),
  async created() {
    this.info = await getAlbumInfo(this.albumId);
  },
  computed: {
    albumLink() {
      return `/album/${this.albumId}`;
    }
  }


}
</script>

<style>

</style>
