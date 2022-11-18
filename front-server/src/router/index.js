import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import RecommendView from '@/views/RecommendView'
import WantToSeeView from '@/views/WantToSeeView'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'
import DetailView from '@/views/DetailView'
import NotFound404 from '@/views/NotFound404View'
import store from '../store/index.js'

Vue.use(VueRouter)

const requireAuth = () => (from, to, next) => {
  const token = localStorage.getItem('token')
  // 로그인 되어있으면 next로 이동
  if (token) {
    store.state.isLogin = true
    return next()
  } // 로그인 안 되어있으면 로그인 페이지로 이동
  next('/login')
}

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
    beforeEnter: requireAuth()
  },
  {
    path: '/wanttosee',
    name: 'WantToSeeView',
    component: WantToSeeView,
    beforeEnter: requireAuth()
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
    // beforeEnter(to, from, next) {
    //     if( isLoggedIn === true) {
    //         console.log('이미 로그인 되어있음!')
    //         next({ name: 'HomeView' })
    //       } else{ 
    //           next()
    //         }
    //       }
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/movies/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
