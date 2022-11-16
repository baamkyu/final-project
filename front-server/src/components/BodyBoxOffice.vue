<template>
  <div>
    <h3>박스오피스 순위</h3>
    <BoxOfficeItem
      v-for="randomMovie in randomMovies"
      :key="randomMovie.id"
      :randomMovie='randomMovie'
    />
  </div>
</template>

<script>
import BoxOfficeItem from '@/components/BodyBoxOfficeItem'

export default {
  name: 'BoxOffice',
  components: {
    BoxOfficeItem
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

</style>