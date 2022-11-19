import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

import _ from 'lodash'
import router from '@/router'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    randomMovies: [],
    token: null,
    username: null,
    comments: [],
    allcomments: [],
    isLogin: null,
    // dddddddddddddddddddd
    userPK: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    allCommentsCount(state) {
      return state.allcomments.length
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      const randomMovies = _.sampleSize(state.movies, 10)
      state.randomMovies = randomMovies
    },
    // 로그인 되면 Home으로 이동(token값이 생기면)
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'HomeView'})
    },
    SAVE_USER(state, username) {
      state.username = username
    },
    // 로그아웃 되면 Home으로 이동(token값이 null이 되면)
    NULL_TOKEN(state) {
      state.token = null
      state.username = null
      router.push({name: 'HomeView'})
    },
    GET_COMMENT(state, comments) {
      state.comments = comments
    },
    COMMENT_COUNT(state, comments) {
      state.allcomments = comments
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {  
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
          // username님 환영합니다 하기 위해 USER_NAME을 따로 받아줌
          context.commit('SAVE_USER', username)
        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      // dddddddddddddddddddddddd
      const userPK = payload.id
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
          // username님 환영합니다 하기 위해 USER_NAME을 따로 받아줌
          context.commit('SAVE_USER', username)
        })
        .catch(err => console.log(err))
    },
    getComment(context, movie_pk) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_pk}/comments/`
      })
          .then((res) => {
            context.commit('GET_COMMENT', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    commentCount(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/comments/`,
      })
        .then((res) => {
          context.commit('COMMENT_COUNT', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
