<template>
  <div>
    <!-- 포스터 사진 -->
    <div>
      <img class="poster" loading="lazy"
        :lowsrc="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`"
        :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${randomMovie.poster_path}`" @click="goMovieDetail">
      <!-- <div>
        <form @submit.prevent="clickWant">
          <input v-if="!alreadyWant" type="submit" class="detail-div-heart" title="찜하기!" value="♡">
          <input v-else type="submit" class="detail-div-heart" title="찜목록에서 삭제" value="♥">
        </form>
      </div> -->
      <!-- 영화 제목 -->
      <div class="movieInfo-title">{{randomMovie?.movie?.movieNm}}</div>
      <!-- 개봉년도, 개봉국가 -->
      <div class="movieInfo">
        {{randomMovie?.movie?.prdtYear}} ·
        {{randomMovie?.movie?.nations[0]}}
      </div>
      <!-- 영화정보 더보기 (DetailView) -->
      <router-link :to="{ 
          name: 'DetailView',
          params: { id: randomMovie?.id } }" class="movieInfo">
          [영화정보 더보기]
      </router-link>
      <hr>
    </div>
  </div>  
</template>

<script>
export default {
  name: 'RandomMovieItem',
  props: {
    randomMovie: Object,
  },
  data(){
    return {
    }
  },
  // methods 제거해도 되는건지 확인 필요
  methods:{
    goMovieDetail() {
      this.$router.push({ name:'DetailView', params: { id: this.randomMovie?.id } })
    },
    }
  }
</script>

<style>
.css-title {
    color: #292a32;
    font-size: 15px;
    font-weight: 400;
}

</style>