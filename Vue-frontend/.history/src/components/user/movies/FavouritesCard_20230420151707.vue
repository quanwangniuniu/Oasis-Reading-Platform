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
.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}
</style>
