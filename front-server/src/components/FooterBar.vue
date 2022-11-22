<template>
  <div class="howmanycomment">
    <h3 class="footer-comment">지금까지 {{ allCommentsCount }}개의 평가가 쌓였어요.</h3>
    <p class="footer-text">SSAFY 8기</p>
    <p class="footer-text">김관섭 임범규</p>
  </div>
</template>

<script>
export default {
  name: 'FooterBar',
  computed: {
    allCommentsCount() {
      return this.$store.getters.allCommentsCount
    }
  }
}
</script>

<style>
.howmanycomment{
  text-align: center;
  background-color: black;
}

.footer-comment{
  color: crimson;
}
.footer-text {
  color: gray
}
</style>