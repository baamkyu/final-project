<template>
  <div>
    <h3>박스오피스 순위</h3>
    <BoxOfficeItem/>
  </div>
</template>

<script>
import BoxOfficeItem from '@/components/BodyBoxOfficeItem'

export default {
  name: 'BoxOffice',
  components: {
    BoxOfficeItem
  },
}
</script>

<style>

</style>