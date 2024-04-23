<script setup>

import { useRouter } from 'vue-router';
const router = useRouter();

const url = router.currentRoute.value.params.url
</script>

<template>
  <div>
    {{ url }}
  </div>
 
</template>

<style scoped>

</style>
