<template>
    <div class="MovieCard">
      <!-- 포스터 사진 -->
      <img class="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie?.poster_path}`">
      <!-- 영화 제목 -->
      <div class="movieInfo-title">{{movie?.titel}}</div>
      <!-- 개봉년도, 개봉국가 -->
      <div class="movieInfo">
        {{movie?.release_date}}
      </div>
      <div class="movieInfo">
        평점 : {{movie?.vote_average}}
      </div>
      <!-- 영화정보 더보기 (DetailView) -->
      <a :href='`https://www.themoviedb.org/movie/${movie?.id}`' class="movieInfo">[영화정보 더보기]</a>
      <hr>
    </div>
</template>

<script>
export default {
  name: 'AwardsItem',
  props: {
    movie: Object
  }
}
</script>

<style>
.movieInfo-title{
  color: lightgray;
  font-size: 16px;
}
.movieInfo {
  color: lightgray;
  font-size: 14px;
}
</style>