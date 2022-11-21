<template>
  <div class="MovieCard">
    <!-- 포스터 사진 -->
    <p>포스터 사진</p>
    <!-- <img class="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie?.poster_path}`"> -->
    <!-- 영화 제목 -->
    <div class="css-title movieInfo">{{movie?.movieNm}}</div>
    <!-- 개봉년도, 개봉국가 -->
    <div class="movieInfo">
      {{movie?.openDt}} · 개봉국가
    </div>
    <div class="movieInfo">
      누적관객 {{movie?.audiAcc}} 명
    </div>
    <!-- 영화정보 더보기 (DetailView) -->
    <p>Detail</p>
    <router-link :to="{ 
      name: 'DetailView',
      params: { id: movie?.movieCd } }" class="movieInfo">
      [영화정보 더보기]
      </router-link>
    <hr>
  </div>
  
</template>

<script>
export default {
  name: 'RealBoxOfficeItem',
  props: {
    movie: Object,
  },
  components:{
  },
  // methods 제거해도 되는건지 확인 필요
  methods:{
    // goMovieDetail() {
    //   this.$router.push({ name:'DetailView', params: { id: this.randomMovie?.id } })
    // }
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