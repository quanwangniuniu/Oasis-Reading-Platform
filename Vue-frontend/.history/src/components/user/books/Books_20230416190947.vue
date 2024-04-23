<script setup>

import { ref, onBeforeMount, watch } from 'vue'
import BookCard from './BookCard.vue'
import {api_getBooksByPage, api_getTotalPages } from '../../axios/api'
import { useRouter } from 'vue-router'

const router = useRouter()


let books = ref([])
const search_input = ref('')
const page = ref(1)
const totalPages = ref(0)

// 页面挂载前请求所有书籍数据
onBeforeMount(() => {
  getBooks(1)
  getTotalPages()
})

const getTotalPages = () => {
  api_getTotalPages().then(res => {
    totalPages.value = res.data
  })
}

const getBooks = (page) => {
  console.log(page)
  api_getBooksByPage(page).then(res => {
    books.value = res.data
    console.log(books.value)
  })
}

// 搜索功能：push到search组件,传递用户输入的书名作为参数
const search = () => {
  console.log(search_input.value)
  router.push({ name: 'transit', query: { title: search_input.value } })
}

//计算属性监听页码变化
watch(page, ()=>{
  getBooks(page.value)
})

</script>

<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
      <div class="search">
        <!-- <input class="search-input" v-model="search_input" />
        <el-icon class="search-icon" @click="search">
          <Search />
        </el-icon> -->
      </div>
    </div>
    <div class="container">
      <BookCard v-for="book in books" :key="book.id" class="card" :book-info="book"></BookCard>
    </div>

    <div class="pagination-container">
      <n-pagination v-model:page="page" :page-count="totalPages" />
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
  background-color: rgb(245, 176, 176, 0.5);
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


.pagination-container{
  margin-top: 50px;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
