<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { api_getAllFolders } from '../../axios/favourite_api'
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)

const folders = ref()
const isCreatingFolder = ref(false)

const model = ref({
  folder: null
})

const chosenFolder = ref()

onBeforeMount(() => {
  api_getAllFolders().then(res => {
    folders.value = res.data.data
  })
})
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px" :model="model" ref="formRef">
      <n-form :model="model">
        <n-form-item>
          <n-radio-group v-model:value="model.folder">
            <n-radio v-for="folder in folders" :key="folder.id" value="123" class="radio-item">
              {{ folder.folder_name }}
            </n-radio>
          </n-radio-group>
        </n-form-item>
        <n-button v-if="isCreatingFolder == false" strong secondary class="add-folder-btn" @click="isCreatingFolder = true">
          新建文件夹
        </n-button>
        <div v-if="isCreatingFolder == true" class="create-folder">
          <n-input v-if="isCreatingFolder == true" type="text" size="medium" class="input"/>
          <n-button strong secondary @click="isCreatingFolder = true">
            新建
          </n-button>           
        </div>
       
      </n-form>
    </n-scrollbar>

  </div>
</template>

<style scoped>
.n-space {
  display: block !important;
}

.n-radio {
  --n-radio-size: 20px !important
}

::v-deep .n-radio__dot {
  border-radius: 0% !important;
}

.radio-item {
  font-size: 15px !important;
  font-weight: lighter;
}

.add-folder-btn{
  width: 350px;
}

.create-folder{
  display: flex;
  border: 1px solid rgb(224, 224, 230)
}

::v-deep .n-input{
  --n-border: 0px;
  border-radius: 0%;
}

::v-deep .n-input:hover{
  --n-border: 1px solid rgb(224, 224, 230)
  border-radius: 0%;
}

::v-deep .n-button{
  border-left: 1px solid rgb(224, 224, 230);
  border-radius: 0%;
}
</style>
