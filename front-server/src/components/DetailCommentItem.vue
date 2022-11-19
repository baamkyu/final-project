<template>
  <div>
    <p>{{comment.content}}</p>
    <!-- # 6. 코멘트 좋아요 구현 -->
    <form @submit.prevent="clickLike">
      <label for="likecnt">좋아요 : {{likecnt}}</label>
      <span>
        <input v-if="alreadyLike" type="submit" value="좋아요 취소">
        <input v-else type="submit" value="좋아요">
      </span>
    </form>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "DetailCommentItem",
    props: {
        comment: Object,
    },
    data() {
      return {
        likecnt : this.comment.like_users.length,
        alreadyLike : this.comment.like_users.includes(),
      }
    },
    // 6. 코멘트 좋아요 구현
    methods: {
      clickLike() {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/likes/`,
          headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
        })
          .then((res) => {
            console.log(res)
            this.likecnt = res.data.like_users.length
            this.alreadyLike = !this.alreadyLike
            })
            .catch((err) => 
            console.log(err)
            )
      },
      countLike() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/likes/`,
          headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
        })
          .then((res) => {
            console.log(res)
            this.likecnt = res.data.like_users.length
            this.alreadyLike = !this.alreadyLike
            })
            .catch((err) => 
            console.log(err)
            )
      }
    }
}
</script>

<style>

</style>