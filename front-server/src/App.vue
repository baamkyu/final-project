<template>
  <div class="HomePage">
    <NavBar/>
    <body class="HomePage">
      <router-view/>
    </body>


    <hr>
    <footer>
      <h3 class="howmanyscore">지금까지 {{ allCommentsCount }}개의 평가가 쌓였어요.</h3>
      <p>SSAFY 8기</p>
      <p>김관섭 임범규</p>
    </footer>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar'
export default {
  methods: {
  },
  components: {
    NavBar
  },
  computed: {
    allCommentsCount() {
      return this.$store.getters.allCommentsCount
    }
  },
}


</script>



<style>
.HomePage {
  background: black;
  color: white;
}

header {
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
body {
  /* padding-top: 75px;  */
}

footer {
  background-color: black;
  color: gray;
  text-align: center;
}


.howmanyscore{
  background-color: black;
  color: crimson;
}

* {
  background-color: black;
}

</style>