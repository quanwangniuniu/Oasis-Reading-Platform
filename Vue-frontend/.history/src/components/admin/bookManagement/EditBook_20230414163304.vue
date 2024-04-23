<script setup>
import {ref, reactive, onBeforeMount} from 'vue'
import {api_getBooks} from '../../axios/api'
const books = ref()

  // 页面挂载前请求所有书籍数据
  onBeforeMount(() =>{
    getAllBooks()
  })

  const getAllBooks = () =>{
    api_getBooks().then(res=>{
      books.value = res.data
      console.log(books.value)
    })
  }
</script>

<template>
  <div>
  <el-table :data="books" style="width: 100%">
    <el-table-column prop="title" label="书名" width="250" />
    <el-table-column prop="author" label="作者" width="250" />
    <el-table-column prop="ISBN" label="ISBN" />
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default>
        <el-button link type="primary" size="small" @click="handleClick"
          >Detail</el-button
        >
        <el-button link type="primary" size="small">Edit</el-button>
      </template>
    </el-table-column>
  </el-table>
  </div>
 
</template>

<style scoped>
</style>
