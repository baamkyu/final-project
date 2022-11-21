<template>
  <div>
    <p>----------------------------</p>
    <p>----------------------------</p>
    <p>----------------------------</p>
    <p>----------------------------</p>
    <p>----------------------------</p>  

    <!-- # 11. 유저간 팔로우 구현 -->
    <h3><b>{{this.$route.params.username}}</b> 님의 프로필</h3>
    <span>팔로우 : {{followCnt}} | 팔로잉 : {{followingCnt}}</span>
    <form v-if="!isSameUser" @submit.prevent="clickFollow">
      <span>
        <input v-if="alreadyFollow" type="submit" value="언팔로우">
        <input v-else type="submit" value="팔로우">
      </span>
    </form>

    <p>보고 싶어요</p> 
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyPageView',
  data() {
    return {
      followCnt: Number,
      followingCnt: Number,
      alreadyFollow: 0,
      isSameUser: this.$route.params.username === this.$store.state.username ? true : false
    }
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to)
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/${to.params.username}/`,
        headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
      })
        .then((res) => {
          this.followCnt = res.data.followings.length
          this.followingCnt  = res.data.followers.length
          this.isSameUser = 1
          this.alreadyFollow = 0
        })
        .catch((err) => 
          console.log(err)
        )
    next()
  },
  created() {
    this.countFollow()
  },
  methods: {
    clickFollow() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/user/${this.$route.params.username}/`,
        headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
      })
        .then((res) => {
          this.followCnt = res.data.followings.length
          this.followingCnt  = res.data.followers.length
          this.alreadyFollow = res.data.followers.includes(this.$store.state.username)
        })
        .catch((err) => 
          console.log(err)
        )
    },
    countFollow() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/${this.$route.params.username}/`,
        headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
      })
        .then((res) => {
          this.followCnt = res.data.followings.length
          this.followingCnt  = res.data.followers.length
          this.alreadyFollow = res.data.followers.includes(this.$store.state.username)
        })
        .catch((err) => 
          console.log(err)
        )
    },
  }
}
</script>

<style>

</style>