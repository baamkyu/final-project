<template>
  <!-- 댓글 -->
  <div>
    <DetailCommentItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
    <br>
  </div>
</template>

<script>
import DetailCommentItem from '@/components/DetailCommentItem'

export default {
    name: 'DetailComment',
    components: {
      DetailCommentItem,
    },
    computed: {
      comments() {
        return this.$store.state.comments.comment_set
      },
    }
}
</script>

<style>
</style>