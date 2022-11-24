<template>
  <div id="top-space">
    <div class="center-item">
      <div class="detail-border">
        <h1 class="font-twayair">{{ movie?.movie?.movieNm }}</h1>
        <div class="detail-div">
          <div>
            <img class="center-img" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie?.poster_path}`" alt="영화정보 확인하기">
          </div>
          <!-- 10. 보고싶어요 구현하기 -->
          <div>
            <form @submit.prevent="clickWant">
              <input v-if="!alreadyWant" type="submit" class="detail-div-heart" title="찜하기!" value="♡">
              <input v-else type="submit" class="detail-div-heart" title="찜목록에서 삭제" value="♥">
            </form>
          </div>
        </div>
      
      <!-- 영화 정보 -->
        <div class="detailview-font">
          <p>제목 : {{ movie?.movie.movieNm }}</p>
          <p>상영 시간 : {{ movie?.movie.showTm }}분</p>
          <p>개봉 년도 : {{ movie?.movie.prdtYear }}년</p>
          <p>감독 : <span v-for="(director, idx) in movie?.movie.directors" :key="idx">{{director}} </span></p>
          <p>출연 배우 : <span v-for="(actor, idx) in movie?.movie.actors" :key="idx">{{actor}} </span></p>
          <p>장르 : <span v-for="(genre, idx) in movie?.movie.genres" :key="idx">{{genre}} </span></p>
          <p>평점 : {{ movie?.vote_average }}</p>
          <p>줄거리 : {{ movie?.overview }}</p>
        </div>
      </div>
    </div>
    <br>
    <br>
    
    <SimilarMovieList :movie-pk="moviePK"/>
    <CreateComment :movie-pk="moviePK"/>
    <DetailComment/>
  </div>
  
</template>

<script>
import axios from 'axios'
import DetailComment from '@/components/DetailComment'
import CreateComment from '@/components/CreateComment'
import SimilarMovieList from '@/components/SimilarMovieList'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    DetailComment,
    CreateComment,
    SimilarMovieList,
  },
  data(){
    return {
      movie: null,
      moviePK: null,
      directors: [],
      alreadyWant: Number,
    }
  },
  created() {
    this.getMovieDetail()
    this.getComment()
    // 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)
    this.checkWant()
  },
  methods: {
    getMovieDetail() {
      axios( {
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
      .then((res) => {
        this.movie = res.data
        this.moviePK = this.movie.id
        // this.directors = this.movie.movie.genres
      })
      .catch((err) => {
        this.$router.push('/404')
        console.log(err)
      })
    },
    getComment() {
      this.$store.dispatch('getComment', this.$route.params.id)
    },
    // 10. 보고싶어요 구현하기 - 클릭시 보고 싶어요 상태 변경하기
    clickWant() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/wants/`,
        headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
      })
        .then(() => {
          this.alreadyWant = !this.alreadyWant
        })
        .catch((err) => console.log(err))
    },
    // 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)
    checkWant() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/wants/`,
        headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
      })
        .then((res) => {
          this.alreadyWant = res.data.wantlist.includes(this.$store.state.userPK)
        })
        .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
@font-face {
    font-family: 'twayair';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_tway@1.0/twayair.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

.font-twayair{
  font-family: 'twayair'
}

.detailview-font{
  font-family: 'twayair';
}
#top-space {
  padding-top: 75px;
}

.center-item {  
  text-align: center;
  margin-left: 25%;
  margin-right: 25%;
}

.center-item {  
  text-align: center;
}

.detail-div {
  display: flex;
  /* position: relative; */
  justify-content: center;
  padding: 20px;
  margin-left: 25%;
  margin-right: 25%;
}

.absolute-box{
  /* position: absolute;
  left: 37%; */
  
}
.detail-div-heart{
  /* bottom: 0px; */
  color: red;
  background: none;
  /* position: fixed; */
  /* height: 45px;
  width: 45px; */
  border: none;
  font-size: 30px;
}

.detail-border {
  border: 2px groove white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: inset 0 0 20px red;
}

p {
  word-break: keep-all;
}
</style>