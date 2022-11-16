<template>
  <div>
    <hr>
    <h3>평균 별점이 높은 작품</h3>
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

</style>