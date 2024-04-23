

<script setup>
import { defineComponent, ref } from "vue";

const token = localStorage.getItem('token');
const previewImageUrlRef = ref("");

function handlePreview(file) {
      const { url } = file;
      previewImageUrlRef.value = url;
      console.log(previewImageUrlRef)
    }

const handleFinish = (file) => {
  previewImageUrlRef.value = file.file.fullPath;
  console.log(file.file.fullPath)
}

</script>

<template>

  <n-upload action="http://127.0.0.1:5000/upload/avatar" :headers="{
    'Authorization': `Bearer ${token}`
  }" :show-file-list="false" @preview="handlePreview" @finish="handleFinish" class="xxx">
    <n-upload-dragger>
      <img :src="previewImageUrlRef" alt="" class="avatar">
    </n-upload-dragger>
  </n-upload>
</template>


<style scoped>
.avatar {
  height: 200px;
  width: 200px;
}
</style>

