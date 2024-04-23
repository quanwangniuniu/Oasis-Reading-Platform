<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const $router = useRouter();
onMounted(() => {
  console.log('$router:', $router.currentRoute.value.params.caseId);
});
</script>

<template>
  <div>
      SpecificBook
  </div>
 
</template>

<style scoped>
</style>
