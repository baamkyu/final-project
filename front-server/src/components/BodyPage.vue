<template>
  <div>
    <BoxOffice/>
    <RealBoxOffice/>
    <AwardsMovie/>
    <PreferDirector/>
    <PreferActor/>
    <AverageScore/>
    <!-- <SearchBar/> -->
  </div>
</template>

<script>
import BoxOffice from '@/components/BodyBoxOffice'
import AwardsMovie from '@/components/BodyAwards'
import PreferDirector from '@/components/BodyPreferDirector'
import PreferActor from '@/components/BodyPreferActor'
import AverageScore from '@/components/BodyAverageScore'
import RealBoxOffice from '@/components/RealBoxOffice'
// import SearchBar from '@/components/SearchBar'

export default {
  name: 'BodyPage',
  components: {
    BoxOffice,
    PreferDirector,
    PreferActor,
    AverageScore,
    AwardsMovie,
    RealBoxOffice,
    // SearchBar
  },
}
</script>

<style>

</style>