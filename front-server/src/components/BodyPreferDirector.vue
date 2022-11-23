<template>
  <div>
    <hr>
    <h3 class="CategoryHeader">/userid/님이 선택한 /directorname/감독의 작품</h3>
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
.CategoryHeader {
  margin: 0 0 0px 36px;
  /* padding: 0 0 0 32; */
  font-family: TmonMonsori;
}
@font-face {
    font-family: 'TmonMonsori';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>