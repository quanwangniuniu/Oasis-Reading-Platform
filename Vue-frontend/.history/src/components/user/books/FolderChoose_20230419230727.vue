<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { api_getAllFolders, api_addFolder, api_addFavourite } from '../../axios/favourite_api'
import { Add } from '@vicons/ionicons5'
import { useRoute, useRouter } from 'vue-router'
import { useMessage } from 'naive-ui'
const route = useRoute()
const router = useRouter()
const message = useMessage()
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)

// 收藏夹列表对象
const folders = ref()
// 是否正在创建收藏夹, 控制页面显示效果
const isCreatingFolder = ref(false)
// 新建文件夹的名称
const newFolderName = ref('')



//页面挂载时加载所有文件夹
onBeforeMount(() => {
  loadFolders()
})

//向后端请求收藏夹列表
const loadFolders = () => {
  api_getAllFolders().then(res => {
    folders.value = res.data.data
    console.log(favouriteObj.value)
  })
}

//创建收藏夹
const creatFolder = () => {
  console.log('xxx')
  api_addFolder(newFolderName.value).then(res => {
    if (res.data.code == 200) {
      console.log(res)
      loadFolders()
      isCreatingFolder.value = false
    }

  })
}


const commitAddFavourite = () => {
  favouriteObj.value.type = 2
  api_addFavourite(favouriteObj.value).then(res => {
    console.log(res.data)
    message.success('收藏成功')
    router.push({ path: '/transit', query: { path1: '/books/' + favouriteObj.value.book_id, path2: '/admin/' + favouriteObj.value.book_id } })
  })
}

// 创建收藏夹input框失去焦点时触发
const closeCreateFolder = () => {
  isCreatingFolder.value = false
}
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px" ref="formRef">
      <n-form>
        <n-form-item>
          <n-radio-group v-model:value="favouriteObj.folder">
            <n-radio v-for="folder in folders" :key="folder.id" :value="folder.id" class="radio-item">
              {{ folder.folder_name }}
            </n-radio>
          </n-radio-group>
        </n-form-item>
        <div v-if="isCreatingFolder == false" class="add-folder-btn" @click="isCreatingFolder = true">
          <n-icon size="25" color="#757575">
            <Add />
          </n-icon>
          新建文件夹
        </div>
        <div v-if="isCreatingFolder == true" class="create-folder">
          <n-input v-if="isCreatingFolder == true" type="text" size="medium" class="input" v-model:value="newFolderName"
            maxlength="10" clearable show-count :autofocus="true" :on-blur="closeCreateFolder">
            <template #suffix>
              <n-button strong secondary @click="creatFolder" class="creat-folder-btn">
                新建
              </n-button>
            </template>
          </n-input>
        </div>
        <div class="commit-btn-container">
          <n-button :disabled="favouriteObj.folder == null" strong secondary round type="primary" class="commit-btn"
            @click="commitAddFavourite">
            确定
          </n-button>
        </div>

      </n-form>
    </n-scrollbar>

  </div>
</template>

<style scoped>
::v-deep .n-space {
  display: block !important;
}

.n-radio {
  --n-radio-size: 20px !important;
  display: flex;
}

::v-deep .n-radio__dot {
  border-radius: 0% !important;
}


::v-deep .n-form-item {
  --n-label-height: 0px !important;
  --n-feedback-height: 0px !important;
}

.radio-item {
  font-size: 17px !important;
  font-weight: lighter;
  margin-bottom: 10px;
}

.add-folder-btn {
  width: 340px;
  height: 30px;
  background-color: transparent;
  text-align: left;
  border: 3px solid rgba(219, 219, 219, 0.9);
  display: flex;
  align-items: center;
}


.create-folder {
  display: flex;
  border: 1px solid rgb(224, 224, 230)
}

::v-deep .n-input {
  --n-border: 0px;
  border-radius: 0%;
}

::v-deep .n-input__border:hover {
  --n-border: 1px solid rgb(224, 224, 230) border-radius: 0%;
}

::v-deep .n-button {
  border-left: 1px solid rgb(224, 224, 230);
  border-radius: 0%;
}


.commit-btn-container {
  display: flex;
  justify-content: center;
  padding: 10px;
}

.commit-btn {
  width: 200px;
}
</style>
