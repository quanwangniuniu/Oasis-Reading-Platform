<script setup >
import { ref } from 'vue'

const filelist = ref([])
const dialogImageUrl = ref()
const dialogVisible = ref()
const fileParam = ref()

const handleRemove = (file, fileList) => {
  console.log(file, fileList);
}

const handlePictureCardPreview = (file) => {
  dialogImageUrl.value = file.url;
  dialogVisible.value = true;
  console.log(file)
}

const handleChange = (file, fileList) => {
  fileParam = new FormData(); //创建form对象
  fileParam.append("file", file["raw"]);
  fileParam.append("fileName", file["name"]);
}

const handleClick = () => {
  axios
      .post("http://127.0.0.1:5000/save-picture/", this.fileParam)
      .then((response) => {
          console.log(response);
          this.fileList = [];
      })
      .catch((e) => {
          console.log(e);
      });
}

</script>

<template>

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
