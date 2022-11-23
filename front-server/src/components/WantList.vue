<template>
  <div>
    <WantListItem
      v-for="movie in wantmovies"
      :key="movie.id"
      :movie="movie"
    />
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

</style>