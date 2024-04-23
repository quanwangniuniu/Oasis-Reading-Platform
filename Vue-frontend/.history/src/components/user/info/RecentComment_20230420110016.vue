<script setup>
import {ref, onBeforeMount} from 'vue'
import MyCommentCard from './MyCommentCard.vue'
import NoDataCard from './NoDataCard.vue'
import {api_getUserComments} from '../../axios/comment_api'

const comments = ref({})

onBeforeMount(()=>{
  api_getUserComments(1).then(res=>{
    comments.value = res.data.data
    console.log(comments.value)
  })
})

</script>

<template>
  <div>
    <div class="container">
      <div v-if="comments.length == 0">
        <NoDataCard></NoDataCard>
      </div>
      <div v-if="comments.length != 0">
        <MyCommentCard v-for="comment in comments" :key="comment.id" :comment = "comment"></MyCommentCard>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  /* background-color: rgb(245, 164, 164); */
  padding: 15px 30px 5px 30px;
}

</style>
