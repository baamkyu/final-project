<template>
  <div>
    <hr>
    <h3>/userid/님이 선택한 /directorname/감독의 작품</h3>
    <PreferDirectorItem/>
  </div>
</template>

<script>
import PreferDirectorItem from '@/components/BodyPreferDirectorItem'

export default {
  name: 'PreferDirector',
  components: {
    PreferDirectorItem
  }
}
</script>

<style>

</style>