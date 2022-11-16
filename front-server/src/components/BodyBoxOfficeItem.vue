<template>
  <div>
    <img id="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`">
    <p>{{randomMovie.movie.movieNm}}</p>
    <p>{{randomMovie.movie.nations}}</p>
    <hr>

  </div>
</template>

<script>
export default {
  name: 'BoxOfficeItem',
  props: {
    randomMovie: Object,
  },
  // data() {
  //   return {
  //     url: String,
  //   }
  // },
  // computed: {
  //   makeUrl() {
  //     this.url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/'+
  //   }
  // }
}
</script>

<style>
/* CSS grid */
</style>