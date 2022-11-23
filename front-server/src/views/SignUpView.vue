<template>
    <div id= "top-space" class="wrap">
    <form class="login" @submit.prevent="signUp">
      <h2 class="login-title">회원가입</h2>
      <div class="sign_sns">
        <li class="login_li"><a class="login_a" href=""><i class="fab fa-instagram"></i></a></li>
        <li class="login_li"><a class="login_a" href=""><i class="fab fa-facebook-f"></i></a></li>
        <li class="login_li"><a class="login_a" href=""><i class="fab fa-twitter"></i></a></li>
      </div>

      <div class="login_id">
        <h4 for="username">아이디</h4>
        <input type="text" id="username" placeholder="아이디" v-model="username">
      </div>
      <div class="login_pw">
          <h4 for="password">비밀번호</h4>
          <input type="password" id="password" placeholder="비밀번호" v-model="password1">
      </div>
      <div class="login_pw">
          <h4 for="password">비밀번호 재확인</h4>
          <input type="password" id="password" placeholder="비밀번호 재확인" v-model="password2">
      </div>
      <div class="submit" >
        <input type="submit" value="submit">
        
      </div>
      <br>
      <router-link :to="{ name: 'LoginView' }" class="go-loginpage">로그인하러 가기!</router-link>
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
    // isPWSame() {
    //   if (this.password1 != this.password2)
    //     alert('비밀번호가 일치하지 않습니다.')
    //     this.password1 = null
    //     this.password2 = null
    //   }
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
  background: rgb(25,26,28);
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.login-title {
  color: white;
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
  color: lightgray;
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
  color: lightgray;
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
  background: linear-gradient(to left, rgb(25,26,28), gray);
  color: white;
  font-size: 1.2em;
  letter-spacing: 2px;
}

.go-loginpage{
  color: white;
  
}
</style>