<template>
<div class="view-container">
  <view-options-menu v-bind:viewCategory="viewCategory" v-bind:setViewCategory="setViewCategory" />
  <div class="dashboard-container">
      <artist-dashboard v-if="viewCategory === 'artist'" />
      <album-dashboard v-if="viewCategory === 'album'" />
  </div>
</div>
</template>

<script>
import ViewOptionsMenu from "./ViewOptionsMenu";

import AlbumDashboard from "./AlbumDashboard";

import ArtistDashboard from "./ArtistDashboard";


export default {
  data: () => ({
    viewCategory: "album"
  }),
  components: {
    ViewOptionsMenu,
    ArtistDashboard,
    AlbumDashboard
  },
  methods: {
    setViewCategory(viewCategory) {
      this.viewCategory = viewCategory;
    }
  }
};
</script>

<style scoped>
.view-container {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
}

.dashboard-container {
  display: flex;
  flex: 1;
  overflow-y: hidden;
}
.dashboard-container > * {
  padding-top: 2rem;
}
</style>
