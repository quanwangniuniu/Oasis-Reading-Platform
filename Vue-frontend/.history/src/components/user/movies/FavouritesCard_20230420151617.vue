<script setup>
const props = defineProps(['folder'])
const folder = props.folder
</script>

<template>
  <div>
    {{ folder.folder_name }}
  </div>
 
</template>

<style scoped>

</style>
