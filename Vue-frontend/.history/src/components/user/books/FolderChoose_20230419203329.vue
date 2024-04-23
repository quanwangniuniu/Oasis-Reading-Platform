<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import {api_getAllFolders} from '../../axios/favourite_api'
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)

const folders = ref({})

onBeforeMount(()=>{
  api_getAllFolders().then(res=>{
    folders.value = res.data.data
  })
})
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px">
      <n-form size="large">
        <n-radio-group name="radiogroup1">
          <n-space>
            <n-radio v-for="folder in folders" :key="folder.id" :value="folder.folder_name" class="radio-item"></n-radio>
          </n-space>
        </n-radio-group>
      </n-form>
    </n-scrollbar>
  </div>
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
