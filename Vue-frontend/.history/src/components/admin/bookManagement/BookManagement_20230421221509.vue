<script setup lang="ts">
import LeftBar from './LeftBar.vue';
import {ref, reactive} from 'vue'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import {api_addBook} from '../../axios/api'
import { ElMessage} from 'element-plus'
import { ElNotification } from 'element-plus'


const bookItem = reactive({
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

const imageUrl = ref('')

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
  api_addBook(bookItem).then(res => {
    console.log(res.data)
    if(res.data.code == 200){
      open()
      for (let prop in bookItem) {
        bookItem[prop] = '';
      }
      imageUrl.value = ''
    }
  })
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
  <div class="top-container">
    <div class="title">
      <span>图书管理</span>&nbsp;<span>book management</span>
    </div>
  </div>
  <div class="container">
      <LeftBar></LeftBar>
      <div class="panel">
        <router-view></router-view>
      </div>
  </div>
 
</template>

<style scoped>
.top-container{
  margin: 50px 50px 0px 50px;
  display: flex;
  justify-content: space-between;
}

.title{
  width: 400px;
  font-family: siyuansongti;
}
.container{
  display: flex;
  margin: 20px 50px 0px 50px
}

.title span:nth-child(1){
  font-size: 30px;
}
.title span:nth-child(2){
  font-size: 20px;
}

.panel{
  box-sizing: border-box;
  flex: 1;
  height: 600px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214); 
  padding: 30px;
}

.book-form{
  width: 450px;
}

.img-upload-and-submit{
  flex: 1;
  margin: 0px auto;
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
