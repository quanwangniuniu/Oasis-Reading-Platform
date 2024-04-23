<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import {api_getAllFolders} from '../../axios/favourite_api'
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)

const folders = ref()

const model = ref({
  folder: null
})

const chosenFolder = ref()

onBeforeMount(()=>{
  api_getAllFolders().then(res=>{
    folders.value = res.data.data
  })
})
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px" :model="model" ref="formRef">
      <n-form       ref="formRef"
      :model="model"
      label-placement="left"
      :label-width="160"
      :disabled="updateDisabled"
      :style="{
        maxWidth: '640px'
      }">
        <n-form-item>
          <n-radio-group name="radiogroup1" v-model:value="model.folder">
            <n-radio v-for="folder in folders" :key="folder.id" value="123" class="radio-item">
                {{folder.folder_name}}
              </n-radio>
          </n-radio-group>          
        </n-form-item>
      </n-form>
    </n-scrollbar>
  </div>

  <n-form
      ref="formRef"
      :model="model"
      label-placement="left"
      :label-width="160"
      :disabled="updateDisabled"
      :style="{
        maxWidth: '640px'
      }"
    >
    <n-form-item label="Radio Group" path="radioGroupValue">
        <n-radio-group v-model:value="model.folder" name="radiogroup2">
          <n-radio value="Radio 1">
            Radio 1
          </n-radio>
          <n-radio value="Radio 2">
            Radio 2
          </n-radio>
          <n-radio value="Radio 3">
            Radio 3
          </n-radio>
        </n-radio-group>
      </n-form-item>
    </n-form>
</template>

<style scoped>
.n-space{
  display: block  !important;
}
.n-radio{
  --n-radio-size:20px !important
}

::v-deep .n-radio__dot{
  border-radius:0% !important;
}

.radio-item{
  font-size: 25px;
  font-weight: lighter;
}
</style>
