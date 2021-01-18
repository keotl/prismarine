<template>
<div style="display: flex; align-items: center;">

  <div class="speaker-button" v-on:click="toggleMute">
    <i class="material-icons">
      {{ speakerIconName }}
    </i>
  </div>
  <div class="clickbox" v-on:mousedown="startSeeking" v-on:click="seek" v-on:wheel="scroll">
  <div class="volume-slider" >
    <div class="volume-highlight" v-bind:style="{width: volumePercentage}" ref="slider" v-on:mousedown="startSeeking" v-on:click="seek"/>
    <div>
      <div class="volume-pin" />
    </div>
    </div>
  </div>


</div>
</template>

<script>
import {
  MouseEventBus
} from '../../mouse-event-bus';

export default {
  data: () => ({
    volume: 1,
    isSeeking: false,
    previousVolume: 1,
    isMuted: false,
  }),
  mounted() {
    const volume = window.localStorage.getItem('volume');
    if (volume) {
        const parsed = parseFloat(volume);
	if (!isNaN(parsed)) {
	    this.volume = parsed;
        }
    }
  },
  methods: {
    handleMouseMove(event) {
      if (this.isSeeking && MouseEventBus.isMouseDown()) {
        this.seek(event);

      } else {
        this.isSeeking = false;
      }
    },
    startSeeking() {
      this.isSeeking = true;
    },
    stopSeeking() {
      this.isSeeking = false;
    },
    seek(event) {
      this.volume = (event.pageX - this.$refs.slider.offsetLeft) / 60;
      if (this.volume < 0) {
        this.volume = 0;
      }
      if (this.volume > 1) {
        this.volume = 1;
      }
      window.localStorage.setItem('volume', this.volume);
    },
    scroll(event) {
      if (event.deltaY < 0 || event.deltaX > 0) {
        this.volume = Math.min(Math.round((this.volume + 0.02) * 100) / 100, 100)
      } else if (event.deltaY > 0 || event.deltaX < 0) {
        this.volume = Math.max(Math.round((this.volume - 0.02) * 100) / 100, 0)
      }
      window.localStorage.setItem('volume', this.volume);
    },
    toggleMute() {
      if (!this.isMuted) {
        this.previousVolume = this.volume;
        this.volume = 0;
        this.isMuted = true;
      } else {
        this.volume = this.previousVolume;
        this.isMuted = false;
      }
      window.localStorage.setItem('volume', this.volume);
    }
  },
  computed: {
    volumePercentage() {
      return this.volume * 80 + '%';
    },
    speakerIconName() {
      if (this.volume === 0) {
        return 'volume_mute';
      }
      if (this.volume > 0.7) {
        return 'volume_up';
      }
      return 'volume_down';
    }
  },
  watch: {
    volume(newVal) {
      this.$emit('volume', newVal);
    }
  },
  created() {
    MouseEventBus.$on('mouse-move', event => this.handleMouseMove(event));
  }

}
</script>

<style scoped lang="scss">
@import '../../styles.sass';
.volume-slider {
    margin-top: auto;
    margin-bottom: auto;
    height: 2px;
    width: 60px;
    background-color: $text-light;
    display: flex;
    flex-direction: row;
    align-items: center;
    transition-property: background-color;
    transition-duration: 0.2s
}
.clickbox {
    padding-top: 10px;
    padding-bottom: 10px;
    cursor: pointer;
}
.clickbox:hover .volume-slider {
  background-color: lighten($text-light, 10);
}

.volume-highlight {
    height: 2px;
    background-color: $accent;
}
.volume-pin {
    height: 12px;
    width: 12px;
    background-color: $accent-secondary;
    border-radius: 50%;
    cursor: pointer;
}
.speaker-button {
    margin-top: 6px;
    margin-right: 1rem;
    transition-duration: 0.2s;
    transition-property: color;
}
.speaker-button:hover {
    color: $text;
    transition-duration: 0.2s;
    transition-property: color;
    cursor: pointer;
}
</style>
