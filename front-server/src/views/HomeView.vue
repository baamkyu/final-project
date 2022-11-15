<template>
  <div id="top-space">
    <BodyPage/>
  </div>
</template>

<script>
import BodyPage from '@/components/BodyPage'

export default {
  name: 'HomeView',
  components: {
    BodyPage
  }
}
</script>

<style>
#top-space {
  padding-top: 30px;
}
</style>