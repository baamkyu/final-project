import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import RecommendView from '@/views/RecommendView'
import WantToSeeView from '@/views/WantToSeeView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/wanttosee',
    name: 'WantToSeeView',
    component: WantToSeeView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
