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
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="book-info">
        <div class="img" v-show="book.url">
          <img :src=book.url alt="">
        </div>

        <div class="info">
          <div class="book-info-title">
            {{ book.title }}
          </div>

          <div class="book-info-author">
            {{ book.author }}
          </div>
          <div>
            出版社:&nbsp;{{ book.publisher }}
          </div>
          <div>
            出版时间:&nbsp;{{ book.publish_year }}
          </div>
          <div>
            页数:&nbsp;{{ book.page }}
          </div>
          <div>
            定价:&nbsp;{{ book.price }}
          </div>
          <div>
            装帧:&nbsp;{{ book.binding }}
          </div>
          <div>
            丛书:&nbsp;{{ book.series }}
          </div>
          <div>
            ISBN:&nbsp;{{ book.ISBN }}
          </div>

        </div>

        <div class="rate">
          <n-rate readonly :default-value="3" class="rate-star" />
        </div>
        <div class="rate-number">
          {{ book.rate_avg }}            
          </div>
      </div>
      <div class="add-rate"></div>
      <div class="book-description">
        <n-ellipsis expand-trigger="click" line-clamp="10" :tooltip="false">
          {{ book.description }}
        </n-ellipsis>
      </div>
      <div class="book-comments"></div>
    </div>
  </div>
</template>

<style scoped>
.top-container {
  margin: 50px 50px 0px 50px;
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

.container {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  margin: 20px 50px 0px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
}

.book-info div {
  margin: 10px;
}

.book-info {
  flex: 1;
  box-sizing: border-box;
  height: 500px;
  padding: 25px 0px 0px 25px;
  display: flex;
  /* background-color: rgba(154, 77, 227, 0.1); */
  font-family: siyuansongti;
}

.info {
  box-sizing: border-box;
  padding-top: 20px;
  height: 400px;
  /* background-color: rgb(202, 114, 114,0.1); */
}

.title-and-rate {
  margin: 0px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.book-info-rate {
  margin: 0px !important;
  font-size: 30px;
}

.book-info-title {
  font-size: 30px;
}

.book-info-author {
  font-size: 20px;
  color: rgb(84, 84, 84);
}

.img {
  height: 400px;
  width: 250px;
}

.img img {
  height: 400px;
  width: 250px;
}

.add-rate {
  /* box-sizing:border-box;
      flex:2;
      height: 500px;
      padding: 50px 25px 0px 50px;
      display: flex; */
  box-sizing: border-box;
  flex: 1;
  height: 500px;
  padding: 25px 25px 0 10px;
  background-color: rgb(52, 155, 52, 0.1);
}

.rate {
  height: 40px;
  margin: 10px 0px !important;
  font-size: 50px;
  padding-top: 10px;
  display: flex;
  background-color: rgb(252, 171, 171);
}

.rate-star {
  margin-top: 100px;
}

.rate-number {
  line-height: 50px;
  margin: 0px;
}

.book-description {
  width: 100%;
  padding: 0px 50px 0 50px;
  white-space: pre-line;
  font-size: medium;
  color: rgb(73, 73, 73);
  font-family: siyuansongti;
}

.book-comments {
  width: 100%;
  height: 200px;
  background-color: blue;
}
</style>
