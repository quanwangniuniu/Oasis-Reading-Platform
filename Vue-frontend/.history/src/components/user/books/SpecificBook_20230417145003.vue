<script setup>
import { reactive, ref } from 'vue'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import { api_getBookById } from '../../axios/api'
const router = useRouter();
const id = router.currentRoute.value.params.id

let book = ref({})

onBeforeMount(() => {
  api_getBookById(id).then(res => {
    book.value = res.data
  })
});

</script>


<template>
  <div>
    <div class="top-container">
      <div class="top-title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="book-info">
        <div class="cover-and-rate">
          <img :src=book.url alt="">
          <div class="rate-container">
            <div class="book-rate"><div>{{ book.rate_avg }}</div></div>
            <div class="book-star"></div>
          </div>
        </div>
        <div class="title-and-desc">
          <div class="book-title">
            <div>{{ book.title }}</div>
          </div>
          <div class="book-author">
            <div>{{ book.author }}</div>
          </div>
          <div class="book-desc">
            <n-ellipsis expand-trigger="click" line-clamp="16" :tooltip="false">
            {{ book.description }}
            </n-ellipsis>            
          </div>

        </div>
        <div class="info"></div>
      </div>

      <div class="comments">

      </div>

    </div>
  </div>
</template>

<style scoped>
.top-container {
  margin: 50px 50px 0px 50px;
  display: flex;
  justify-content: space-between;
}

.top-title {
  width: 200px;
  font-family: siyuansongti;
}

.top-title span:nth-child(1) {
  font-size: 30px;
}

.top-title span:nth-child(2) {
  font-size: 20px;
}

.container {
  margin: 20px 50px 0px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti;
}

.book-info {
  background-color: rgb(188, 224, 188);
  padding: 30px;
  display: flex;

}

.comments {
  height: 300px;
  background-color: rgb(218, 188, 224);
}

.cover-and-rate {
  height: 500px;
  width: 250px;
  background-color: rgb(255, 182, 133);
  margin-right: 30px;
}

.cover-and-rate img {
  height: 400px;
  width: 250px;
  margin: 0px;
}

.rate-container{
  display: flex;
  background-color: rgb(235, 119, 119);
  align-items: center;
}

.book-star{
  width: 100px;
  height: 60px;
  background-color: yellow;
}

.book-rate{
  width: 100px;
  background-color: green;
  display: flex;
  flex-direction: column;
  justify-content: end;
  font-size: 30px;
}
.title-and-desc {
  flex: 1;
  background-color: rgb(154, 231, 231);
}

.title {
  display: flex;
}

.book-title {
  font-size: 40px;
}

.book-author {
  font-size: 20px;
  color: grey;
  margin-top: -10px;
  margin-bottom: 10px;
}

.book-desc{
  white-space: pre-line;
}

.info {
  height: 500px;
  width: 250px;
  background-color: rgb(142, 142, 244);
  margin-left: 30px;
}</style>
