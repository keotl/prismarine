<template>
  <div class="artist-container">
    <div v-for="artist of artists" v-bind:key="artist.id" class="artist">
      <router-link v-bind:to="`/artist/${artist.id}`" tag="div" class="album">
        <artwork-thumbnail v-bind:imageUrl="artist.artwork_url" />
        <div class="album-info">
          <div class="artist-container-name">
            {{artist.name}}
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { getArtistSummary } from "../../api/waveform";
import { waveformServer } from "../../config";
import ArtworkThumbnail from "./ArtworkThumbnail";

export default {
  data: () => ({
    artists: []
  }),
  components: {
    ArtworkThumbnail
  },
  async created() {
    this.artists = await getArtistSummary();
    this.artists.sort(function(a, b) {
      var itemA = a.name.toLowerCase();
      var itemB = b.name.toLowerCase();
      if (itemA < itemB) return -1;
      if (itemA > itemB) return 1;
      return 0;
    });
  },
  methods: {
    artistArtwork(artist) {
      return `${waveformServer}${artist.artwork_url}`;
    }
  }
};
</script>


<style scoped lang="scss">
@import "../../styles.sass";
.artist-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
  justify-content: center;
  overflow-y: auto;

  width: 100%;
  height: fit-content;
  max-height: 100%;
}

.artist-container-name {
  margin-bottom: 2rem;
}

.artist {
  margin-left: 1rem;
  margin-right: 1rem;
  cursor: pointer;
}

.artist-artwork {
  border: 3px solid $border;
}

.box {
  background-color: $content-card-background;
  color: $text;
  margin-right: 2rem;
}
</style>
