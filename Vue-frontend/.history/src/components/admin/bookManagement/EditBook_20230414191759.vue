<script setup lang="ts">
import {ref, reactive, onMounted} from 'vue'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import {api_addBook, api_getBookById} from '../../axios/api'
import { ElMessage} from 'element-plus'
import { ElNotification } from 'element-plus'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()

const imageUrl = ref('')
const id = route.query.id;

let bookItem = reactive({
  id:'',
  title: '',
  author: '',
  publisher: '',
  isbn: '',
  description: '',
  publish_year: '',
  page:'',
  binding: '',
  price:'',
  seriers:' ',
  url:''
})

onMounted(()=>{
    api_getBookById(id).then(res=>{
        bookItem = res.data
        console.log(res.data)
    })
})


const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  bookItem.url = response.url
  bookItem.id = response.id
  imageUrl.value = URL.createObjectURL(uploadFile.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (rawFile.type !== 'image/jpeg') {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}

const addBook = ()=>{
    console.log(boo)
//   api_addBook(bookItem).then(res => {
//     console.log(res.data)
//     if(res.data.code == 200){
//       open()
//       for (let prop in bookItem) {
//         bookItem[prop] = '';
//       }
//       imageUrl.value = ''
//     }
//   })
}

const open = () => {
  ElNotification.success({
    title: 'Success',
    message: '添加图书成功',
    offset: 100,
  })
}


</script>

<template>
    <div class="container">
        <div class="book-form">
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
              <el-input v-model="bookItem.isbn" />
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
              <el-input v-model="bookItem.seriers" />
            </el-form-item>
            <el-form-item label="出版日期">
              <el-input v-model="bookItem.publish_year" />
            </el-form-item>
          </el-form>
        </div>
        <div class="img-upload-and-submit">
          <div class="img-container">
            <div class="img-upload">
              <el-upload
                class="avatar-uploader"
                action="http://127.0.0.1:5000/uploadCover"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload"
              >
                <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
              </el-upload>
            </div>
          </div>
          <div class="submit">
            <button @click="addBook">添加</button>
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
