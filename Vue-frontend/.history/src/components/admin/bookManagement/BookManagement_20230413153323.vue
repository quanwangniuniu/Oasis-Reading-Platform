<script setup>
import LeftBar from './LeftBar.vue';
</script>

<template>
  <div class="top-container">
    <div class="title">
      <span>图书管理</span>&nbsp;<span>book management</span>
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
  width: 300px;
  font-family: siyuansongti;
}
.container{
  display: flex;
  margin: 20px 50px 0px 50px
}

.title span:nth-child(1){
  font-size: 30px;
}
.title span:nth-child(2){
  font-size: 20px;
}

.panel{
  flex: 1;
  height: 600px;
  background-color: green;
}

</style>
