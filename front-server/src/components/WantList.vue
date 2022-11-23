<template>
  <div class="wantlist-container">
    <div class="wantlist-item"
        v-for="movie in wantmovies"
        :key="movie.id">
        <WantListItem :movie="movie"/></div>
  </div>
</template>

<script> 
import WantListItem from '@/components/WantListItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'WantList',
  components: {
    WantListItem,
  },
  data() {
    return {
      wantmovies: Array
    }
  },
  created() {
    this.getWantList()
  },
  methods: {
    getWantList() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/${this.$route.params.username}/`,
      })
        .then((res) => {
          this.wantmovies = res.data.wantmovies
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
  .wantlist-container{
    display: grid;
    justify-content: center;
    grid-template-columns: 298px 298px 298px;
    grid-gap: 3px;
    /* padding: 10px; */
    color: black;
    /* background-color: #f54; */
  }
  .wantlist-item{
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    background-color: #1C1D1F;
  }
</style>