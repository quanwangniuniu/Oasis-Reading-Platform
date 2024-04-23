<script setup lang="ts">
import {ref, reactive} from 'vue'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import {api_addBook} from '../../axios/api'
import { ElMessage} from 'element-plus'
import { ElNotification } from 'element-plus'
import {validatePrice, validatePage} from '../../../util/validate'

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
  xxx:'',
  series:' ',
  serie:'',
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
  // api_addBook(bookItem).then(res => {
  //   console.log(res.data)
  //   if(res.data.code == 200){
  //     open()
  //     for (let prop in bookItem) {
  //       bookItem[prop] = '';
  //     }
  //     imageUrl.value = ''
  //   }
  // })
  console.log(bookItem)
}

const open = () => {
  ElNotification.success({
    title: 'Success',
    message: '添加图书成功',
    offset: 100,
  })
}

const rules = {
  title: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: '书名不能为空'
    },
  ],
  author: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: '作者不能为空'
    },
  ],  
  publisher: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: '出版社不能为空'
    },
  ], 
  description: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: '书籍简介不能为空'
    },
  ],   
  ISBN: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: 'ISBN不能为空'
    },
  ], 
  binding: [
    {
      required: true,
      trigger: ["input", "blur"],
      message: '装帧不能为空'
    },
  ], 
  page: [
    {
      required: true,
      trigger: ["input", "blur"],
      validator: validatePage,
    },
  ], 
  price: [
     {
      required: true,
      trigger: ["input", "blur"],
      validator: validatePrice,
    },   
  ],
  eee:[
     {
      required: true,
      trigger: ["input", "blur"],
      validator: validatePrice,
    },   
  ],

};



</script>

<template>
    <div class="container">
        <div class="book-form">
          <n-form ref="formRef" :model="bookItem" :rules="rules">
            <n-grid :cols="24" :x-gap="24">
              <n-form-item-gi path="title" label="书名" :span="24">
                <n-input 
                  placeholder="请输入书名" 
                  class="input" 
                  v-model:value="bookItem.title"
                  maxlength="30"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="author" label="作者" :span="12">
                <n-input 
                  placeholder="请输入作者" 
                  class="input" 
                  v-model:value="bookItem.author"
                  maxlength="30"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="publisher" label="出版社" :span="12">
                <n-input 
                  placeholder="请输入出版社" 
                  class="input" 
                  v-model:value="bookItem.publisher"
                  maxlength="30"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="description" label="简介" :span="24">
                <n-input 
                  type = "textarea"
                  placeholder="请输入书籍简介" 
                  class="input" 
                  v-model:value="bookItem.description"
                  :autosize="{minRows: 3, maxRows: 3}"
                  maxlength="2000"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="ISBN" label="ISBN" :span="12">
                <n-input 
                  placeholder="请输入ISBN" 
                  class="input" 
                  v-model:value="bookItem.isbn"
                  maxlength="10"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="binding" label="装帧" :span="12">
                <n-input 
                  placeholder="请输入装帧" 
                  class="input" 
                  v-model:value="bookItem.binding"
                  maxlength="10"
                  show-count
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="page" label="页数" :span="12">
                <n-input 
                  placeholder="请输入页数" 
                  class="input" 
                  v-model:value="bookItem.page"
                >
                </n-input>  
              </n-form-item-gi>

              <n-form-item-gi path="price" label="价格" :span="12">
                <n-input 
                  placeholder="请输入价格" 
                  class="input" 
                  v-model:value="bookItem.price"
                >
                </n-input>  
              </n-form-item-gi>    
              
              <n-form-item-gi path="publish_year" label="系列名" :span="12">
                <n-input 
                  placeholder="请输入系列名" 
                  class="input" 
                  v-model:value="bookItem.series"
                >
                </n-input>  
              </n-form-item-gi>  

              <n-form-item-gi path="publish_year" label="出版日期" :span="12">
                <n-input 
                  placeholder="请输入出版日期" 
                  class="input" 
                  v-model:value="bookItem.publish_year"
                >
                </n-input>  
              </n-form-item-gi>    
            </n-grid>
          </n-form>

          
          <!-- <el-form
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
          </el-form> -->
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
  border: 3px dashed rgb(225, 225, 225);
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


::v-deep .el-upload{
  height: 400px;
  width: 250px;
}
</style>
