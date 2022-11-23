<template>
    <!-- CreateComment < DetailView -->
    <div class="comment-area">
        <h3 v-if="commentCnt">{{commentCnt}}개의 댓글</h3>
        <h3 v-else>댓글이 없습니다.</h3>
        <form @submit.prevent="createComment" class="comment-submit">
            <label for="content"></label>
            <textarea type="text" id="content" cols="30" rows="10" v-model.trim="content" class="comment" placeholder="이 영화의 후기를 남겨주세요!"></textarea><br>
            <input type="submit" id="submit" class="comment-button" value="등록">
        </form>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'CreateComment',
    data() {
        return {
            content: null,
            like_users: [],
            // author: this.$store.state.username,
        }
    },
    computed: {
        commentCnt() {
            return this.$store.state.comments.comment_set.length
        }
    },
    props: {
        moviePk: Number,
    },
    methods: {
        // 9. 커멘트 추가하기
        createComment() {
            const content = this.content
            const like_users = this.like_users
            const author = this.$store.state.username
            
            if (!content) {
                alert('내용을 입력해주세요!')
                return
            }
            axios({
                method: 'post',
                url: `${API_URL}/api/v1/movies/${this.moviePk}/comments/`,
                data: {content, like_users, author,},
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
                .then((res) => {
                    // 원래 url주소로 redirect 시키기
                    this.$router.go(this.$router.currentRoute)
                    this.$store.dispatch('createComment', res.data)
                })
                .catch((err) => console.log(err))
        },
    },
}
</script>

<style>
/* .community{
    word-break: keep-all;
    border: 1px solid #ddd;
    padding: 10px;
    display: flex;
    justify-content: center;
    width: 80%;
    height: 75px;
    line-height: 160%;
} */

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