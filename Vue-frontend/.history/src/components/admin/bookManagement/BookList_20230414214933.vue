<script setup>
import { ref, reactive, onBeforeMount } from 'vue'
import { api_getBooks, api_deleteBookById, api_getBooksByPage } from '../../axios/api'
import { ElMessage, ElMessageBox,ElNotification  } from 'element-plus'
import { useRouter } from 'vue-router'

const router = useRouter()

const books = ref()
const current_page = ref(1)

// 页面挂载前请求所有书籍数据
onBeforeMount(() => {
  getAllBooks(1)
})

//请求所有书籍, 页面挂载和删除数据后触发
const getAllBooks = (page) => {
  console.log(page)
  api_getBooksByPage(page).then(res => {
    books.value = res.data
    console.log(books.value)
  })
}

//编辑图书函数, 跳转至/admin/books/edit组件
const editBook = (bookItem) => {
  console.log(bookItem)
  router.push({ path: '/admin/books/edit', query: { id: bookItem.id } })
}

//删除图书函数, 
const deleteBook = (row) => {
  api_deleteBookById(row.id).then(res => {
    getAllBooks()
    ElMessage({
      message: '删除成功',
      type: 'success',
      duration: 1500
    })
  })
}

//删除后开启提示让用户确认是否删除
const open = (row) => {
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
      deleteBook(row)
    })
    .catch(() => {
      ElNotification.error({
        title: 'error',
        message: '取消删除',
        offset: 100,
        duration: 1500
      })
      console.log('cancel')
    })
}


const handleCurrentChange = (number) => {
  getAllBooks(number)
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
          <el-button link type="danger" size="small" @click="open(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="pagination">
      <el-pagination layout="prev, pager, next" :total="50" @current-change="handleCurrentChange" />
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
