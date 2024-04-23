<script setup>
import LeftBar from './LeftBar.vue';
</script>

<template>
  <div class="container">
      <LeftBar></LeftBar>
      <div class="panel"></div>
  </div>
 
</template>

<style scoped>

.container{
  display: flex;
  padding: 50px;
}

.panel{
  flex: 1;
  height: 600px;
  background-color: green;
}

</style>
