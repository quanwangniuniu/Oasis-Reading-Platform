<template>
  <div class="container">
    <n-form ref="formRef" :model="bookItem" label-placement="top">
      <n-grid :cols="24" :x-gap="24">
        <n-form-item-gi :span="24" label="书名">
          <n-input v-model:value="bookItem.title" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="作者">
          <n-input v-model:value="bookItem.author" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="出版社">
          <n-input v-model:value="bookItem.publisher" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="24" label="简介" path="textareaValue">
        <n-input
          v-model:value="bookItem.description"
          placeholder="Textarea"
          type="textarea"
          :autosize="{
            minRows: 3,
            maxRows: 3
          }"
        />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="ISBN">
          <n-input v-model:value="bookItem.isbn" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="装帧">
          <n-input v-model:value="bookItem.binding" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="页数">
          <n-input v-model:value="bookItem.page" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="价格">
          <n-input v-model:value="bookItem.price" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="页数">
          <n-input v-model:value="bookItem.page" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="价格">
          <n-input v-model:value="bookItem.price" placeholder="Input" />
        </n-form-item-gi>
      </n-grid>
    </n-form>
  </div>

</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'


let bookItem = reactive({
  id: '',
  title: '',
  author: 'sdfa',
  publisher: '',
  isbn: '',
  description: '',
  publish_year: '',
  page: '',
  binding: '',
  price: '',
  seriers: ' ',
  url: ''
})


</script>
<style scoped>
.container{
  width: 400px;
}
</style>

