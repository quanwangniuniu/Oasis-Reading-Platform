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
}

.div{
flex: 1;
width: 200px;
height: 600px;
background-color: green;
}

</style>
