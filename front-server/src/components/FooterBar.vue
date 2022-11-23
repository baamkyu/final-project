<template>
  <div class="howmanycomment">
    <h3 class="footer-comment">지금까지 ★{{ allCommentsCount }}개의 평가가 쌓였어요</h3>
    
    <div class="footer-container">
        <div class="material-symbols-outlined footer-left-item film-icon-size">movie_edit</div>
        <div class="footer-right-item">
          SSAFY 8기
          <br>
          김관섭 임범규
        </div>
        
    </div>

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
  height:100%;
}

.footer-comment{
  padding-top: 10px;
  color: crimson;
}
.footer-text {
  color: gray
}

.footer-container {
  display: inline-flex;
  justify-content: center;
  background-color: black;
  height: 110px;
}

.footer-left-item {
  display: flex;
  justify-content: center;
}
.footer-right-item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.film-icon-size {
  font-size: 100px;
}

</style>