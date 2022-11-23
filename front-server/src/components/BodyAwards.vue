<template>
  <div>    
    <h3 class="CategoryHeader">{{AwardMovieList[0]['festival_name']}} 수상작</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="movie in AwardMovieList"
        :key="movie.id">
        <AwardsItem :movie="movie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import AwardsItem from '@/components/BodyAwardsItem'
import axios from 'axios'
import _ from 'lodash'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import "swiper/css/swiper.css"

export default {
  name: 'AwardsMovie',
  components: {
    AwardsItem,
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
      AwardMovieList: Array
    }
  },
  created() {
    this.getAwardMovies()
  },
  methods: {
    getAwardMovies() {
      const API_URL = 'http://127.0.0.1:8000'
      const festival = ['아카데미', '칸 영화제', '베를린 영화제']
      const pickFestival = _.sampleSize(festival, 1)[0]
      console.log(pickFestival)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/award/movie/${pickFestival}/`,
      })
        .then((res) => {
          this.AwardMovieList = res.data
          }) 
        .catch((err) => {
          console.log(err)
          })
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