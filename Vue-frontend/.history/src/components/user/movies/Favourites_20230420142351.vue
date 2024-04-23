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
      <div class="left-bar">
        <n-list hoverable clickable>
          <n-list-item>
            fsdfsdf
          </n-list-item>
          <n-list-item>
            sfsdf
          </n-list-item>
        </n-list>
      </div>

      <div class="content">

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
  width: 400px;
  font-family: siyuansongti;
}

.title span:nth-child(1) {
  font-size: 30px;
}

.title span:nth-child(2) {
  font-size: 20px;
}

.panel {
  /* height: 500px; */
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti;
  padding: 30px;
  height: 400px;
}

.carousel-img {
  margin: 0 auto;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
