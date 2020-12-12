<template>
<div class="navbar">
  <div class="navbar-brand">
    <div class="navbar-item">
    <router-link to="/" class="navbar-item" tag="div" style="cursor: pointer;">
    Prismarine Player
      </router-link>
    </div>
  </div>
  <div class="navbar-menu">
    <div class="navbar-start">
      <router-link to="/" class="navbar-item" tag="a">
        <i class="material-icons"> home </i>
      </router-link>
    </div>
    <div class="navbar-end">
      <div class="navbar-item">
        <InteractiveSearch/>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import InteractiveSearch from './search/InteractiveSearch';

export default {
  data: () => ({
    searchQuery: '',
  }),
  components: {
    InteractiveSearch,
  },
  methods: {
    clearSearch() {
      this.searchQuery = '';
    },
  }

}
</script>

<style scoped lang="scss">
@import '../styles.sass';
.navbar * {
    background-color: $menu-background;
    color: $text;
}
.navbar * a:hover,
.navbar * a:hover * {
    background-color: $menu-accent-background;
}
.navbar-burger {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
