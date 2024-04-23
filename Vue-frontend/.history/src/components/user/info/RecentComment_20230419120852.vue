<script setup>
import {ref, onBeforeMount} from 'vue'
import MyCommentCard from './MyCommentCard.vue'
import {api_getUserComments} from '../../axios/comment_api'

onBeforeMount(()=>{
  api_getUserComments(1).then(res=>{
    console.log(res.data)
  })
})

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
  padding: 15px 30px 5px 30px;
}

</style>
