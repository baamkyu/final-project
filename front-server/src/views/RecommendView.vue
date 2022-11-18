<template>
  <div id="top-space">
    <div class="search-wrapper">
      <input type="text" v-model="search" placeholder="Search title.."/>
          <label>Search title:</label>
    </div>
    <div class="wrapper">
      <div class="card" v-for="movie in movies" :key="movie.id">
        <small>title: {{ movie.title }}</small>
        출시년도:{{ movie.prdtYear }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'RecommendView',
  data() {
    return {
      movies: [
        {title: '미이라', prdtYear: 2010, id:1},
        {title: '범죄도시', prdtYear: 2018, id:2},
        {title: 'ironman', prdtYear: 2000, id:3}
      ]
    }
  },
  computed: {
    filteredMovies() {
      return this.movies.filter(p => {
        return p.name.toLowerCase().indexOf(this.search.toLowerCase()) != -1;
      });
    }
  }
}
</script>

<style>
#top-space {
  padding-top: 75px;
}

.card {
    box-shadow: rgba(0, 0, 0, 0.117647) 0px 1px 6px, rgba(0, 0, 0, 0.117647) 0px 1px 4px;
    max-width: 124px;
    margin: 12px;
    transition: .15s all ease-in-out;
    &:hover {
      transform: scale(1.1);
    }
}
</style>