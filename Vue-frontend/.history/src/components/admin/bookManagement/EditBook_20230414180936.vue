<script setup>
import { ref, reactive, onBeforeMount } from 'vue'
import { api_getBooks } from '../../axios/api'
import { ElMessage, ElMessageBox } from 'element-plus'
const books = ref()
const verifyDelete = ref()

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

const editBook = (row) => {
  console.log(row)
}

const deleteBook = (row) => {
  open()
  if(verifyDelete.value){
    console.log(row)
  }else{
    console.log('cancel')
  }
}

const open = () => {
  ElMessageBox.confirm(
    '确定要删除这本书吗?',
    'Warning',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    }
  )
    .then(() => {
      verifyDelete.value = true
      ElMessage({
        type: 'success',
        message: 'Delete completed',
      })
    })
    .catch(() => {
      verifyDelete.value = false
      ElMessage({
        type: 'info',
        message: 'Delete canceled',
      })
    })
}
</script>

<template>
  <div class="list-container">
    <el-table :data="books" style="width: 100%;" class="book-list">
      <el-table-column prop="id" label="编号" width="150" />
      <el-table-column prop="title" label="书名" width="250" />
      <el-table-column prop="author" label="作者" width="250" />
      <el-table-column prop="ISBN" label="ISBN" />
      <el-table-column fixed="right" label="操作" width="150">
        <template #default="scope">
          <el-button link type="success" size="small" @click="editBook(scope.row)">编辑</el-button>
          <el-button link type="danger" size="small" @click="deleteBook(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

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
  display: flex;
  flex-direction: column;
}

.pagination {
  height: 50px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
