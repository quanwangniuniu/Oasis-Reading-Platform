<script setup>
</script>

<template>
    <div class="edit-container">
        <n-upload directory-dnd action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f">
            <div class="dragger-container">
                <n-upload-dragger class="avatar-upload-dragger">
                    <img :src=userInfo.avatar alt="" class="edit-avatar">
                </n-upload-dragger>
            </div>
        </n-upload>
        <n-form ref="formRef" :label-width="80">
            <n-form-item label="姓名" path="user.name">
                <n-input placeholder="输入姓名" />
            </n-form-item>
            <n-form-item label="年龄" path="user.age">
                <n-input placeholder="输入年龄" />
            </n-form-item>
            <n-form-item label="电话号码" path="phone">
                <n-input placeholder="电话号码" />
            </n-form-item>
            <n-form-item>
                <n-button attr-type="button" @click="handleValidateClick">
                    验证
                </n-button>
            </n-form-item>
        </n-form>
    </div>
</template>

<style scoped>
.edit-container {
  width: 500px;
  height: 500px;
}

.edit-avatar {
  height: 150px;
  width: 150px;
  border-radius: 50%;
}

.dragger-container {
  width: 500px;
  display: flex;
  justify-content: center;
}

.avatar-upload-dragger {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  padding: 0px;
}
</style>
