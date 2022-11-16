import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import moviedata from '../movie.json'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: []
  },
  getters: {
  },
  mutations: {
  //   movieDB(state, data){
  //     state.movies= data
  //   }
  },
  actions: {
    // dbInit({commit}){
    //   const res = moviedata
    //   const data = res.map(d=>({
    //     score: d.fields.vote_average,
    //     pk: d.pk,
    //   }))
    //   commit('movieDB', data)
    // }
    // getMovie() {
    //   axios({
    //     method: 'get',
    //     url: './movie.json',
    //   })
    //     .then((res) => {
    //       console.log(res)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
  },
  modules: {
  }
})
