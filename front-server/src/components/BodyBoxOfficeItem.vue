<template>
  <li class="MovieCard">
    <!-- 포스터 사진 -->
    <img class="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie?.poster_path}`" @click="goMovieDetail">
    <!-- 영화 제목 -->
    <div class="css-title movieInfo">{{randomMovie?.movie?.movieNm}}</div>
    <!-- 개봉년도, 개봉국가 -->
    <div class="movieInfo">
      {{randomMovie?.movie?.prdtYear}} ·
      {{randomMovie?.movie?.nations}}
    </div>
    <!-- 영화정보 더보기 (DetailView) -->
    <router-link :to="{ 
      name: 'DetailView',
      params: { id: randomMovie?.id } }" class="movieInfo">
      영화정보 더보기
      </router-link>
    <hr>
  </li>
  
</template>

<script>

export default {
  name: 'BoxOfficeItem',
  props: {
    randomMovie: Object,
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
#poster {
  display: flex;
  /* flex-direction: row; */
  position: relative;
  overflow: hidden;
  top: 0;
  left: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  border: 1px solid #eae9e8;
  border-radius: 5px;
  background: #f8f8f8;
  -webkit-transition: 300ms;
  transition: 300ms;
}
/* CSS grid */
li {
  display: inline-block;
  vertical-align: top;
  /* box-sizing: border-box; */
  /* width: 33.333333333333336%; */
  padding: 0 5px;
  margin: 0 0 24px; 
}


.poster {
  vertical-align: top;
  width: 200px;
  /* height: 100%; */
  opacity: 1;
  object-fit: cover;
  transition: opacity 420ms;
  cursor: pointer;
}

.css-title {
    color: #292a32;
    font-size: 15px;
    font-weight: 400;
}

.movieInfo {
  color: white;
}
.MovieCard {
  border: 2px red;
}

/* 화면 뒤집기 하려고 했는데 실패함
.hidden { display: none; }
.trigger:hover + .hidden { display: inline; } */
</style>