import Vue from 'vue'
import VueRouter from 'vue-router'
import Bulma from 'bulma'
import App from './App.vue'
import Artist from './components/Artist'
import Album from './components/Album'
import Track from './components/Track'
import Home from './components/dashboard/Home'
import Player from './components/Player'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(Bulma)

const router = new VueRouter({
  routes: [{
      path: "/artist/:id",
      component: Artist,
      name: "Artist"
    },
    {
      path: "/",
      component: Home,
      name: "Home"
    },
    {
      path: "/album/:id",
      component: Album,
      name: "Album"
    },
    {
      path: "/track/:id",
      component: Track,
      name: "Track"
    }
  ]
})

Vue.component('player', Player);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
