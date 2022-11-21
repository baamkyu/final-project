<template>
  <li class="trigger">
    <img class="poster" loading="lazy"
    :lowsrc="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`"
    :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`" @click="goMovieDetail"
    decoding="async">
    <div class="css-title">{{randomMovie.movie.movieNm}}</div>
    <div>
      {{randomMovie.movie.prdtYear}} ·
      {{randomMovie.movie.nations[0]}}

    </div>
    <!-- 영화정보 더보기 (DetailView) -->
    <router-link :to="{ 
      name: 'DetailView',
      params: { id: randomMovie?.id } }" class="movieInfo">
      [영화정보 더보기]
      </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'BoxOfficeItem',
  props: {
    randomMovie: Object,
  },
  components:{
  },
  // methods 제거해도 되는건지 확인 필요
  methods:{
    goMovieDetail() {
      this.$router.push({ name:'DetailView', params: { id: this.randomMovie?.id } })
    }
  }
}
</script>

<style>
.css-title {
    color: #292a32;
    font-size: 15px;
    font-weight: 400;
}
.movieInfo {
  color: white;
}
</style>