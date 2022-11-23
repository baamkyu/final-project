<template>
    <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie?.poster_path}`" @click="goMovieDetail">
</template>

<script>
export default {
  name: 'WantListItem',
  props: {
    movie: Object
  },
  methods:{
    goMovieDetail() {
      this.$router.push({ name:'DetailView', params: { id: this.movie?.id } })
    }
  }
}
</script>

<style>
  .wantlist-img-container{
    border: 1px solid white;

  }
</style>