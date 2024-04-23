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
      <n-form size="large">
        <n-form-item v-model:value="model.folder">
          <n-radio-group name="radiogroup1">
            <n-radio v-for="folder in folders" :key="folder.id" :value="folder.folder_id" class="radio-item">
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
      <n-radio-group name="radiogroup1">
            <n-radio v-for="folder in folders" :key="folder.id" v-model:value="folder.folder_id" class="radio-item">
                {{folder.folder_name}}
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
