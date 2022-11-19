<template>
  <div>
    <p>{{comment.content}}</p>
    <form @submit.prevent="clickLike">
      <label for="likecnt">좋아요 : {{likecnt}}</label>
      <input type="submit">
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
        likecnt : 0,
      }
    },
    methods: {
      clickLike() {    
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/${this.comment.id}/likes/${this.comment.user}`
        })
      }
    }
}
</script>

<style>

</style>