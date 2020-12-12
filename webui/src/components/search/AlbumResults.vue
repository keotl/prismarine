<template>
<div>
  <div class="dropdown-item section-title" v-if="results.length > 0">Albums</div>
  <div class="dropdown-divider" v-if="results.length > 0" />
  <router-link tag="a" v-for="album of results" v-bind:key="album.id" v-bind:to="`/album/${album.id}`" class="dropdown-item result">
    <div class="container" style="flex-direction: row; display: flex;">
      <div class="info-item">
        <SearchResultThumbnail v-bind:imagePath="album.artwork_url" />
      </div>
      <div class="info-item">
        <div>
          {{ album.name }}
        </div>
        <div class="artist-name">
          {{ album.artist }} <span v-if="album.year !== 0">({{ album.year }})</span>
        </div>
      </div>

    </div>
  </router-link>

</div>
</template>

<script>
import {
  searchAlbums
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
    this.results = await searchAlbums(this.query);
  },
  watch: {
    async query(newVal) {
      this.results = await searchAlbums(newVal);
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
