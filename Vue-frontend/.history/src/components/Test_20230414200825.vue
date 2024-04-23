<template>
  <div class="container">
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
        <n-input
          v-model:value="bookItem.description"
          placeholder=""
          type="textarea"
          :autosize="{
            minRows: 3,
            maxRows: 3
          }"
        />
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

  <button @click="xxx">test</button>

  <input v-model="str">
</template>

<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue'
import {api_getBookById} from '../components/axios/api'

let str = ref('')

let bookItem = ref({
  id:'',
  title: '',
  author: '',
  publisher: '',
  ISBN: 0,
  description: '',
  publish_year: '',
  page:0,
  binding: '',
  price: 0,
  series:' ',
  url:''
})

onMounted(()=>{
  str.value = 'xxx'
    api_getBookById(1).then(res=>{
        bookItem.value = res.data
        console.log(bookItem)
    })
})

const xxx = () => {
  console.log(bookItem.value.title)
}

</script>
<style scoped>
.container{
  width: 400px;
}
</style>

