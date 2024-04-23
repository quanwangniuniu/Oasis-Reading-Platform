<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const $router = useRouter();
const id = $router.currentRoute.value.params.id

let book = ref()

onMounted(() => {
    getBookById(id).then(res=>{
      book.value = res.data
    })
});

</script>

<template>
  <div>
      {{book}}
  </div>
 
</template>

<style scoped>
</style>
