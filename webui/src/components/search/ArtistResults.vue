<template>
<div>
  <div class="dropdown-item section-title" v-if="results.length > 0">Artists</div>
  <div class="dropdown-divider" v-if="results.length > 0" />
  <router-link tag="a" v-for="artist of results" v-bind:key="artist.id" v-bind:to="`/artist/${artist.id}`" class="dropdown-item result">
    <div class="container" style="flex-direction: row; display: flex; ">

      <div class="artist-thumbnail-placeholder" v-if="artist.artwork_url === ''">
        <i class="material-icons small"> music_note</i>

      </div>
      <img class="artist-thumbnail" v-if="artist.artwork_url !== ''" v-bind:src="artworkUrl(artist.artwork_url)" />
      <div class="info-item">
        {{ artist.name }}
      </div>
    </div>
  </router-link>

</div>
</template>

<script>
import {
  searchArtists
} from '../../api/waveform';
import {
  waveformServer
} from '../../config';

import SearchResultThumbnail from './SearchResultThumbnail';

export default {
  props: ['query'],
  data: () => ({
    results: []
  }),
  methods: {
    artworkUrl(path) {
      if (path !== '') {
        return `${waveformServer}${path}`;
      }
    }
  },
  components: {
    SearchResultThumbnail
  },
  async created() {
    this.results = await searchArtists(this.query);
  },
  watch: {
    async query(newValue) {
      this.results = await searchArtists(newValue);
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
    color: $text;
    margin-top: auto;
    margin-bottom: auto;
}
.section-title {
    color: $text;
    font-weight: bold;
}
.dropdown-divider {
    background-color: $text-light;
}

.artist-thumbnail-placeholder {
    background-color: $content-card-accent-background;
    color: $text;
    height: 48px;
    width: 48px;
    border-radius: 50%;
    margin-right: 0.8rem;
}
.artist-thumbnail-placeholder > * {
    margin-top: 8px;
    opacity: 0.8;
    font-size: 32px;
    margin-left: 8px;
}

.artist-thumbnail {
    min-height: 48px;
    border-radius: 50%;
    margin-right: 1rem;
}
</style>
