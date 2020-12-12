<template>
<div>
  <h1> Album Search</h1>
  <AlbumResult v-for="album of results" v-bind:albumId="album.id" v-bind:key="album.id" />

</div>
</template>

<script>
import {
  searchAlbums
} from '../api/waveform'

import AlbumResult from './AlbumResult'

export default {
  props: ['query'],
  data: () => ({
    results: []
  }),
  components: {
    AlbumResult
  },
  async created() {
    this.results = await searchAlbums(this.query);
  }
}
</script>

<style>

</style>
