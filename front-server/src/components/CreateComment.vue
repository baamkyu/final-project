<template>
    <!-- CreateComment < DetailView -->
    <div>
        <h3>게시글 작성</h3>
        <form @submit.prevent="createComment">
            <label for="content">내용 : </label>
            <textarea type="text" id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
            <input type="submit" id="submit">
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
    props: {
        moviePk: Number,
    },
    methods: {
        // 9. 커멘트 추가하기
        createComment() {
            const content = this.content
            const like_users = this.like_users
            const author = this.$store.state.username
            
            // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            console.log(author)
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
                    console.log(author)
                    this.$router.go(this.$router.currentRoute)
                    this.$store.dispatch('createComment', res.data)
                })
                .catch((err) => console.log(err))
        },
    },
}
</script>

<style>

</style>