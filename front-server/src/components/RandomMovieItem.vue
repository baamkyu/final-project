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
      <div class="css-title movieInfo">{{randomMovie?.movie?.movieNm}}</div>
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
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'BoxOfficeItem',
  props: {
    randomMovie: Object,
  },
  data(){
    return {
      // alreadyWant: Number,
    }
  },
  // methods 제거해도 되는건지 확인 필요
  methods:{
    goMovieDetail() {
      this.$router.push({ name:'DetailView', params: { id: this.randomMovie?.id } })
    },

    // // 10. 보고싶어요 구현하기 - 클릭시 보고 싶어요 상태 변경하기
    // clickWant() {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/api/v1/movies/${this.$route.params.id}/wants/`,
    //     headers: {
    //                 Authorization: `Token ${this.$store.state.token}`
    //             }
    //   })
    //     .then(() => {
    //       this.alreadyWant = !this.alreadyWant
    //     })
    //     .catch((err) => console.log(err))
    // },
    // // 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)
    // checkWant() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/${this.$route.params.id}/wants/`,
    //     headers: {
    //                 Authorization: `Token ${this.$store.state.token}`
    //             }
    //   })
    //     .then((res) => {
    //       this.alreadyWant = res.data.wantlist.includes(this.$store.state.userPK)
    //     })
    //     .catch((err) => console.log(err))
    //   }
    }
  }
</script>

<style>
.css-title {
    color: #292a32;
    font-size: 15px;
    font-weight: 400;
}
.movieInfo {
  color: white;
}

</style>