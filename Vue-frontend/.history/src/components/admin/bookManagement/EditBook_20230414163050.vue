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
    <el-table-column prop="title" label="name" width="180" />
    <el-table-column prop="author" label="author" width="180" />
    <el-table-column prop="isbn" label="isbn" />
  </el-table>
  </div>
 
</template>

<style scoped>
</style>
