import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

import _ from 'lodash'

export default new Vuex.Store({
  state: {
    movies: [],
    randomMovies: []
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      const randomMovies = _.sampleSize(state.movies, 10)
      state.randomMovies = randomMovies
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
  },
  modules: {
  }
})
