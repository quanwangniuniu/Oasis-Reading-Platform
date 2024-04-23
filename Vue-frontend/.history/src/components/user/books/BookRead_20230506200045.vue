<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';

const props = defineProps(['url'])
const url = ref(props.url)

</script>

<template>
  <div>
    {{ url }}
  </div>
 
</template>

<style scoped>

</style>
