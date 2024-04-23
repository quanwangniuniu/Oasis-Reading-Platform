<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import { api_addBook, api_getBookById } from '../../axios/api'
import { ElMessage } from 'element-plus'
import { ElNotification } from 'element-plus'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()

const imageUrl = ref('')
const id = route.query.id;

let bookItem = ref({
  id: '',
  title: '',
  author: '',
  publisher: '',
  ISBN: '',
  description: '',
  publish_year: '',
  page: '',
  binding: '',
  price: '',
  series: ' ',
  url: ''
})

onMounted(() => {
  api_getBookById(id).then(res => {
    bookItem = res.data
    console.log(bookItem)
  })
})


const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  bookItem.value.url = response.url
  bookItem.value.id = response.id
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

const addBook = () => {
  console.log(bookItem)
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
      <n-form ref="formRef" :model="bookItem" label-placement="top">
        <n-grid :cols="24" :x-gap="24">
          <n-form-item-gi :span="24" label="书名">
            <n-input v-model:value="bookItem.title" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="作者">
            <n-input v-model:value="bookItem.author" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="出版社">
            <n-input v-model:value="bookItem.publisher" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="24" label="简介" path="textareaValue">
            <n-input v-model:value="bookItem.description" placeholder="" type="textarea" :autosize="{
              minRows: 3,
              maxRows: 3
            }" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="ISBN">
            <n-input v-model:value="bookItem.ISBN" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="装帧">
            <n-input v-model:value="bookItem.binding" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="页数">
            <n-input v-model:value="bookItem.page" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="价格">
            <n-input v-model:value="bookItem.price" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="系列名">
            <n-input v-model:value="bookItem.series" placeholder="" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="出版日期">
            <n-input v-model:value="bookItem.publisher" placeholder="" />
          </n-form-item-gi>
        </n-grid>
      </n-form>
    </div>
    <div class="img-upload-and-submit">
      <div class="img-container">
        <div class="img-upload">
          <el-upload class="avatar-uploader" action="http://127.0.0.1:5000/uploadCover" :show-file-list="false"
            :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="avatar-uploader-icon">
              <Plus />
            </el-icon>
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
.container {
  width: 100%;
  display: flex;
}

.book-form {
  width: 450px;
}

.img-upload-and-submit {
  flex: 1;
}

.img-container {
  width: 100%;
  height: 450px;
}

.img-upload {
  width: 250px;
  height: 400px;
  margin: 0 auto;
}

.avatar {
  width: 250px;
  height: 400px;
}

.submit {
  height: 100px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.submit button {
  width: 300px;
  height: 50px;
  border: none;
  background-color: rgb(52, 52, 52);
  box-shadow: 0px 1px 3px 2px rgb(214, 214, 214);
  color: white;
  font-size: 20px;
}
</style>
