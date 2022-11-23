<template>
  <div class="comment-item-area">
    <br>
    <hr>
    <span>작성자 : 
      <router-link
                :to="{ name: 'MyPageView', params: { username: comment?.author } }">{{comment?.author}}
      </router-link>
    </span>
    <br>
    <br>
    <p>{{comment?.content}}</p>
    <p>{{comment?.created_at}}</p>
    <!-- # 6. 코멘트 좋아요 구현 -->
    <div class="form-inline-block">
      <form @submit.prevent="clickLike">
        <p class="button-p-size">
          <button v-if="alreadyLike" type="submit" class="thumb-button">
            <span class="blue-thumb material-symbols-outlined">thumb_up</span>
            <span>{{likecnt}}</span>
            <span class="material-symbols-outlined"></span>
          </button>
          <button v-else type="submit" class="thumb-button">
            <span class="material-symbols-outlined">thumb_up</span>
            <span>{{likecnt}}</span>
          </button>
        </p>
      </form>
      <!-- # 12. 코멘트 삭제하기 구현 - 작성자 일경우 나오게하기!-->
        <form v-if="isSameUser&&!wantEdit" @submit.prevent="deleteComment">
          <button type="submit" class="comment-icon-button">
            <span class="material-symbols-outlined">delete</span>      
          </button>
        </form>
      <!-- # 13. 코멘트 수정하기 구현 - 작성자 일경우 나오게하기! -->
      <form v-if="isSameUser&&!wantEdit" @submit.prevent="clickEdit">
        <button type="submit" class="comment-icon-button">
          <span class="material-symbols-outlined">edit </span>      
        </button>
      </form>
  </div>
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
.comment-item-area {
  margin-left: 20%;
  margin-right: 20%;
}

.comment-icon-button{
  background: #1C1D1F;
  border: 1px #1C1D1F solid;
}

.button-p-size {
  height: 12px;
  width: auto;
}

.form-inline-block{
  display: flex;
}

.blue-thumb{
  color: #1A73E8;
  }

.thumb-button {
  background-color: #1C1D1F;
  border: 1px #1C1D1F solid;
}
</style>