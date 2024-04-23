<script setup>
import { defineProps, computed, ref } from 'vue';
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'

const props = defineProps(['avatar'])
const avatar = props.avatar
</script>

<template>
    <div class="edit-container">
        <n-upload directory-dnd action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f">
            <div class="dragger-container">
                <n-upload-dragger class="avatar-upload-dragger">
                    <img :src=avatar alt="" class="edit-avatar">
                </n-upload-dragger>
            </div>
        </n-upload>

        <n-form ref="formRef" :label-width="80">
            <div class="form-gender">
                <n-radio-group name="radiogroup1">
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
                    <n-date-picker type="date" class="form-input" />
                </n-form-item>                
            </div>

            <div class="form-item-container">
                <div class="form-item-label">手机号</div>
                <n-input placeholder="手机号" class="form-input"/>            
            </div>

            <n-form-item>
                <n-button attr-type="button">
                    验证
                </n-button>
            </n-form-item>
        </n-form>
    </div>
</template>

<style scoped>
.edit-container {
    width: 300px;
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

.form-item-container{
    display: flex;
    justify-content: center;
    margin-top: 0px;
}

.form-item-label{
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-right: 5px;
}

.form-input{
    width: 200px;
}
</style>
