<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/'
const $router = useRouter();
const id = $router.currentRoute.value.params.id

onMounted(() => {
    getBookById(id).then(res=>{
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
