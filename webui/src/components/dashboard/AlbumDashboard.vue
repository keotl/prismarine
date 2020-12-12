<template>
  <div class="album-container">
    <div v-for="album of albums" v-bind:key="album.id" class="album">
      <router-link v-bind:to="`/album/${album.id}`" tag="div" class="album">
        <artwork-thumbnail v-bind:imageUrl="album.artwork_url" />
        <div class="album-info">
          <div class="album-name">
            {{truncateIfTooLong(album.name)}}
          </div>
          <div class="artist-name">
            {{truncateIfTooLong(album.artist)}}
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { getAlbumSummary } from "../../api/waveform";

import ArtworkThumbnail from "./ArtworkThumbnail";

export default {
  data: () => ({
    albums: []
  }),
  components: {
    ArtworkThumbnail
  },
  async created() {
    this.albums = await getAlbumSummary();
    this.albums.sort(function(a, b) {
      var itemA = a.artist.toLowerCase();
      var itemB = b.artist.toLowerCase();
      if (itemA < itemB) return -1;
      if (itemA > itemB) return 1;

      if (a.year < b.year) return -1;
      if (a.year > b.year) return 1;

      return 0;
    });
  },
  methods: {
    truncateIfTooLong(text) {
      const maxLength = 18;

      if (text.length > maxLength) {
        return `${text.substring(0, maxLength)}...`;
      }
      return text;
    }
  }
};
</script>

<style scoped lang="scss">
@import "../../styles.sass";
.album-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
  justify-content: center;
  overflow-y: auto;

  width: 100%;
  height: fit-content;
  max-height: 100%;
}

.album-info {
  margin-bottom: 1rem;
}

.artist-name {
  color: $text-light;
}

.album {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  cursor: pointer;
}

.box {
  background-color: $content-card-background;
  color: $text;
  margin-right: 2rem;
}
</style>
