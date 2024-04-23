<script setup>
</script>

<template>
  <div class="main">
    <div class="top-container">
      <div class="title">
        <span>我的收藏</span>&nbsp;<span>Favourites</span>
      </div>
    </div>

    <div class="panel">

    </div>
  </div>
</template>

<style scoped>
.main {
  height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
}

.top-container {
  margin: 50px 50px 20px 50px;
  height: 50px;
  display: flex;
  justify-content: space-between;
}

.title {
  width: 400px;
  font-family: siyuansongti;
}

.title span:nth-child(1) {
  font-size: 30px;
}

.title span:nth-child(2) {
  font-size: 20px;
}

.panel{
  /* height: 500px; */
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti; 
  padding: 0px 30px 30px 30px;
  background-color: red;
}
</style>
