<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import {api_getFavourites} from '../../axios/favourite_api'
import FavouriteCard from './FavouritesCard.vue'

const folders = ref({})

onBeforeMount(()=>{
  api_getFavourites().then(res=>{
    folders.value = res.data.data
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
      <FavouriteCard v-for="folder in folders" :key="folder.id" :folder="folder">
      </FavouriteCard>
      <!-- <div class="subtitle">
        默认收藏夹 - &nbsp; - &nbsp; - &nbsp; -
      </div> -->
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
  display: flex;
}

.left-bar {
  width: 150px;
}

.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}
</style>
