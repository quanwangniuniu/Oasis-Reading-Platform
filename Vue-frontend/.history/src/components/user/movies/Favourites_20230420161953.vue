<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { api_getFavourites } from '../../axios/favourite_api'
import FavouriteCard from './FavouritesCard.vue'

const folders = ref({})

onBeforeMount(() => {
  api_getFavourites().then(res => {
    folders.value = res.data.data
    // folders.value.sort((a, b) => b.books.length - a.books.length)
    console.log(res.data.data)
  })
})

</script>

<template>
  <div class="main">
    <div class="top-container">
      <div class="title">
        <span>我的收藏</span>&nbsp;<span>Favourites</span>
      </div>
    </div>
    <div class="panel">


      <n-collapse>
        <n-collapse-item v-for="folder in folders" :key="folder.id" :name="folder.id" :title="folder.name">
          <FavouriteCard :folder="folder"></FavouriteCard>
        </n-collapse-item>
      </n-collapse>

<!-- 
      <FavouriteCard v-for="folder in folders" :key="folder.id" :folder="folder">
      </FavouriteCard> -->
    </div>
  </div>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  margin-bottom: 50px;
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
  padding: 50px;
  /* width: 1000px; */
}

.left-bar {
  width: 150px;
}

::v-deep .n-collapse-item__header-main{
  font-size: 20px;
  color: rgb(2, 128, 2) !important;
  font-family: deyihei;
}
</style>
