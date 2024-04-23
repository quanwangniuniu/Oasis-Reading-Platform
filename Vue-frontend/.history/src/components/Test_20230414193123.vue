<template>
  <n-radio-group
    name="left-size"
    style="margin-bottom: 12px"
  >
    <n-radio-button value="small">
      小
    </n-radio-button>
    <n-radio-button value="medium">
      中
    </n-radio-button>
    <n-radio-button value="large">
      大
    </n-radio-button>
  </n-radio-group>
  <n-form
    ref="formRef"
    inline
    :label-width="80"
    :model="formValue"
  >
    <n-form-item label="姓名" path="user.name">
      <n-input v-model:value="formValue.user.name" placeholder="输入姓名" />
    </n-form-item>
    <n-form-item label="年龄" path="user.age">
      <n-input v-model:value="formValue.user.age" placeholder="输入年龄" />
    </n-form-item>
    <n-form-item label="电话号码" path="phone">
      <n-input v-model:value="formValue.phone" placeholder="电话号码" />
    </n-form-item>
    <n-form-item>
      <n-button attr-type="button">
        验证
      </n-button>
    </n-form-item>
  </n-form>

  <pre>{{ JSON.stringify(formValue, null, 2) }}
</pre>
</template>

<script setup lang="ts">
import { defineComponent, ref } from 'vue'
import { FormInst, useMessage } from 'naive-ui'

const formValue = ref({
        user: {
          name: '',
          age: ''
        },
        phone: ''
      })

</script>
<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

