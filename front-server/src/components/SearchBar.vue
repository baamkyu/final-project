<template>
  <div>
    <!-- 여기서 class="form-control" 은 부트스트랩 사용 -->
    <input
      v-model="title"
      class="form-control"
      type="text"
      placeholder="Search for Movies"
      @keyup.enter="apply"/>
    <div class="selects">
      <select
        v-for="filter in filters"
        v-model="$data[filter.name]"
        :key="filter.name"
        class="form-select">
        <option
          v-for="item in filter.items"
          :key="item">
          {{ item }}
        </option>
      </select>
    </div>
    <button class="btn btn-primary" @click="apply">Apply</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  computed: {
      randomMovies() {
        return this.$store.state.randomMovies
    }
  },
  data() {
    return {
      title: '',
      filters: [
        {
          // 1985년부터 개봉된 영화들 1년 단위로 선택하면 가져오는듯?
          // name: 'year',
          // items: (() => {
          //   const years = []
          //   const thisYear = randomMovies.getFullYear() // 올해 년도 가져오는듯
          //   for (let i = thisYear; i>=1985; i--) {
          //     years.push(i)
          //   }
          //   return years
          // })()
        }
      ]
    }
  }
}
</script>

<style>
.selects{
  display: flex;
  select {
    width: 120px;
    margin-right: 10px;
    &:last-child {
      margin-right: 0;
    }
  }
}

.btn{
  width:120px;
  height: 50px;
  font-weight: 700;
  flex-shrink: 0;
}
</style>