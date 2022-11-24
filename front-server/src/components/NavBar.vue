<template>
  <nav class="nav">
    <div class="nav-left">
      <div>
        <img class="nav-logo" src="../assets/삼조의 영화방.png" alt="" @click="goHome">
      </div>
      <div class="nav-left-menu">
        <router-link id="nav-menu" :to="{ name: 'HomeView' }">홈</router-link>
        <router-link id="nav-menu" class="here :active" :to="{ name: 'RecommendView' }">맞춤 콘텐츠</router-link>
      </div>
    </div>
<!-- RESET CSS 해보기!! -->
    <div class="nav-right">
      <!-- 로그인 되어 있지 않으면 SignUp, Login 출력 -->
      <div class="nav-right-menu">
        <router-link v-if="!isLogin" id="nav-menu" class="here" :to="{ name: 'SignUpView' }">
          <span class="material-symbols-outlined">assignment_ind 회원가입</span>
        </router-link>
        <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'LoginView' }">
          <span class="material-symbols-outlined">Login
            <span>로그인</span>
          </span>
        </router-link>
        <!-- 로그인 되어있으면 LogOut, userID 출력 -->
        <button v-if="isLogin" id="nav-menu" @click="logOut">
          <span class="material-symbols-outlined navbar-icon">logout</span>
          <span id="nav-menu">로그아웃</span>
        </button>

        <span v-if="isLogin" class="material-symbols-outlined username-font navbar-icon" id="nav-menu-person-icon">person
        <!-- <span class="username-font" id="nav-menu"> -->
        <router-link class="font-color-white" id="nav-menu-id"
          :to="{ name: 'MyPageView', params: { username: this.$store.state.username } }">{{ this.$store.state.username }}
        </router-link>
        <span id="nav-menu">님 반갑습니다.</span>
        <!-- </span> -->
        </span>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    logOut() {
      this.$store.commit('NULL_TOKEN')
      alert('로그아웃 되었습니다.')
    },
    goHome() {
      this.$router.push({ name:'HomeView' })
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  }
}
</script>

<style>

.nav {
  position: fixed;
  background-color: black;
  z-index: 99;
  width: 100vw;
  justify-content: space-between;
}

.nav-logo {
  padding: 3px;
  cursor: pointer;
}

.nav-left {
  display: flex;
  grid-area: left;
  align-items: center;
  padding-left: 1rem;
  gap: 3.5rem;
}


.nav-right {
  display: flex;
  grid-area: right;
  align-items: center;
  justify-content: flex-end;
  padding-right: 3.5rem;
}

.nav-menu {
  /* display: flex;
  flex-direction: row;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  color: white;
  gap: 0.1rem; */
}

.nav-menu-username {
  display: flex;
  flex-direction: row;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  color: white;
}

.font-color-white{
  text-decoration: none;
  color: white;
}
.nav-left-menu {
  flex-direction: row;
  display: flex;
}

.nav-right-menu { 
  /* display: flex;
  flex-direction: row;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  color: white;
  gap: 0.1rem; */
}



/* 얘 왜 빨간색 안 되지?, 홈 누르면 align중간이 맞나? */
/* nav a.router-link-exact-active {
  align-items: center;
  text-align: center;
  color: red;
} */


#nav-menu {
  text-decoration: none;
  cursor: pointer;
  margin-right: 20px;
  font-size: 19px;  
  color: white;
  font-family: 'Happiness-Sans-Title';
  transition: color 0.5s ease-in-out;
}
#nav-menu:hover{
  color: lightgray;
  opacity: 0.8;
}

#nav-menu-id{
  text-decoration: none;
  cursor: pointer;
  margin-left: -10px;
  font-size: 19px;  
  color: white;
  font-family: 'Happiness-Sans-Title';
  transition: color 0.5s ease-in-out;
}
#nav-menu-id:hover{
  text-decoration: underline;
}


#nav-menu-person-icon {
  text-decoration: none;
  cursor: pointer;
  margin-right: 20px;
  font-size: 19px;  
  color: white;
  transition: color 0.5s ease-in-out;
}
#nav-menu-person-icon:hover{
  color: lightgray;
  opacity: 0.8;
}


.howmanyscore{
  color: crimson;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 700,
  'GRAD' 0,
  'opsz' 48;
  margin-right: 10px;
  font-size: 19px;
  justify-content: flex-end;
}


button {
  background-color: black;
  color: white;
}


.navbar-icon{
  margin-top: -10px;
}

@font-face {
    font-family: 'FlowerSalt';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/FlowerSalt.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'Cafe24Oneprettynight';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Oneprettynight.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'NanumSquareNeo-Variable';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'Happiness-Sans-Title';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2205@1.0/Happiness-Sans-Title.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

</style>