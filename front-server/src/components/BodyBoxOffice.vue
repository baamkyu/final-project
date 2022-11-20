<template>
  <div>
    <h3 class="CategoryHeader">박스오피스 순위</h3>
    <ul>
      <BoxOfficeItem
        v-for="randomMovie in randomMovies"
        :key="randomMovie.id"
        :randomMovie='randomMovie'
        class="moviebox"
      />
    </ul>
  </div>
</template>

<script>
import BoxOfficeItem from '@/components/BodyBoxOfficeItem'

export default {
  name: 'BoxOffice',
  components: {
    BoxOfficeItem,
  },
  computed: {
    randomMovies() {
      return this.$store.state.randomMovies
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>
/* h3 {
  font-family: 'GangwonEduPowerExtraBoldA';
} */

@font-face {
    font-family: 'GangwonEduPowerExtraBoldA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/GangwonEduPowerExtraBoldA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* .moviebox{
  border:30px red;
  
} */
</style>