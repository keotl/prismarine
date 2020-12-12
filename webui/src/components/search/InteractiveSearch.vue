<template>
<div class="field dropdown is-right" v-bind:class="{'is-active': shouldShowSearchResults}">
  <div class="control has-icons-left">
    <input v-model="query" class="input" type="search" v-on:focusout="focusOut" v-on:focus="focusIn" />
    <span class="icon is-small is-left">
      <i class="material-icons search-icon">search</i>
    </span>

    <div class="dropdown-menu" id="search-results">
      <div class="dropdown-content">
        <ArtistResults v-bind:query="query" />
        <AlbumResults v-bind:query="query" />
        <TrackResults v-bind:query="query" />
      </div>
    </div>
  </div>
</div>
</template>

<script>
import AlbumResults from './AlbumResults';
import TrackResults from './TrackResults';
import ArtistResults from './ArtistResults';

export default {
  data: () => ({
    query: '',
    hideResults: false
  }),
  components: {
    AlbumResults,
    TrackResults,
    ArtistResults
  },
  computed: {
    shouldShowSearchResults() {
      return this.query !== '' && !this.hideResults;
    }
  },
  methods: {
    async focusOut() {
      await new Promise(resolve => setTimeout(resolve, 300));
      this.hideResults = true;
    },
    async focusIn() {
      await new Promise(resolve => setTimeout(resolve, 300));
      this.hideResults = false;
    }
  }

}
</script>

<style scoped lang="scss">
@import '../../styles.sass';

#search-results {
    left: -5rem;

}
.dropdown-content {
    background-color: darken($content-card-background, 4);
}
input.input,
input.input:hover {
    background-color: $unfocused-control-background;
    color: $unfocused-control-text;
    border-color: $unfocused-control-text;
    transition: 0.2s;
    transition-property: background-color;
}
input.input:focus {
    background-color: white;
    transition: 0.2s;
    transition-property: background-color;
}

.search-icon {
    color: $unfocused-control-text;
}
</style>
