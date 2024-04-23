<script setup>
import { reactive, ref, h, watch, computed } from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter();

const url = ref(router.currentRoute.value.params.url)
</script>

<template>
  <div>
    {{ url }}
  </div>
 
</template>

<style scoped>

</style>
