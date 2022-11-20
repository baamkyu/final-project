<template>
  <div id="top-space" class="text-center" >
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="username">ID: </label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password">PW </label>
      <input type="password" id="password" v-model="password">
      <br>
      <input type="submit" value="logIn"><br>
      <router-link :to="{ name: 'SignUpView' }">회원가입하러 가기!</router-link>
    </form>
  </div>
</template>

<script>

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  components: {
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password,
      }
      this.$store.dispatch('logIn', payload)
    }
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