<script setup>
import LeftBar from './LeftBar.vue';
import {ref} from 'vue'


const bookItem = ref({
  title: '',
  author: '',
  publisher: '',
  ISBN: '',
  description: '',
  publish_year: '',
  page:'',
  binding: '',
  price:'',
  seriers:' '
})


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
        <div>
          <el-form
            label-position="top"
            label-width="100px"
            :model="formLabelAlign"
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
              <el-input v-model="bookItem.price" />
            </el-form-item>
            <el-form-item label="出版日期">
              <el-input v-model="bookItem.price" />
            </el-form-item>
          </el-form>
        </div>
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

</style>
