<template>
  <div id="top-space">
    <h1>LoginPage</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">

      <label for="password">password : </label>
      <input type="password" id="password" v-model="password">

      <input type="submit" value="logIn">
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
  padding-top: 60px;
} 
</style>