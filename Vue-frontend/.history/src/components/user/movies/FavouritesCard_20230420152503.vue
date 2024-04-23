<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
const props = defineProps(['folder'])
const folder = props.folder

onBeforeMount(() => {
  console.log(folder.books.length)
})
</script>

<template>
  <div>
    <div class="subtitle">
      {{ folder.name }} - &nbsp; - &nbsp; - &nbsp; -
    </div>

    <div v-if="folder.books.length == 0" class="on-data-container">
      nodata
    </div>
  </div>
</template>

<style scoped>
.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}
</style>
