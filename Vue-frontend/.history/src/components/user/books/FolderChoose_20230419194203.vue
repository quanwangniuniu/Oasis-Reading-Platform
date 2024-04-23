<script setup>
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    {{favouriteObj.id}}
  </div>
 
</template>

<style scoped>

</style>
