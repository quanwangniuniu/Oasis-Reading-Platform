<script setup>

import { ref, onBeforeMount, watch } from 'vue'
import BookCard from './BookCard.vue'
import { api_getBooksByPage, api_getTotalPages } from '../../axios/api'
import { useRouter } from 'vue-router'
import { Search } from '@vicons/ionicons5'

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
watch(page, () => {
  getBooks(page.value)
})

</script>

<template>
  <div class="main">
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
      <div>
        <n-input placeholder="搜索" size="small" class="input" v-model:value="search_input" @keyup.enter="search()">
          <template #prefix>
            <n-icon :component="Search" color="black" />
          </template>
        </n-input>

      </div>

    </div>
    <n-scrollbar style="flex-grow: 1;">
      <div class="container">
        <BookCard v-for="book in books" :key="book.id" class="card" :book-info="book"></BookCard>
      </div>
    </n-scrollbar>


    <div class="pagination-container">
      <n-pagination v-model:page="page" :page-count="totalPages" />
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

.search {
  width: 400px;
  display: flex;
  justify-content: right;
  background-color: rgb(245, 176, 176, 0.5);
}



.container {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  margin-left: 50px;
  margin-right: 50px;
}

.card {
  margin-bottom: 50px;
}


.pagination-container {
  height: 30px;
  margin-top: 10px;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.input {
  width: 300px;
}
</style>
