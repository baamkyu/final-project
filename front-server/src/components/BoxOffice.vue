<template>
  <div>
    <h3 class="CategoryHeader">박스오피스 순위</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="movie in BoxOfficeList"
        :key="movie.rank">
        <BoxOfficeItem :movie="movie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev background-none" slot="button-prev"></div>
      <div class="swiper-button-next background-none" slot="button-next"></div> 
    </swiper>
  </div>
</template>

<script>
import BoxOfficeItem from '@/components/BoxOfficeItem'
import axios from 'axios'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import "swiper/css/swiper.css"

export default {
  name: 'RealBoxOffice',
  components: {
    BoxOfficeItem,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
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
      BoxOfficeList: Array,
    }
  },
  created() {
    this.getBoxoffic()
  },
  // 13. 실시간 박스오피스 정보 가져오기
  methods: {
    getBoxoffic() {
      const API_URL = 'https://api.themoviedb.org/3/movie/now_playing'
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
          this.BoxOfficeList = res.data.results
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
@font-face {
    font-family: 'GangwonEdu_OTFBoldA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEdu_OTFBoldA.woff') format('woff');
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
.swiper-slide {
  height: 600px;
  /* width: 100%;  */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: bold;
}

.swiper-pagination-bullet {
  background-color: white !important;
}

</style>