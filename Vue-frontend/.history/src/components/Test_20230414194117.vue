<template>
  <n-form ref="formRef" :model="model" label-placement="top">
    <n-grid :cols="24" :x-gap="24">
      <n-form-item-gi :span="12" label="Input" path="inputValue">
        <n-input v-model:value="model.inputValue" placeholder="Input" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Textarea" path="textareaValue">
        <n-input v-model:value="model.textareaValue" placeholder="Textarea" type="textarea" :autosize="{
          minRows: 3,
          maxRows: 5
        }" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Select" path="selectValue">
        <n-select v-model:value="model.selectValue" placeholder="Select"/>
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Multiple Select" path="multipleSelectValue">
        <n-select v-model:value="model.multipleSelectValue" placeholder="Select"   multiple />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Datetime" path="datetimeValue">
        <n-date-picker v-model:value="model.datetimeValue" type="datetime" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Switch" path="switchValue">
        <n-switch v-model:value="model.switchValue" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Checkbox Group" path="checkboxGroupValue">
        <n-checkbox-group v-model:value="model.checkboxGroupValue">
          <n-space>
            <n-checkbox value="Option 1">
              Option 1
            </n-checkbox>
            <n-checkbox value="Option 2">
              Option 2
            </n-checkbox>
            <n-checkbox value="Option 3">
              Option 3
            </n-checkbox>
          </n-space>
        </n-checkbox-group>
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Radio Group" path="radioGroupValue">
        <n-radio-group v-model:value="model.radioGroupValue" name="radiogroup1">
          <n-space>
            <n-radio value="Radio 1">
              Radio 1
            </n-radio>
            <n-radio value="Radio 2">
              Radio 2
            </n-radio>
            <n-radio value="Radio 3">
              Radio 3
            </n-radio>
          </n-space>
        </n-radio-group>
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Radio Button Group" path="radioGroupValue">
        <n-radio-group v-model:value="model.radioGroupValue" name="radiogroup2">
          <n-radio-button value="Radio 1">
            Radio 1
          </n-radio-button>
          <n-radio-button value="Radio 2">
            Radio 2
          </n-radio-button>
          <n-radio-button value="Radio 3">
            Radio 3
          </n-radio-button>
        </n-radio-group>
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Input Number" path="inputNumberValue">
        <n-input-number v-model:value="model.inputNumberValue" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Time Picker" path="timePickerValue">
        <n-time-picker v-model:value="model.timePickerValue" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Slider" path="sliderValue">
        <n-slider v-model:value="model.sliderValue" :step="5" />
      </n-form-item-gi>
      <n-form-item-gi :span="14" label="Transfer" path="transferValue">
        <n-transfer v-model:value="model.transferValue" style="width: 100%"   />
      </n-form-item-gi>
      <n-form-item-gi :span="5" label="Nested Path" path="nestedValue.path1">
        <n-cascader v-model:value="model.nestedValue.path1" placeholder="Nested Path 1"  />
      </n-form-item-gi>
      <n-form-item-gi :span="5" path="nestedValue.path2">
        <n-select v-model:value="model.nestedValue.path2" placeholder="Nested Path 2"   />
      </n-form-item-gi>
      <n-gi :span="24">
        <div style="display: flex; justify-content: flex-end">
          <n-button round type="primary">
            验证
          </n-button>
        </div>
      </n-gi>
    </n-grid>
  </n-form>
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
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

