<script setup>
import MyCommentCard from './MyCommentCard.vue'

</script>

<template>
  <div>
    <div class="container">
      <MyCommentCard></MyCommentCard>
      <MyCommentCard></MyCommentCard>
      <MyCommentCard></MyCommentCard>
    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: rgb(245, 164, 164);
  padding: 15px 30px 10px 30px;
}

.container MyCommentCard:not(:first-child) {
  background-color: blue;
}
</style>
