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
    <div class="list-container">
        <div class="book-list">

        </div>

        <div class="pagination">

        </div>
    </div>

  <!-- <div>
  <el-table :data="books" style="width: 100%">
    <el-table-column prop="title" label="书名" width="250" />
    <el-table-column prop="author" label="作者" width="250" />
    <el-table-column prop="ISBN" label="ISBN" />
    <el-table-column fixed="right" label="Operations" width="150">
      <template #default>
        <el-button link type="success" size="small">编辑</el-button
        >
        <el-button link type="danger" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  </div> -->
 
</template>

<style scoped>
.list-container{
    height: 100%;
    width: 100%;
    /* background-color: green; */
    display: flex;
    flex-direction: columns;
}
.book-list{
    flex: 1;
    width: 100%;
    background-color: red;
}

.pagination{
    height: 100px;
    width: 100%;
    background-color: rebeccapurple;
}
</style>
