<script setup>
import { defineProps, computed, ref } from 'vue';
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
            <n-form-item label="Datetime" path="datetimeValue">
                <n-date-picker v-model:value="" type="datetime" />
            </n-form-item>
            <n-form-item label="电话号码" path="phone">
                <n-input placeholder="电话号码" />
            </n-form-item>
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
