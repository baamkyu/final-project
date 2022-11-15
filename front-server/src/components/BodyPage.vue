<template>
  <div>
    <BoxOffice/>
    <PreferDirector/>
    <PreferActor/>
    <AverageScore/>
  </div>
</template>

<script>
import BoxOffice from '@/components/BodyBoxOffice'
import PreferDirector from '@/components/BodyPreferDirector'
import PreferActor from '@/components/BodyPreferActor'
import AverageScore from '@/components/BodyAverageScore'

export default {
  name: 'BodyPage',
  components: {
    BoxOffice,
    PreferDirector,
    PreferActor,
    AverageScore
  }
}
</script>

<style>

</style>