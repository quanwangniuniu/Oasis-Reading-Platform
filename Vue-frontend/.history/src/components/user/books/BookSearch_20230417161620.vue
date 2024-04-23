<script setup>

import { ref, onBeforeMount } from 'vue'
import BookCard from './BookCard.vue'
import { api_getBookByTitle } from '../../axios/api'
import { useRoute, useRouter } from 'vue-router'
import { Search } from '@vicons/ionicons5'
const route = useRoute()
const router = useRouter()

let title = route.query.title;
let books = ref([])
const search_input = ref('')


const search = () => {
  router.push({ name: 'searchTransit', query: { title: search_input.value } })
}

onBeforeMount(() => {
  api_getBookByTitle(title).then(res => {
    books.value = res.data
  })
})


</script>

<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>搜索</span>&nbsp;<span>books</span>
      </div>
      <n-input placeholder="搜索" class="input" v-model:value="search_input" @keyup.enter="search()">
        <template #prefix>
          <n-icon :component="Search" color="black" />
        </template>
      </n-input>
    </div>
    <div class="container">
      <BookCard v-for="book in books" :key="book.id" class="card" :book-info="book"></BookCard>
    </div>
  </div>
</template>

<style scoped>
.top-container {
  margin: 50px 50px -30px 50px;
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

.search {
  width: 400px;
  display: flex;
  justify-content: right;
}

.search-input {
  border: 0px;
  padding: 0;
  outline: none;
  box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
  height: 40px;
  width: 400px;
  z-index: 1;
}

.search-icon {
  z-index: 2;
  margin-left: -40px;
}

.search-input:focus {
  border-color: green;
  outline-color: gray;
}

.container {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  margin-left: 50px;
  margin-right: 50px;
}

.card {
  margin-top: 50px;
}

.input {
  width: 300px;
  height: 100%;
}</style>
