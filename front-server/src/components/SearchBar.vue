<template>
  <div id="nav">
    <div class="menu-nav">
      <div class="search-form">
          <!-- 엔터 클릭시 searchresultshow 실행 -->
        <b-form-input
          size="sm"
          class="mr-sm-2"
          type="text"
          placeholder="검색어를 입력해주세요"
          v-model="keyword"
          @keyup.enter="searchresultshow(keyword)"
        ></b-form-input>
        <!-- 버튼 클릭시 searchresultshow 실행 -->
        <b-button
          size="sm"
          class="my-2 my-sm-0"
          type="submit"
          @click="searchresultshow(keyword)"
        >
          <b-icon icon="search"></b-icon>
        </b-button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Nav",
  data() {
    return {
      keyword: ''
    }
  },
  methods: {
    search(keyword) {
      if (keyword !== ''){ //검색어를 입력한 경우
        this.$router.push({
          name: "SearchPage",
          params: {
            keyword: this.keyword,
            isResultShow: true,
          },
        });
        this.keyword = ''
        console.log('"',keyword,'"' + ' 검색')
      } else {
        alert('검색어를 입력해주세요!')  //검색어를 입력하지 않은 경우
      }
    },
  }
};
</script>