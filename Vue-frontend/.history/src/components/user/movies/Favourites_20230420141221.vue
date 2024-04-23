<script setup>
</script>

<template>
  <div class="main">
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
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
  width: 200px;
  font-family: siyuansongti;
}

.title span:nth-child(1) {
  font-size: 30px;
}

.title span:nth-child(2) {
  font-size: 20px;
}
</style>
