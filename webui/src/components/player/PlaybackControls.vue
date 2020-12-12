<template>
<div class="button-container">
  <div v-on:click="$emit('previous')" class="playback-button">
    <i class="material-icons">skip_previous</i>
  </div>
  <div v-if="isPlaying" v-on:click="$emit('pause')" class="playback-button">
    <i class="material-icons">pause</i>
  </div>
  <div v-if="!isPlaying" v-on:click="$emit('play')" class="playback-button">
    <i class="material-icons"> play_arrow </i>
  </div>
  <div v-on:click="$emit('stop')" class="playback-button">
    <i class="material-icons"> stop</i>
  </div>

  <div v-on:click="$emit('next')" class="playback-button">
    <i class="material-icons"> skip_next</i>
  </div>
</div>
</template>

<script>
export default {
  props: ['isPlaying']
}
</script>

<style scoped lang="scss">
@import '../../styles.sass';
.playback-button {
    background-color: $menu-background;
    color: $text-light;
    margin-top: auto;
    margin-bottom: auto;
    padding-top: 4px;
    padding-left: 4px;
    border-radius: 50%;
    height: 32px;
    width: 32px;
    animation-delay: 0.4s;
    transition-duration: 0.4s;
    transition-property: color;
    user-select: none;
    -moz-user-select: none;
}
.playback-button:hover {
    cursor: pointer;
    // box-shadow: 0 0 5px 10px $accent inset;
    color: $text;
    transition-duration: 0.4s;
    transition-property: color;
}

.button-container {
    display: flex;
    flex-direction: row;
    flex: 1;
    justify-content: center;
}
</style>
