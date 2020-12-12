<template>
<div>
  <div class="dropdown-item section-title" v-if="results.length > 0">Tracks</div>
  <div class="dropdown-divider" v-if="results.length > 0" />
  <router-link tag="a" v-for="track of results" v-bind:key="track.id" v-bind:to="`/album/${track.album_id}`" class="dropdown-item result">
    <div class="container" style="flex-direction: row; display: flex; ">
      <div class="info-item">
        <SearchResultThumbnail v-bind:imagePath="track.artwork_url" />
      </div>
      <div class="info-item">
        <div>
          {{ track.title }}
        </div>
        <div class="artist-name">
          {{ track.artist }}
        </div>
      </div>

    </div>
  </router-link>

</div>
</template>

<script>
import {
  searchTracks
} from '../../api/waveform';
import SearchResultThumbnail from './SearchResultThumbnail';

export default {

  props: ['query'],
  data: () => ({
    results: []
  }),
  components: {
    SearchResultThumbnail
  },
  async created() {
    this.results = await searchTracks(this.query);
  },
  watch: {
    async query(newVal) {
      this.results = await searchTracks(newVal);
    }
  }

}
</script>

<style scoped lang="scss">
@import '../../styles.sass';

.result {
    text-align: left;
}
a.dropdown-item:hover {
    background-color: $content-card-accent-background;
}
.artist-name {
    color: $text-light;
}
.info-item {
    margin-right: 1rem;
    color: $text;
}
.section-title {
    color: $text;
    font-weight: bold;
}
.dropdown-divider {
    background-color: $text-light;
}
</style>
