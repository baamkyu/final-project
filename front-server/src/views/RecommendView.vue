<template>
  <div id="top-space">
    <h1>맞춤 영화 찾기</h1>
    <div class="d-flex flex-wrap">
    <div v-for="time in times" :key="time" class="px-3 mb-3" @click="clickBox(time)">
      <button class="noClick" :class="{'clicked' : timeLst.includes(time)}"> {{ time }} </button>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendView',
    data: function() {
      return {
        genres: ["장르종류"],
        genre: '',
        years: [],
        year: '',
        nations: ["해외 영화", "국내 영화"],
        nation: '',
      }
    },
    methods: {
      // clickGenre: function(genre){
      //   if (this.genre.includes(genre)){
      //     this.genreData = this.genre.indexOf(genre)
      //     this.
      //   }
      // }
    }
  }
</script>

<style>

</style>