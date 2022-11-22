<template>
  <div class="HomePage">
    <NavBar/>
    <body class="HomePage">
      <router-view/>
    </body>
    <footer>
      <FooterBar/>
    </footer>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar'
import FooterBar from '@/components/FooterBar'
export default {
  methods: {
  },
  components: {
    NavBar,
    FooterBar
  }
}


</script>



<style>
.HomePage {
  background: rgb(28,29,31);
  color: white;
}

.header-style {
  position: fixed;
  width:100%;
  height: 75px;
  padding: 1rem;
  color: white;
  background: black;
  display: flex;
  /* justify-content: space-between;
  align-items: center; */
}


</style>