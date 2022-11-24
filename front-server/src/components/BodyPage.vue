<template>
  <div>
    <BoxOffice/>
    <RandomMovie/>
    <AwardsMovie/>
  </div>
</template>

<script>
import BoxOffice from '@/components/BoxOffice'
import RandomMovie from '@/components/RandomMovie'
import AwardsMovie from '@/components/BodyAwards'

export default {
  name: 'BodyPage',
  components: {
    RandomMovie,
    AwardsMovie,
    BoxOffice,
  },
}
</script>

<style>
@font-face {
    font-family: 'Cafe24Ssurround';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/Cafe24Ssurround.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'TmonMonsori';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>