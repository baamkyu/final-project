<template>
  <div id="top-space">
    <div class="center-item">
      <span class="material-symbols-outlined account_circle">account_circle</span>

      <!-- # 11. 유저간 팔로우 구현 -->
      <h3><b>{{this.$route.params.username}}</b> 님의 프로필</h3>
      <span>팔로잉 : {{followCnt}} | 팔로워 : {{followingCnt}}</span>
      <br>
      <br>
      <!-- 본인 프로필이 아니면 팔로우, 언팔로우 기능 뜨게 하기 -->
      <form v-if="!isSameUser" @submit.prevent="clickFollow">
        <button v-if="alreadyFollow" type="submit" class="follow-button">
          <span class="material-symbols-outlined">person_remove</span>언팔로우
        </button>
        <button v-else type="submit" value="팔로우" class="follow-button"> 
          <span class="material-symbols-outlined">person_add</span>팔로우
        </button>
      </form>
    
      <br>
      <p>보고 싶어요</p> 
      <WantList/>
    </div>
  </div>
</template>

<script>
import WantList from '@/components/WantList'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyPageView',
  components: {
    WantList
  },
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

.follow-button{
  background-color: rgb(28,29,31);
  color: white;
  border: solid 1px white;
  border-radius: 12px;
}

.account_circle{
  font-size: 200px !important;
}
</style>