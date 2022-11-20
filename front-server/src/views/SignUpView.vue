<template>
  <div id="top-space" class="text-center">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <label for="username">username   : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
      <br>
      <router-link :to="{ name: 'LoginView' }">로그인하러 가기!</router-link>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
      return {
        username: null,
        password1: null,
        password2: null,
      }
    },
  components:{
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    },
  }
}
</script>

<style>
#top-space {
  padding-top: 75px;
}
.text-center {
  text-align: center;
}
</style>