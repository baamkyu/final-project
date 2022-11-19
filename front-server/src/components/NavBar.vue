<template>
  <nav class="nav">
    <div class="nav-left">
      <div>
        <img class="nav-logo" src="../assets/삼조로고1.png" alt="" @click="goHome">
      </div>
      <div class="nav-left-menu">
        <router-link id="nav-menu" :to="{ name: 'HomeView' }">홈</router-link>
        <router-link id="nav-menu" class="here :active" :to="{ name: 'RecommendView' }">추천 콘텐츠</router-link>
        <router-link id="nav-menu" class="here :active" :to="{ name: 'WantToSeeView' }">내가 찜한 콘텐츠</router-link>
      </div>
    </div>
<!-- RESET CSS 해보기!! -->
    <div class="nav-right">
      <!-- 로그인 되어 있지 않으면 SignUp, Login 출력 -->
      <div class="nav-right-menu">
        <router-link v-if="!isLogin" id="nav-menu" class="here" :to="{ name: 'SignUpView' }">
          회원가입
        </router-link>
        <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'LoginView' }">
          <span class="material-symbols-outlined">Login
            <span>로그인  </span>
          </span>
        </router-link>
        <!-- 로그인 되어있으면 LogOut, userID 출력 -->
        <button v-if="isLogin" id="nav-menu" @click="logOut">
          <span class="material-symbols-outlined">logout
            <span>로그아웃</span>
          </span>
        </button>

          <span v-if="isLogin" class="material-symbols-outlined">person
            <span>
              <router-link id="nav-menu" 
                :to="{ name: 'MyPageView', params: { username: this.$store.state.username } }">{{ this.$store.state.username }}
              </router-link>님 반갑습니다.
            </span> 

          <!-- <span v-if="isLogin" id="nav-menu" class="material-symbols-outlined">person
            <span class="username-font">{{ this.$store.state.username }}님 반갑습니다.</span> -->

          </span>
        <!-- 메뉴는 로그인 상관 없이 출력 -->
          <span class="material-symbols-outlined">
          menu
          </span>
          <!-- <span class="material-symbols-outlined">
          menu_open
          </span> -->
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
  /* height: 3.5rem; */
  /* box-shadow: 0 1px 0 0 rgb(0 0 0 / 8%); */
  justify-content: space-between;
  /* display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
  grid-template-areas: "left right"; */
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
  gap: 2rem;
}

.nav-right {
  display: flex;
  grid-area: right;
  align-items: center;
  justify-content: flex-end;
  padding-right: 3.5rem;
}

.nav-menu {
  display: flex;
  flex-direction: row;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  color: white;
  gap: 0.1rem;
}

.nav-left-menu {
  flex-direction: row;
  display: flex;
  /* gap: 1rem; */
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

.username-font {
  font-family: FlowerSalt;
}

@font-face {
    font-family: 'FlowerSalt';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/FlowerSalt.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

</style>