<template>
<div id="app" v-on:mousedown="mouseDown" v-on:mouseup="mouseUp" v-on:mousemove="mouseMove">
  <div>
    <Navbar />
  </div>
  <router-view tag="div" style="flex: 1; min-height:0; -webkit-overflow-scrolling: touch;"></router-view>
  <player/>

</div>
</template>

<script>
import Navbar from './components/Navbar';
import {
  MouseEventBus
} from './mouse-event-bus';

export default {
  name: 'app',
  components: {
    Navbar
  },
  methods: {
    mouseDown() {
      MouseEventBus.$emit("mouse-down");
    },
    mouseUp() {
      MouseEventBus.$emit("mouse-up");
    },
    mouseMove(event) {
      MouseEventBus.$emit("mouse-move", event);
    }
  }
}
</script>

<style lang="scss">
@import './styles.sass';
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: $text;
    display: flex;
    height: 100vh;
    flex-direction: column;
    background-color: $background;
    overflow-x: hidden;
}
html {
    overflow: hidden;
}

// vue-custom-scrollbar configuration
.ps__thumb-y {
  background-color: $text !important;
}
.ps__rail-y:hover {
  background-color: $text-light !important;
}
</style>
