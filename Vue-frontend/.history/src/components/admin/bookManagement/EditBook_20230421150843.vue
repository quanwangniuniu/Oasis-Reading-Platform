<script setup lang="ts">
import {ref, reactive, onMounted} from 'vue'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import {api_updateBook, api_getBookById} from '../../axios/api'
import { ElMessage} from 'element-plus'
import { ElNotification } from 'element-plus'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()

const imageUrl = ref('')
const id = route.query.id;

let bookItem = ref({
  id:'',
  title: '',
  author: '',
  publisher: '',
  ISBN: '',
  description: '',
  publish_year: '',
  page:'',
  binding: '',
  price:'',
  series:' ',
  url:''
})

onMounted(()=>{
  getBookInfo()
})

const getBookInfo = () => {
  api_getBookById(id).then(res=>{
        bookItem.value = res.data
        imageUrl.value = bookItem.value.url
        console.log(bookItem)
    })
}


// const handleAvatarSuccess: UploadProps['onSuccess'] = (
//   response,
//   uploadFile
// ) => {
//   bookItem.value.url = response.url
//   bookItem.value.id = response.id
//   imageUrl.value = URL.createObjectURL(uploadFile.raw!)
// }

// const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
//   if (rawFile.type !== 'image/jpeg') {
//     ElMessage.error('Avatar picture must be JPG format!')
//     return false
//   } else if (rawFile.size / 1024 / 1024 > 2) {
//     ElMessage.error('Avatar picture size can not exceed 2MB!')
//     return false
//   }
//   return true
// }


const updateBook = () => {
  api_updateBook(bookItem.value).then(res => {
    console.log(res.data)
    if(res.data.code == 200){
      open()
      router.push( {path: '/admin/books/list'})
    }
  })
}

const open = () => {
  ElNotification.success({
    title: 'Success',
    message: '修改图书信息成功',
    offset: 100,
    duration: 1500
  })
}


</script>

<template>
    <div class="container">
        <div class="book-form">

          <n-form ref="formRef" :model="bookItem" >
            <n-grid :cols="24" :x-gap="24">
              <n-form-item path="title" label="书名" :span="24">
                <n-input 
                  placeholder="请输入书名" 
                  class="input" 
                  v-model:value="bookItem.title"
                >
                </n-input>  
              </n-form-item>
            </n-grid>
          </n-form>
<!-- 
          <el-form
            label-position="top"
            label-width="100px"
            :model="bookItem"
            style="max-width: 460px"
            :inline="true"
          >
            <el-form-item label="书名" style="width:420px">
              <el-input v-model="bookItem.title" />
            </el-form-item>
            <el-form-item label="作者">
              <el-input v-model="bookItem.author" />
            </el-form-item>
            <el-form-item label="出版社">
              <el-input v-model="bookItem.publisher" />
            </el-form-item>
            <el-form-item label="简介" style="width:420px">
                <el-input v-model="bookItem.description" type="textarea"/>
            </el-form-item> 
            <el-form-item label="ISBN">
              <el-input v-model="bookItem.ISBN" />
            </el-form-item>
            <el-form-item label="装帧">
              <el-input v-model="bookItem.binding" />
            </el-form-item>
            <el-form-item label="页数">
              <el-input v-model="bookItem.page" />
            </el-form-item>
            <el-form-item label="价格">
              <el-input v-model="bookItem.price" />
            </el-form-item>
            <el-form-item label="系列名">
              <el-input v-model="bookItem.series" />
            </el-form-item>
            <el-form-item label="出版日期">
              <el-input v-model="bookItem.publish_year" />
            </el-form-item>
          </el-form> -->
        
        </div>
        <div class="img-upload-and-submit">
          <div class="img-container">
            <div class="img-upload">
              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            </div>
          </div>
          <div class="submit">
            <button @click="updateBook">修改</button>
          </div>
        </div>
    </div>
 
</template>

<style scoped>
.container{
    width: 100%;
    display: flex;
}
.book-form{
  width: 450px;
}

.img-upload-and-submit{
  flex: 1;
}

.img-container{
  width: 100%;
  height: 450px;
}

.img-upload{
  width: 250px;
  height: 400px;
  margin: 0 auto;
}
.avatar{
  width: 250px;
  height: 400px;
}
.submit{
  height: 100px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.submit button{
  width: 300px;
  height: 50px;
  border: none;
  background-color: rgb(52, 52, 52);
  box-shadow: 0px 1px 3px 2px rgb(214, 214, 214);
  color: white;
  font-size: 20px;
}
</style>
