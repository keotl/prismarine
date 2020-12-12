<template>
  <div class="tabs is-centered" style="margin-bottom: 0">
    <ul>
      <li v-bind:class="{'is-active' : isAlbum }">
        <a v-on:click="setViewCategory('album')">Albums</a>
      </li>
      <li v-bind:class="{'is-active' : isArtist }">
        <a v-on:click="setViewCategory('artist')">Artists</a>
      </li>
<!--      <li v-bind:class="{'is-active' : isTrack }">
        <a v-on:click="setViewCategory('track')">Tracks</a>
      </li> -->
    </ul>
  </div>
</template>

<script>
export default {
  props: ["viewCategory", "setViewCategory"],
  computed: {
    isAlbum() {
      return this.viewCategory === "album";
    },
    isArtist() {
      return this.viewCategory === "artist";
    },
    isTrack() {
      return this.viewCategory === "track";
    }
  }
};
</script>

<style scoped lang="scss">
@import "../../styles.sass";
.tabs {
  background-color: $content-card-background;
}
.tabs li.is-active a {
  color: $accent-secondary;
  border-bottom-color: $accent-secondary;
}
.tabs a {
  color: $text-light;
  border-bottom-color: $text-light;
  transition: 0.2s;
  transition-property: color, border-bottom-color;
}
.tabs a:hover {
  color: $text;
  border-bottom-color: $text;
  transition: 0.2s;
  transition-property: color, border-bottom-color;
}
.tabs ul {
  border-bottom-color: $text-light;
}
</style>

