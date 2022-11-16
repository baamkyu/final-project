<template>
  <div>
    <BoxOffice/>
    <AwardsMovie/>
    <PreferDirector/>
    <PreferActor/>
    <AverageScore/>
  </div>
</template>

<script>
import BoxOffice from '@/components/BodyBoxOffice'
import AwardsMovie from '@/components/BodyAwards'
import PreferDirector from '@/components/BodyPreferDirector'
import PreferActor from '@/components/BodyPreferActor'
import AverageScore from '@/components/BodyAverageScore'

export default {
  name: 'BodyPage',
  components: {
    BoxOffice,
    PreferDirector,
    PreferActor,
    AverageScore,
    AwardsMovie
  }
}
</script>

<style>

</style>