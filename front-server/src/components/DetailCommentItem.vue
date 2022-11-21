<template>
  <div>
    <p>{{comment?.content}}</p>
    <span>작성자 : 
      <router-link
                :to="{ name: 'MyPageView', params: { username: comment?.author } }">{{comment?.author}}
      </router-link>
    </span>
    <!-- # 6. 코멘트 좋아요 구현 -->
    <form @submit.prevent="clickLike">
      <label for="likecnt">좋아요 : {{likecnt}}</label>
      <p>
        <button v-if="alreadyLike" type="submit">
          <span class="material-symbols-outlined font-size: 10px">좋아요 취소thumb_up_off</span>
        </button>
        <button v-else type="submit">
          <span class="material-symbols-outlined font-size: 3px">좋아요 thumb_up</span>
        </button>
      </p>
    </form>
    <!-- # 12. 코멘트 삭제하기 구현 - 작성자 일경우 나오게하기!-->
    <form v-if="isSameUser&&!wantEdit" @submit.prevent="deleteComment">
      <button type="submit">
        <span class="material-symbols-outlined">삭제 delete</span>      
      </button>
    </form>
    <!-- # 13. 코멘트 수정하기 구현 - 작성자 일경우 나오게하기! -->
    <form v-if="isSameUser&&!wantEdit" @submit.prevent="clickEdit">
      <button type="submit">
        <span class="material-symbols-outlined">수정 edit</span>      
      </button>
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
        likecnt : Number,
        alreadyLike : Number,
        isSameUser : this.comment.author === this.$store.state.username ? true : false,
        wantEdit: false,
      }
    },
    created() {
      this.countLike()
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
            this.likecnt = res.data.like_users.length
            this.alreadyLike = res.data.like_users.includes(this.$store.state.userPK)
            })
            .catch((err) => 
            console.log(err)
            )
      },
      // 12. 코멘트 삭제하기 구현
      deleteComment() {
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/edit_delete/`,
        })
        .then(() => {
          this.$store.dispatch('deleteComment')
          this.$router.go(this.$router.currentRoute)
        }
          )
          .catch((err) => console.log(err))
      },
      // 13. 코멘트 수정하기 구현 (클릭시 수정하는 칸 생성)
      clickEdit() {
        this.wantEdit = !this.wantEdit 
      },
      // 13. 코멘트 수정하기 구현
      editComment() {
        axios({
          method: 'put',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/edit_delete/`,
        })
        .then(() => this.$router.go(this.$router.currentRoute))
        .catch((err) => console.log(err))
      },
    }
}
</script>

<style>

</style>