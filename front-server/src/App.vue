<template>
  <div>
    <header class="navbar-height">
      <img src="./assets/logo.png" alt="" @click="goHome">
      <nav>
        <router-link id="nav-menu nav-left" :to="{ name: 'HomeView' }">홈</router-link>
        <router-link id="nav-menu nav-left" :to="{ name: 'RecommendView' }">추천 콘텐츠</router-link>
        <router-link id="nav-menu nav-left" :to="{ name: 'WantToSeeView' }">내가 찜한 콘텐츠</router-link>
        <router-link v-if="!isLogin" id="nav-menu nav-right" :to="{ name: 'SignUpView' }">SignUp</router-link>
        <router-link v-if="!isLogin" id="nav-menu nav-right" :to="{ name: 'LoginView' }">
          <span class="material-symbols-outlined">login</span>
          Login
        </router-link>
        <button v-else id="nav-menu nav-right" @click="logOut">
          <span class="material-symbols-outlined">logout</span>
          LogOut
        </button>
        <span class="material-symbols-outlined" id="nav-right">
        person
        </span>{{ this.$store.state.username }}님 반갑습니다.
        <span class="material-symbols-outlined">
        menu
        </span>
        <span class="material-symbols-outlined">
        menu_open
        </span>
        <!-- <router-link v-if="isLogin" type="button" @click="logOut">LogOut</router-link> -->
      </nav>
    </header>

    <body>
      <router-view/>
    </body>


    <hr>
    <footer>
      <h3 class="howmanyscore">지금까지 {{allCommentsCount}}개의 평가가 쌓였어요.</h3>
      <p>SSAFY 8기</p>
      <p>김관섭 임범규</p>
    </footer>



  </div>
</template>

<script>
export default {
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
    allCommentsCount() {
      return this.$store.getters.allCommentsCount
    }
  }
}


</script>


<style>

header {
  position: fixed;
  width:100%;
  height: 60px;
  padding: 1rem;
  color: white;
  background: black;
  display: flex;
  /* justify-content: space-between; */
  align-items: center;
}

body {
  /* padding-top: 75px; */
}

footer {
  background-color: black;
  color: gray;
  text-align: center;
}

img {
  /* margin-right: 1000px; */

}

#nav-right {
  /* z-index: 1; */
  /* margin-left: auto; */
  text-align: right;
}

#nav-left {
  /* margin-right: auto; */
  text-align: left;
}

nav a {
  /* font-weight: bold; */
  /* color: #2c3e50; */
}

/* 얘 왜 빨간색 안 되지?, 홈 누르면 align중간이 맞나? */
nav a.router-link-exact-active {
  font-weight: bold;
  align-items: center;
  text-align: center;
  color: red;
}


#nav-menu {
  text-decoration: none;
  cursor: pointer;
  margin-right: 20px;
  color: white;
}

.howmanyscore{
  color: crimson;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}
button {
  background-color: black;
  color: white;
}

* {
  font-family: 'HSSaemaul-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/HSSaemaul-Regular.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>
