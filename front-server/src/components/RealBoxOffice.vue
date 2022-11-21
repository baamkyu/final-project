<template>
  <div>
    <h3 class="CategoryHeader">ㄹㅇ박스오피스 순위</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="movie in BoxOfficeList"
        :key="movie.rank">
        <RealBoxOfficeItem :movie="movie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import RealBoxOfficeItem from '@/components/RealBoxOfficeItem'
import axios from 'axios'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import "swiper/css/swiper.css"

export default {
  name: 'RealBoxOffice',
  components: {
    RealBoxOfficeItem,
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
      BoxOfficeList: Array,
    }
  },
  created() {
    this.getBoxoffic()
  },
  // 13. 실시간 박스오피스 정보 가져오기
  methods: {
    getBoxoffic() {
      // http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=f5eef3421c602c6cb7ea224104795888&movieCd=20124079
      const API_URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
      const API_KEY = 'f5eef3421c602c6cb7ea224104795888'
      // const API_KEY = 'a222b6703b63955f330a30797f941c12'
      let date = new Date()
      let year = date.getFullYear()
      let month = date.getMonth()+1
      let day = date.getDate()-1

      if(month < 10){
        month = '0' + month
      }
      if(day < 10){
        day = '0' + day
      }
      let YESTERDAY = year + "" + month + "" + day 
      // console.log(YESTERDAY)
      // console.log(typeof(YESTERDAY))
      // console.log(`${API_URL}key=${API_KEY}&targetDt=${YESTERDAY}`)

      // 13-1. 진흥원 api에서 박스오피스 리스트 받아오기
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          targetDt: YESTERDAY,
        }
      })
        .then((res) => {
          this.BoxOfficeList = res.data.boxOfficeResult.weeklyBoxOfficeList
          // 13-2. 진흥원 api에서 박스오피스 영화별 상세정보 받아오기
          const detailMoviesInfos = this.BoxOfficeList
          for (const detailMovieInfo of detailMoviesInfos) {
            const movieCd = detailMovieInfo.movieCd
            const detail_movie_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
            axios({
              method: 'get',
              url: detail_movie_url,
              params: {
                key: API_KEY,
                movieCd: movieCd,
              }
            })
              .then((res) => {
                console.log(res)
                // const detailobject = res.data.movieInfoResult.movieInfo
                // const movieNm = detailobject.movieNm
                // const movieNmEn = detailobject.movieNmEn
                // const showTm = detailobject.showTm
                // const prtdYear = detailobject.prtdYear
                // const directors= detailobject.directors
                // const actors = detailobject.actors
                // const nations = detailobject.nations
                // const genres = detailobject.genres
              })
              .catch((err) => console.log(err))
          }
        }
        )
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