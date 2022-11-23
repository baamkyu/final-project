<template>
  <div>
    <hr>
    <h3 class="CategoryHeader">평균 별점이 높은 작품</h3>
    <AverageScoreItem/>
  </div>
</template>

<script>
import AverageScoreItem from '@/components/BodyAverageScoreItem'

export default {
  name: 'AverageScore',
  components: {
    AverageScoreItem
  }
}
</script>

<style>
@font-face {
    font-family: 'TmonMonsori';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>