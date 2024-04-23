<script setup>
const props = defineProps(['folder'])
const folder = props.folder
</script>

<template>
  <div>
    <div class="subtitle">
        {{ folder.name }} - &nbsp; - &nbsp; - &nbsp; -
      </div>
  </div>
 
</template>

<style scoped>

</style>
