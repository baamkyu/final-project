<template>
  <div id= "top-space" class="wrap">
    <form class="login" @submit.prevent="logIn">
      <h2 class="login-title">로그인</h2>
      <div class="login_id">
        <h4 for="username">아이디</h4>
        <input type="text" id="username" placeholder="아이디" v-model="username">
      </div>
      <div class="login_pw">
          <h4 for="password">비밀번호</h4>
          <input type="password" id="password" placeholder="비밀번호" v-model="password">
      </div>
      <div class="submit">
        <input type="submit" value="submit">
      </div>
      <br>
      <router-link :to="{ name: 'SignUpView' }" class="go-loginpage">회원가입하러 가기!</router-link>
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

.login_a {
  text-decoration: none;
  color: black;
}

.login_li {
  list-style: none;
}

.wrap {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.1);
}

.login {
  width: 30%;
  height: 600px;
  background: white;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border: white 1px solid;
}

h2 {
  color: tomato;
  font-size: 2em;
}
.login_sns {
  padding: 20px;
  display: flex;
}

.login_sns li {
  padding: 0px 15px;
}

.login_sns a {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  border-radius: 50px;
  background: white;
  font-size: 20px;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.4), -3px -3px 5px rgba(0, 0, 0, 0.1);
}

.login_id {
  margin-top: 20px;
  width: 80%;
  text-decoration: none;
  color: black;
}

.login_id input {
  width: 100%;
  height: 50px;
  border-radius: 30px;
  margin-top: 10px;
  padding: 0px 20px;
  border: 1px solid lightgray;
  outline: none;
}

.login_pw {
  margin-top: 20px;
  width: 80%;
  text-decoration: none;
  color: black;
}

.login_pw input {
  width: 100%;
  height: 50px;
  border-radius: 30px;
  margin-top: 10px;
  padding: 0px 20px;
  border: 1px solid lightgray;
  outline: none;
}

.login_etc {
  padding: 10px;
  width: 80%;
  font-size: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.submit {
  margin-top: 50px;
  width: 80%;
}
.submit input {
  width: 100%;
  height: 50px;
  border: 0;
  outline: none;
  border-radius: 40px;
  background: linear-gradient(to left, rgb(255, 77, 46), rgb(255, 155, 47));
  color: white;
  font-size: 1.2em;
  letter-spacing: 2px;
}

</style>