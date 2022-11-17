<template>
  <div id="top-space">
    <BodyPage/>
    <span class="material-symbols-outlined">
      menu
    </span>
    <span class="material-symbols-outlined">
    favorite
    </span>
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
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}

#top-space {
  padding-top: 60px;
}
</style>