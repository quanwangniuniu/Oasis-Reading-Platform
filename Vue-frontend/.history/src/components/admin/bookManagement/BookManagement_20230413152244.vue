<script setup>
import LeftBar from './LeftBar.vue';
</script>

<template>
  <div class="container">
      <LeftBar></LeftBar>
      <div></div>
  </div>
 
</template>

<style scoped>

.container{
  display: flex;
}

.div{
flex: 1;
height: 600px;
background-color: green;
}

</style>
