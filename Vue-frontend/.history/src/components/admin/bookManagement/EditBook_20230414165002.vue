<script setup>
import { ref, reactive, onBeforeMount } from 'vue'
import { api_getBooks } from '../../axios/api'
const books = ref()

// 页面挂载前请求所有书籍数据
onBeforeMount(() => {
  getAllBooks()
})

const getAllBooks = () => {
  api_getBooks().then(res => {
    books.value = res.data
    console.log(books.value)
  })
}
</script>

<template>
  <div class="list-container">
    <div class="book-list">
      <el-table :data="books" style="width: 100%">
        <el-table-column prop="title" label="书名" width="250" />
        <el-table-column prop="author" label="作者" width="250" />
        <el-table-column prop="ISBN" label="ISBN" />
        <el-table-column fixed="right" label="Operations" width="150">
          <template #default>
            <el-button link type="success" size="small">编辑</el-button>
            <el-button link type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div class="pagination">
      <div class="example-pagination-block">
        <el-pagination layout="prev, pager, next" :total="1000" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.list-container {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.book-list {
  flex: 1;
  width: 100%;
  background-color: red;
}

.pagination {
  height: 50px;
  width: 100%;
  display: flex;
  align-items: center;
}


</style>
