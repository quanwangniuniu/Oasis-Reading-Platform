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
        <n-form-item label="Radio Button Group" path="radioGroupValue">
          <n-radio-group name="radiogroup1">
            <n-radio-button v-for="folder in folders" :key="folder.id" :value="folder.folder_name" class="radio-item">
                {{folder.folder_name}}
              </n-radio-button>
          </n-radio-group>          
        </n-form-item>

        <n-form-item label="Radio Button Group" path="radioGroupValue">
        <n-radio-group name="radiogroup2">
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
      </n-form-item>

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
