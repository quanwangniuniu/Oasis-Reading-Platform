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
        <div class="cover-and-rate"></div>
        <div class="title-and-desc"></div>
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
  margin: 20px 50px 0px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
}

.book-info{
  width: 100px;
  height: 500px;
  background-color: green;
}


</style>
