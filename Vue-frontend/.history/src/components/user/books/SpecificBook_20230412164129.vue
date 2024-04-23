<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const $router = useRouter();

onMounted(() => {
  getBookById().then(res=>{
    console.log(res.data)
  })
});
</script>

<template>
  <div>
      SpecificBook
  </div>
 
</template>

<style scoped>
</style>
