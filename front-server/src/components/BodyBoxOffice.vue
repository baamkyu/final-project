<template>
  <div>
    <h3 class="CategoryHeader">박스오피스 순위</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="randomMovie in randomMovies"
        :key="randomMovie.id">
        <BoxOfficeItem :randomMovie="randomMovie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import BoxOfficeItem from '@/components/BodyBoxOfficeItem'
import "swiper/css/swiper.css"

export default {
  name: 'BoxOffice',
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
      }
    }
  },
  computed: {
    randomMovies() {
      return this.$store.state.randomMovies
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
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
  width: 15%;
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