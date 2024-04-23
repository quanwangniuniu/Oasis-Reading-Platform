<template>
  <div class="container">
    <n-form ref="formRef" :model="model" label-placement="top">
      <n-grid :cols="24" :x-gap="24">
        <n-form-item-gi :span="24" label="书名">
          <n-input v-model:value="model.inputValue" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="作者">
          <n-input v-model:value="model.inputValue" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="出版社">
          <n-input v-model:value="model.inputValue" placeholder="Input" />
        </n-form-item-gi>
        <n-form-item-gi :span="24" label="简介" path="textareaValue">
        <n-input
          v-model:value="model.textareaValue"
          placeholder="Textarea"
          type="textarea"
          :autosize="{
            minRows: 3,
            maxRows: 5
          }"
        />
      </n-form-item-gi>
      </n-grid>
    </n-form>
  </div>

</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'

const model = ref({
  inputValue: null,
  textareaValue: null,
  selectValue: null,
  multipleSelectValue: null,
  datetimeValue: null,
  nestedValue: {
    path1: null,
    path2: null
  },
  switchValue: false,
  checkboxGroupValue: null,
  radioGroupValue: null,
  radioButtonGroupValue: null,
  inputNumberValue: null,
  timePickerValue: null,
  sliderValue: 0,
  transferValue: null
})

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

