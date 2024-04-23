<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['comment'])
const commentObj = ref(props.comment)
</script>

<template>
  <div>
    <div class="container">
        <div class="img-container"><img :src="commentObj.url" alt=""></div>
        <div class="comment-container">
            <div class="comment-info">
              <div class="title">
                {{ commentObj.title }}
              </div>
              <div class="rating">
                    <n-rate readonly :default-value=commentObj.rate/2 size="small" />
                </div>
              <div class="date">
                {{ commentObj.created_time }}
              </div>
            </div>
            <div class="comment">
              {{ commentObj.comment }}
            </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  /* background-color: rgb(158, 246, 155); */
  height: 120px;
  margin-bottom: 15px;
  box-shadow: 0px 0px 2px 2px rgb(214, 214, 214); 
}

.container{
    display: flex;
    align-items: center;
}

.img-container, .img-container img{
    height: 120px;
    width: 75px;
}

.comment-info{
  display: flex;
  margin-left: 10px;
}

.comment-info > div{
  display: flex;
  flex-direction: column;
  justify-content: end;
  margin-right: 5px;
}

.title{
  font-size: 25px;
}

.comment{
  height: 60px;
  margin-left: 10px;
  font-size: 20px;
  font-family: 'Courier New', Courier, monospace;
}

.rating{
  padding-bottom: 10px;
}

.date{
  padding-bottom: 7px;
  color: grey;
}
</style>
