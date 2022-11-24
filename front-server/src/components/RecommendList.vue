<template>
  <div>
    <div class="recommend-form">
      <div class="recommend-header">맞춤 영화 찾기</div>
      <div class="recommend-div">
        <!-- `genre-${num}` -->
        <div class="recommend-select-header font-twayair">장르 선택</div>
          <span v-for="(genre,num) in genres" :key="`genre-${num}`">
            <button v-if="selectedGenre === num" @click="clickGenre(null)" class="recommend-button-selected">{{ genre }}</button>
            <button v-else @click="clickGenre(num)" class="recommend-button">{{genre}}</button>
          </span>
        <br>
        <br>
        <div class="recommend-select-header font-twayair">국가 선택</div>
          <span v-for="(nation, num) in nations" :key="`nation-${num}`">
            <button v-if="selectedNation === num" @click="clickNation(null)" class="recommend-button-selected">{{ nation }}</button>
            <button v-else @click="clickNation(num)" class="recommend-button">{{ nation }}</button>
          </span>
        <br>
        <br>
        <div>
            <button @click="submitComment" class="recommend-start-button">영화 보기</button>
        </div>
        </div>
      </div>

    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="movie in RecommendList"
        :key="movie.id">
        <RecommendItem :movie="movie"/>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import RecommendItem from '@/components/RecommendItem'
import axios from 'axios'
// import _ from 'lodash'

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import "swiper/css/swiper.css"

export default {
  name: 'RecommendList',
  components: {
    RecommendItem,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      RecommendList: Array,
      genreNum: null,
      nationNum: null,
      selectedGenre: null,
      selectedNation: null,
      genres: ["SF","가족","공포(호러)","다큐멘터리","드라마","멜로/로맨스","뮤지컬","미스터리","범죄",
      "사극","서부극(웨스턴)","스릴러","애니메이션","액션","어드벤처","장르","전쟁","코미디","판타지"],
      nations: ["해외", "국내"],

      swiperOption: {
          // 1~10 -> 1~10 반복할거임?
          loop: false,
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
  },
  methods: {
    //  선택한 장르 담아놓기
    clickGenre(select) {
      this.selectedGenre = select
      console.log(this.selectedGenre)
    },
    // 선택한 나라 담아놓기
    clickNation(select) {
      this.selectedNation = select
      console.log(this.selectedNation)
    },
    // 안 담겨있음 && 클릭 => 담기, 담겨있음 && 클릭 => 비우기
    // clickBox(num) {
    //   if (this.genre.includes(num)){
        
    //   }
    // },

    // 제출을 누르면 검색
    submitComment() {
      const genre_num = this.selectedGenre
      const nation_num = this.selectedNation
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/recommend/${genre_num}/${nation_num}/`,
      })
        .then((res) => {
          this.RecommendList = res.data
        })
        .catch((err) => console.log(err))
    },
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

.recommend-form{
  margin-left: 25%;
  margin-right: 25%;
  vertical-align: center;
  border: white 1px solid;
  border-radius: 10px;
  box-shadow: inset 0 0 20px red;
}

.recommend-header{
  margin-top: 35px;
  display : flex;
  flex-direction : column;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  font-family: 'TmonMonsori';
}

.recommend-div{
  text-align: center;
  padding-top: 21px;
  padding-right: 53px;
  padding-left: 53px;
  padding-bottom: 21px;
}

.recommend-button{
  background-color: black;
  border: white 1px solid;
  font-family: 'twayair';
  border-radius: 8px;
  color: white;
  padding: 16px;
  margin-top: 16px;
  margin-right: 9px;
  cursor: pointer;
  transition: color 0.3s ease-in-out;
}

.recommend-button:hover{
  background-color: black;
  border: #D9514F solid 1px;
  color: #D9514F;
  opacity: 0.7;
}

.recommend-button-selected{
  background-color: #D9514F;
  border: white 1px solid;
  font-family: 'twayair';
  border-radius: 8px;
  color: white;
  padding: 16px;
  margin-top: 16px;
  margin-right: 9px;
  cursor: pointer;
  transition: color 0.3s ease-in-out;
}
.recommend-button-selected:hover{
  opacity: 0.5;
}


.recommend-start-button{
  font-family: 'twayair';
  background-color: #D9514F;
  font-size: 20px;
}
.recommend-start-button:hover{
  border: white 2px solid;
}

.recommend-select-header{
  font-size: 24px;
  text-align: center;
}

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