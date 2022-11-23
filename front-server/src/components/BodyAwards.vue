<template>
  <div>    
    <!-- <h3 class="CategoryHeader">{{pickFestival}} 수상작</h3> -->
    <span class="CategoryHeader span-to-h3">{{festival_name}} 수상작</span>
    <select class="selectbox" @change="getAwardMovies($event)">
      <option value="0">선택</option>
      <option value="아카데미">아카데미 영화제</option>
      <option value="칸 영화제">칸 영화제</option>
      <option value="베를린 영화제">베를린 영화제</option>
    </select>
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
    <hr>
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
      AwardMovieList: Array,
      festival_name: '',
      values: [],
      options: [],
      swiperOption: {
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
          },
          autoplay: {
            delay : 3000,   // 시간 설정
            disableOnInteraction : false,  // false로 설정하면 스와이프 후 자동 재생이 비활성화 되지 않음
          },
          // centeredSlides : true,
          breakpoints: {
            640: {
              slidesPerView: 2,
              spaceBetween: 10,
            },
            940: {
              slidesPerView: 3,
              spaceBetween: 10,
            },
            1240: {
              slidesPerView: 4,
              spaceBetween: 10,
            },
            1560: {
              slidesPerView: 5,
              spaceBetween: 10,
            }
        },
      },
    }
  },
  created() {
    this.getAwardRandomMovies()
  },
  methods: {
    getAwardMovies(event) {
      const API_URL = 'http://127.0.0.1:8000'
      const pickFestival = event.target.value
      // const festival = ['아카데미', '칸 영화제', '베를린 영화제']
      // const pickFestival = _.sampleSize(festival, 1)[0]
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/award/movie/${pickFestival}/`,
      })
        .then((res) => {
          this.AwardMovieList = res.data
          console.log(res.data[0].festival_name)
          this.festival_name = res.data[0].festival_name
          }) 
        .catch((err) => {
          console.log(err)
          })
    },
    getAwardRandomMovies(){
      const API_URL = 'http://127.0.0.1:8000'
      // const pickFestival = event.target.value
      const festival = ['아카데미', '칸 영화제', '베를린 영화제']
      const pickFestival = _.sampleSize(festival, 1)[0]
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/award/movie/${pickFestival}/`,
      })
        .then((res) => {
          this.AwardMovieList = res.data
          // console.log(res.data[0].festival_name)
          this.festival_name = res.data[0].festival_name
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
.span-to-h3{
  font-size: calc(1.3rem + 0.6vw);
  font-weight: 500;
  line-height: 1.2;
  padding-right: 50px;
}

.selectbox{
  padding: 2px;
  width: 145px;
  border: 1px solid white;
  border-radius: 3px;
  text-align: center;
  background-color: #1C1D1F;
  color: white;
  position: relative;
}
</style>