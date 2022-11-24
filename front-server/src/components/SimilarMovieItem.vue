<template>
  <div>
    <div>
      <!-- 포스터 사진 -->
      <img class="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie?.poster_path}`">
      <!-- 영화 제목 -->
      <div class="css-title movieInfo">{{movie?.title}}</div>
      <!-- 개봉년도, 개봉국가 -->
      <div class="movieInfo">
        {{movie?.release_date}}
      </div>
      <div class="movieInfo">
        평점 : {{movie?.vote_average}}
      </div>
      <!-- 영화정보 더보기 (DetailView) -->
      <router-link :to="{ 
        name: 'DetailView',
        params: { id: movie?.movieCd } }" class="movieInfo">
        [영화정보 더보기]
      </router-link>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SimilarMovieItem',
  props: {
    movie: Object
  }
}
</script>

<style>
</style>