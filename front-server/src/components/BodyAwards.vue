<template>
  <div>
    <h3 class="CategoryHeader">올해의 수상작</h3>
    <AwardsItem/>
  </div>
</template>

<script>
import AwardsItem from '@/components/BodyAwardsItem'

export default {
  name: 'AwardsMovie',
  components: {
    AwardsItem
  }
}
</script>

<style>
.CategoryHeader {
  margin: 0 0 16px 36px;
  padding: 0 0 0 32;
}
</style>