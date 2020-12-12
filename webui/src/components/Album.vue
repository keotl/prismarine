<template>
<div class="columns" style="margin-bottom: 0px">
  <div class="column is-one-third">
    <div style="height: 4em" />

    <div class="image" style="margin-left: 3rem; margin-right: 3rem;">
      <Artwork v-bind:imageUrl="album.artwork" v-bind:isPlaying="isPlaying"/>
      <!-- <img v-bind:src="artwork" class="album-artwork" v-bind:class="{'playing-album-artwork': isPlaying}" /> -->
    </div>
  </div>
  <div class="column" style="width: 100%;margin-right: 1rem;">
    <div class="box info-box" style="display:flex; justify-content: space-between;">
      <div>
        <div>
          {{ album.name }}
        </div>
        <div class="artist-info">
          <router-link tag="span" class="hidden-link" v-bind:to="`/artist/${album.artist_id}`">{{ album.artist }} <span v-if="album.year !== 0">({{ album.year }})</span> </router-link>

        </div>
      </div>

      <div>
        <div class="album-info">
          {{ album.genre }}
        </div>
        <div class="album-info">
          {{ album.tracks ? album.tracks.length : 0 }} tracks

        </div>
      </div>

    </div>
    <div class="box track-list">
      <Track v-for="track of album.tracks" v-bind:info="track" v-bind:key="track.id" v-on:play-track="queueAlbumStartingAtTrack($event)" />
    </div>
</div>

</div>
</template>

<script>
import {
  getAlbumInfo
} from '../api/waveform';
import Track from './Track';
import {
  PlayerEventBus,
  currentlyPlaying
} from '../player-event';
import Artwork from './Artwork';
import {
  waveformServer
} from '../config';

export default {
  data: () => ({
    album: {},
    isPlaying: false
  }),
  components: {
    Track,
    Artwork
  },
  async beforeCreate() {
    const albumId = this.$route.params.id;
    this.album = await getAlbumInfo(albumId);
    PlayerEventBus.$on('playing', trackId => {
      this.isPlaying = this.isTrackIdInAlbum(trackId);
    });
    PlayerEventBus.$on('stopped', () => {
      this.isPlaying = false;
    })
    this.isPlaying = this.isTrackIdInAlbum(currentlyPlaying);
  },
  methods: {
    queueAlbumStartingAtTrack(trackId) {
      const queuedTracks = [];
      let nextTrackIndex = -1;
      for (let i = 0; i < this.album.tracks.length; i++) {
        if (trackId === this.album.tracks[i].id) {
          nextTrackIndex = i;
          break;
        }
      }
      for (let i = nextTrackIndex; i < this.album.tracks.length; i++) {
        queuedTracks.push(this.album.tracks[i]);
      }

      PlayerEventBus.$emit('squash-queue-tracks', queuedTracks);
    },
    isTrackIdInAlbum(trackId) {
      try {
        for (let track of this.album.tracks) {
          if (track.id === trackId) {
            return true;
          }
        }
        return false;
      } catch (Exception) {
        return false;
      }
    }
  },
  computed: {
  },
  watch: {
    '$route.params.id': async function(newId) {
      this.album = await getAlbumInfo(newId);
      this.isPlaying = this.isTrackIdInAlbum(currentlyPlaying);
    }
  }
}
</script>

<style scoped lang="scss">
@import '../styles.sass';
* {
    @extend .no-select;
}

.artist-info {
    color: $text-light;
}

.info-box {
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    margin-top: 1em;
    padding-left: 1em;
    background-color: $content-card-background;
    color: $text;
}

.album-info {
    color: $text-light;
    text-align: right;
}
.track-list {
    background-color: $content-card-background;
}
.hidden-link {
    cursor: pointer;
}
</style>
