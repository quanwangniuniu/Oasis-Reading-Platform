<script setup>
import LeftBar from './LeftBar.vue';
</script>

<template>
  <div class="top-container">
    <div class="title">
      <span>图书</span>&nbsp;<span>books</span>
    </div>
  </div>
  <div class="container">
      <LeftBar></LeftBar>
      <div class="panel"></div>
  </div>
 
</template>

<style scoped>
.top-container{
  margin: 50px 50px 0px 50px;
  display: flex;
  justify-content: space-between;
}

.title{
  width: 200px;
  font-family: siyuansongti;
}
.container{
  display: flex;
}

.panel{
  flex: 1;
  height: 600px;
  background-color: green;
}

</style>
