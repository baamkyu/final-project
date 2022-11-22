<template>
  <div id="top-space">
    <BodyPage/>
  </div>
</template>

<script>
import BodyPage from '@/components/BodyPage'

export default {
  name: 'HomeView',
  components: {
    BodyPage
  },
  computed: {
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.commentCount()
    this.getUserDetail()
  },
  methods: {
    commentCount() {
      this.$store.dispatch('commentCount')
    },
    getUserDetail() {
      this.$store.dispatch('getUserDetail', this.username)
    }
  }
}

</script>

<style>
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}

#top-space {
  padding-top: 75px;
}
</style>