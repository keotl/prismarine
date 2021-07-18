<template>
<div class="columns">
  <div class="column is-one-quarter">
    <div style="height: 4em" />
    <div class="image" style="margin-left: 3rem; margin-right: 3rem;">
    <Artwork v-bind:imageUrl="artistImage" v-bind:isPlaying="false"/>
    </div>
  </div>
  <div class="column">
    <div style="height: 2rem;" />
    <div class="box">
      <div> {{ this.artist.name }}</div>
    </div>
    <div> Albums </div>
    <div style="display: flex; flex-wrap: wrap;">
      <div v-for="album of artist.albums" v-bind:key="album.id">

        <router-link v-bind:to="`/album/${album.id}`" tag="div" class="album">
          <img v-if="album.artwork_url !== ''" v-bind:src="albumArtwork(album)" class="image album-art" />
	  <div v-if="album.artwork_url === ''" class="placeholder album-art" >
	  <i class="material-icons md-48">music_note</i>
	  </div>
          <div class="album-info">
            <div>
              {{ truncateIfTooLong(album.name) }}
            </div>
            <div class="year-info" v-if="album.year !== 0">
              {{album.year}}
            </div>
          </div>

        </router-link>

      </div>
    </div>
  </div>
</div>
</template>

<script>
import {
  getArtistInfo
} from '../api/waveform';
import Artwork from './Artwork';
import {
  waveformServer
} from '../config';

export default {
  data: () => ({
    artist: {}
  }),
  components: {
    Artwork
  },
  methods: {
    albumArtwork(album) {
      return `${waveformServer}${album.artwork_url}`;
    },
    truncateIfTooLong(text) {
      const maxLength = 15;

      if (text.length > maxLength) {
        return `${text.substring(0, maxLength)}...`;
      }
      return text;
    },
    sortAlbums(albums) {
      return albums.sort(function(a, b) {
        if (a.year < b.year) return -1;
        if (a.year > b.year) return 1;
        return 0;
    });
    }
  },
  async created() {
    this.artist = await getArtistInfo(this.$route.params.id);
    this.artist.albums = this.sortAlbums(this.artist.albums);
  },
  computed: {
    artistImage() {
      return "";
      // TODO revert when using a new artist image API. - keotl 2021-07-18
      // return `${waveformServer}${this.artist.image_url}`;
    }
  },
  watch: {
    '$route.params.id': async function(newVal) {
      this.artist = await getArtistInfo(newVal);
      this.artist.albums = this.sortAlbums(this.artist.albums);
    }
  }

}
</script>

<style scoped lang="scss">
@import '../styles.sass';
.album {
    margin-right: 1rem;
    margin-left: 1rem;
    cursor: pointer;
}

.box {
    background-color: $content-card-background;
    color: $text;
    margin-right: 2rem;
}
.album-art {
  width: 128px;
  border: 3px solid $text-light;
  transition: 0.2s;
  transition-property: color, border;
}
.placeholder {
    height: 128px;
    text-align: center;
    color: $text-light;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.album-art:hover {
  border: 3px solid $border;
  transform: scale(1.02);
  color: $border;
}
.year-info {
    color: $text-light;
}
</style>
