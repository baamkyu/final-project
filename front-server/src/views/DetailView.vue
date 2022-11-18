<template>
  <div id="top-space">
    <h1>Detail</h1>
    <img class="poster" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie?.poster_path}`" alt="영화정보 확인하기">
    <p>제목 : {{ movie?.movie.movieNm }}</p>
    <p>상영 시간 : {{ movie?.movie.showTm }}분</p>
    <p>개봉 년도 : {{ movie?.movie.prdtYear }}년</p>
    <p>감독 : {{ movie?.movie.directors }}</p>
    <p>출연 배우 : {{ movie?.movie.actors }}</p>
    <p>장르 : {{ movie?.movie.genres }}</p>
    <p>청소년 관람 불가 :{{ movie?.adult }}</p>
    <p>평점 : {{ movie?.vote_average }}</p>
    <p>줄거리 :{{ movie?.overview }}</p>
    
    <hr>
    <DetailComment/>
  </div>
</template>

<script>
import axios from 'axios'
import DetailComment from '@/components/DetailComment'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    DetailComment,
  },
  data(){
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios( {
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
        this.getComment()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getComment() {
      console.log(this.movie)
      this.$store.dispatch('getComment', this.movie.id)
    }
  }
}
</script>

<style>
#top-space {
  padding-top: 60px;
}
</style>