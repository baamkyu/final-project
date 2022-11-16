<template>
  <div>
    <hr>
    <h3>/userid/님이 선택한 /actorname/배우의 작품</h3>
    <PreferActorItem/>
  </div>
</template>

<script>
import PreferActorItem from '@/components/BodyPreferActorItem'

export default {
  name: 'PreferActor',
  components: {
    PreferActorItem
  }
}
</script>

<style>

</style>