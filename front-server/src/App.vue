<template>
  <div id="app">
    <nav>
      <img src="./assets/logo.png" alt="">
      <router-link id="nav-text-deco" :to="{ name: 'HomeView' }">홈</router-link> |
      <router-link id="nav-text-deco" :to="{ name: 'RecommendView' }">추천 콘텐츠</router-link> |
      <router-link id="nav-text-deco" :to="{ name: 'WantToSeeView' }">내가 찜한 콘텐츠</router-link> |
    </nav>
    <router-view/>
  </div>
</template>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.app {
  min-height: 60px;
}

#nav-text-deco {
  text-decoration: none; 
}

img {
  margin-right: 10px;
}
</style>
