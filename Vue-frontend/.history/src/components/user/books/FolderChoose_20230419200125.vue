<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 120px">
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
        {{favouriteObj.book_id}}
    </n-scrollbar>
  </div>
 
</template>

<style scoped>

</style>
