<template>
  <div>
    <p>{{randomMovie.movie.nations}}</p>
    <p>{{randomMovie.movie.movieNm}}</p>
    <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`">

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

</style>