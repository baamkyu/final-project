<template>
  <div>
    <BoxOffice/>
    <RandomMovie/>
    <AwardsMovie/>
    <PreferDirector/>
    <PreferActor/>
    <AverageScore/>
    <!-- <SearchBar/> -->
  </div>
</template>

<script>
import BoxOffice from '@/components/BoxOffice'
import RandomMovie from '@/components/RandomMovie'
import AwardsMovie from '@/components/BodyAwards'
import PreferDirector from '@/components/BodyPreferDirector'
import PreferActor from '@/components/BodyPreferActor'
import AverageScore from '@/components/BodyAverageScore'
// import SearchBar from '@/components/SearchBar'

export default {
  name: 'BodyPage',
  components: {
    RandomMovie,
    PreferDirector,
    PreferActor,
    AverageScore,
    AwardsMovie,
    BoxOffice,
    // SearchBar
  },
}
</script>

<style>

</style>