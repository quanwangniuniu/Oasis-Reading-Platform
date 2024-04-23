<script setup >
import { ref } from 'vue'

const filelist = ref([])
const dialogImageUrl = ref('')
const dialogVisible = ref()

const handleRemove = (file, fileList) => {
  console.log(file, fileList);
}

const handlePictureCardPreview = (file) => {
  dialogImageUrl.value = file.url;
  dialogVisible.value = true;
  console.log(file)
}
</script>

<template>
  作者：蜗牛
  链接：https://zhuanlan.zhihu.com/p/476017031
  来源：知乎
  著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

  <div>
    <el-upload 
      v-model="fileList" 
      ref="uploadref" 
      action="#" 
      :auto-upload="false" 
      list-type="picture-card"
      :file-list="fileList" 
      :limit="1" 
      :on-change="handleChange" 
      :on-preview="handlePictureCardPreview"
      :on-remove="handleRemove">
      <i class="el-icon-plus"></i>
    </el-upload>
    <el-dialog v-model="dialogVisible">
      <img width="100%" :src="dialogImageUrl" alt="" />
    </el-dialog>
    <button @click="handleClick">点我保存图片</button>
  </div>
</template>


<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>
