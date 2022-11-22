<template>
  <div>    
    <h3 class="CategoryHeader">비슷한 작품</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="movie in SimilarMovieList"
        :key="movie.id">
        <SimilarMovieItem :movie="movie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import SimilarMovieItem from '@/components/SimilarMovieItem'
import axios from 'axios'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import "swiper/css/swiper.css"

export default {
  name: 'SimilarMovieList',
  components: {
    SimilarMovieItem,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      swiperOption: {
          // 한 페이지에 몇개?
          slidesPerView: 5,
          // 객체 간에 사이 간격
          spaceBetween: 10,
          // 1~10 -> 1~10 반복할거임?
          loop: true,
          pagination: {
            el: '.swiper-pagination',
            // 밑에 점 클릭해서 이동 가능?
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
      SimilarMovieList: Array
    }
  },
  created() {
    this.getSimilarMovies()
  },
  methods: {
    getSimilarMovies() {
      const API_URL = `https://api.themoviedb.org/3/movie/${this.$route.params.id}/similar`
      const API_KEY = 'bd7f98121a9d0436318b3160e3374695'
      axios({
        method: 'get',
        url: `${API_URL}?api_key=${API_KEY}&language=ko-KR&page=1`,
        params: {
          key: API_KEY,
        }
      })
        .then((res) => {
          console.log(res.data.results)
          this.SimilarMovieList = res.data.results
          }) 
        .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
/* h3 {
  font-family: 'GangwonEduPowerExtraBoldA';
} */

@font-face {
    font-family: 'GangwonEduPowerExtraBoldA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEduPowerExtraBoldA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* .moviebox{
  border:30px red;
  
} */
.swiper {
  height: 600px;
  width: 100%;
}
.swiper-item{
  width: 20%;
}
.swiper-slide {
  height: 600px;
  /* width: 100%;  */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: bold;
}
</style>