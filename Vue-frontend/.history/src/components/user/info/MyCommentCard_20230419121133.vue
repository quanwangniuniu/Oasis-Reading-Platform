<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['comment'])
const commentObj = ref(props.comment)
</script>

<template>
  <div>
    <div class="container">
        <div class="img-container"><img src="" alt=""></div>
        <div class="comment-container">
            <div class="rate"></div>
            <div class="comment"></div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: rgb(158, 246, 155);
  height: 120px;
  margin-bottom: 15px;
}

.container{
    display: flex;
    align-items: center;
}

.img-container{
    height: 120px;
    width: 75px;
    background-color: red;
}
</style>
