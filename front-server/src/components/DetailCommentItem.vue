<template>
  <div>
    <div class="comment-item-area" v-if="!wantEdit">
      <br>
      <hr>
      <span>작성자 : 
        <router-link
                  :to="{ name: 'MyPageView', params: { username: comment?.author } }">{{comment?.author}}
        </router-link>
      </span>
      <!-- <span> 좋아요 : {{likecnt}}</span> -->
      <br>
      <br>
      <p :v-model="editContent">{{comment?.content}}</p>
      <!-- <p>{{comment?.content}}</p> -->
      <p>{{comment?.created_at}}</p>
      <!-- # 6. 코멘트 좋아요 구현 -->
      <div class="form-inline-block">
        <form @submit.prevent="clickLike">
          <!-- <label for="likecnt">좋아요 : {{likecnt}}</label> -->
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
            <button type="submit">
              <span class="material-symbols-outlined">delete</span>      
            </button>
          </form>
        <!-- # 13. 코멘트 수정하기 구현 - 작성자 일경우 나오게하기! -->
        <form v-if="isSameUser&&!wantEdit" @submit.prevent="clickEdit">
          <button type="submit">
            <span class="material-symbols-outlined">edit </span>      
          </button>
        </form>
    </div>
    </div>

    <div v-if="wantEdit">
      <hr>
      <div class="comment-area">
        <form @submit.prevent="editComment" class="comment-submit">
            <label for="content"></label>
            <textarea type="text" id="content" cols="30" rows="10" class="comment" v-model="editContent"></textarea><br>
            <input type="submit" id="submit" class="comment-button" value="수정">
        </form>
    </div>
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
        editContent: this.comment?.content,
        author: this.comment?.author,
        like_users: this.comment?.like_users,
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
        const content = this.editContent
        const author = this.author
        const like_users = this.like_users
        axios({
          method: 'put',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/edit_delete/`,
          data: {content, author, like_users,}
        })
        .then(() => {
          this.$router.go(this.$router.currentRoute)
          this.wantEdit = !this.wantEdit 
          })
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

.comment-area{
    margin-left: 20%;
}

.comment {
    width: 70%;
    height: 100px;
    padding: 10px;
    background-color: #d0e2bc;
    font: 1.4em/1.6em;
    /* margin-left: 52%; */
    border-left: 6px solid #095484;
}
.comment-submit {
    /* display: inline; */
    /* margin-left:30% */
    
}

.comment-button {
    color: white;
    background: #095484;
    border-radius: 10px;
}

</style>