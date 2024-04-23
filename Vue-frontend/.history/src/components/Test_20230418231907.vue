

<script setup>
import { defineComponent, ref } from "vue";

const token = localStorage.getItem('token');
const previewImageUrlRef = ref("");

function handlePreview(file) {

}

const handleFinish = () => {
  console.log('success')
}

</script>

<template>
  <n-upload action="http://127.0.0.1:5000/upload/avatar" :headers="{
    'Authorization': `Bearer ${token}`
  }" show-file-list="false" @preview="handlePreview" @finish="handleFinish"  class="xxx"/>



<n-upload action="http://127.0.0.1:5000/upload/avatar" :headers="{
    'Authorization': `Bearer ${token}`
  }" show-file-list="false" @preview="handlePreview" @finish="handleFinish"  class="xxx">
    <n-upload-dragger>
      <div style="margin-bottom: 12px">
        <n-icon size="48" :depth="3">
          <archive-icon />
        </n-icon>
      </div>
      <n-text style="font-size: 16px">
        点击或者拖动文件到该区域来上传
      </n-text>
      <n-p depth="3" style="margin: 8px 0 0 0">
        请不要上传敏感数据，比如你的银行卡号和密码，信用卡号有效期和安全码
      </n-p>
    </n-upload-dragger>
  </n-upload>
</template>


<style scoped>
.xxx{
  height: 200px;
  width: 200px;
}
</style>

