<template>
  <div>
    <h3>박스오피스 순위</h3>
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
* {
  font-family: 'HSSaemaul-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/HSSaemaul-Regular.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
/* .moviebox{
  display: flex;
  flex-direction: row;
} */
</style>