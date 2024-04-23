<script setup>
import { defineProps, computed, ref } from 'vue';
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'

const props = defineProps(['user-info'])
const avatar = props.userInfo.avatar
</script>

<template>
    <div class="edit-container">
        <n-popover trigger="hover" :show-arrow="false">
            <template #trigger>
            <n-upload directory-dnd action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f" class="upload-container">
                <div class="dragger-container">
                    <img :src=avatar alt="" class="edit-avatar">
                    <n-upload-dragger class="avatar-upload-dragger">
                    </n-upload-dragger>
                </div>
            </n-upload>

            </template>

            <span>点击可以更换头像</span>
        </n-popover>


        <n-form ref="formRef" :label-width="80">
            <div class="form-item-container">
                <div class="form-item-label">性别</div>
                <n-radio-group name="radiogroup1" class="form-input">
                    <n-space>
                        <n-radio value="Radio 1">
                            男
                        </n-radio>
                        <n-radio value="Radio 2">
                            女
                        </n-radio>
                        <n-radio value="Radio 3">
                            未知
                        </n-radio>
                    </n-space>
                </n-radio-group>
            </div>

            <div class="form-item-container">
                <div class="form-item-label">生日</div>
                <n-form-item path="datetimeValue">
                    <n-date-picker type="date" class="form-input picker" />
                </n-form-item>
            </div>

            <div class="form-item-container">
                <div class="form-item-label">手机号</div>
                <n-input placeholder="手机号" class="form-input" />
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
                <n-input placeholder="邮箱" class="form-input" />
            </div>

            <div class="form-item-container">
                <n-button strong secondary type="primary" class="commit-btn">
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

.upload-container {
    display: flex;
    justify-content: center;
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
