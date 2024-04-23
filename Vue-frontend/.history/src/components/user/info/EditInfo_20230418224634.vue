<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';

const props = defineProps(['user'])
const userInfo = ref(props.user)
let token = localStorage.getItem('token');

onBeforeMount(() => {
    console.log('uuu')
    console.log(props.user)
    userInfo.value.gender = String(userInfo.value.gender)
    console.log(userInfo)
})

const handlePreview = (file) => {
    // const { url } = file;
    // userInfo.value.avatar = url;
}

const commit = () => {
    console.log(userInfo.value)
}

</script>

<template>
    <div class="edit-container">
        <n-popover trigger="hover" :show-arrow="false">
            <template #trigger>
                <div>
                    <el-upload
                    class="upload-container"
                        action="http://127.0.0.1:5000/uploadCover"
                        :show-file-list="false"
                        :on-success="handleAvatarSuccess"
                        :before-upload="beforeAvatarUpload"
                    >
                    <div class="dragger-container">

                    </div>
                        <img :src=userInfo.avatar alt="" class="edit-avatar">   
                    </el-upload>
                    
                    <!-- <n-upload 
                        action="http://127.0.0.1:5000/upload/avatar" 
                        preset="card" 
                        :headers="{
                            'Authorization': `Bearer ${token}`
                        }" 
                        @preview="handlePreview" 
                        class="upload-container">
                        <div class="dragger-container">
                            <img :src=userInfo.avatar alt="" class="edit-avatar">
                            <n-upload-dragger class="avatar-upload-dragger">
                            </n-upload-dragger>
                        </div>
                    </n-upload>                     -->
                </div>
            </template>

            <span>点击可以更换头像</span>
        </n-popover>


        <n-form :model="userInfo" :label-width="80">
            <div class="form-item-container">
                <div class="form-item-label">性别</div>
                <n-radio-group name="radiogroup1" class="form-input" v-model:value="userInfo.gender">
                    <n-space>
                        <n-radio value="1">
                            男
                        </n-radio>
                        <n-radio value="2">
                            女
                        </n-radio>
                        <n-radio value="0">
                            未知
                        </n-radio>
                    </n-space>
                </n-radio-group>
            </div>

            <div class="form-item-container">
                <div class="form-item-label">生日</div>
                <n-form-item path="datetimeValue">
                    <n-date-picker type="date" class="form-input picker" v-model:value="userInfo.birthday" />
                </n-form-item>
            </div>

            <div class="form-item-container">
                <div class="form-item-label">手机号</div>
                <n-input placeholder="手机号" class="form-input" v-model:value="userInfo.phone" />
            </div>

            <div class="form-item-container">
                <div class="form-item-label">验证码</div>
                <n-input placeholder="验证码" class="form-input">
                    <template #suffix>
                        <div>发送验证码</div>
                    </template>
                </n-input>
            </div>

            <div class="form-item-container">
                <div class="form-item-label">邮箱</div>
                <n-input placeholder="邮箱" class="form-input" v-model:value="userInfo.email" />
            </div>

            <div class="form-item-container">
                <n-button strong secondary type="primary" class="commit-btn" @click="commit()">
                    提交
                </n-button>
            </div>
        </n-form>
    </div>
</template>

<style scoped>
.edit-container {
    width: 300px;
    height: 500px;
}

.upload-container{
    display: flex;
    justify-content: center;
}

.el-upload{
    height: 150px !important;
}

.edit-avatar {
    height: 150px;
    width: 150px;
    border-radius: 50%;
}

.dragger-container {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    position: relative;
    margin-bottom: 20px;
    /* display: flex;
    justify-content: center;
    position: relative; */
}

.avatar-upload-dragger {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    position: absolute;
    padding: 0px;
    top: 0;
    left: 0;
    z-index: 1;
    background-color: rgba(255, 255, 255, 0.5);

}

.form-item-container {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.form-item-label {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-right: 5px;
    width: 50px;
}

.form-input {
    width: 300px;
    display: flex;
    justify-content: center;
}

.picker {
    margin: 0px;
}

.n-form-item.n-form-item--top-labelled {
    grid-template-areas: none;
    grid-template-rows: none;
    grid-template-columns: none;
}

.commit-btn {
    width: 375px;
}
</style>
