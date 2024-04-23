<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    {{favouriteObj.book_id}}
  </div>
 
</template>

<style scoped>

</style>
