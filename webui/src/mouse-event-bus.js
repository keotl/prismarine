import Vue from 'vue';
export const MouseEventBus = new Vue();

let mouseDown = false;
MouseEventBus.$on("mouse-down", () => mouseDown = true);
MouseEventBus.$on("mouse-up", () => mouseDown = false);

MouseEventBus.isMouseDown = function() {
  return mouseDown;
}
