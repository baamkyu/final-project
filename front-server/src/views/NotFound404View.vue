<template>
  <div id="top-space" class="page-min-height">
    <img src="../assets/page404.png" class="Page404">
  </div>
</template>

<script>
export default {
  name: 'NotFound404',
}
</script>

<style>
#top-space {
  padding-top: 75px;
}
.page-min-height{
  min-height: 100vw;
}

.Page404 {
  display:block;
  height: 600px;
  weight: 100vw;
  margin-left: auto;
  margin-right: auto;
}

@font-face {
  font-family: 'DungGeunMo';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>