<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import type { UploadProps } from 'element-plus'
import {api_updateUserInfo} from '../../axios/user_api'
import { useRoute, useRouter } from 'vue-router'
import {validatePhone, validateCode, validateEmail} from '../../../util/validate'
import { useMessage } from 'naive-ui'
import {baseURL} from '../../axios/config'

const message = useMessage()
const router = useRouter()
const props = defineProps(['user', 'show'])
const userInfo = ref(props.user)
const formRef = ref(null);

const uploadURL = ref()

const rules = {
  phone:[
    {
      required:true,
      validator: validatePhone,
      trigger:["input", "blur"]
    }
  ],
  code:[
    {
      validator: validateCode,
      trigger:["input", "blur"]
    }
  ],
  email:[
  {
      validator: validateEmail,
      trigger:["input", "blur"]
    }   
  ]
};

onBeforeMount(() => {
  console.log('uuu')
  console.log(props.user)
  userInfo.value.gender = String(userInfo.value.gender)
  console.log(userInfo)
  uploadURL.value = baseURL + '/uploadCover'
  console.log(uploadURL.value)
})

const commit = () => {
  // 如果用户没有设置生日, 设置其为0
  if(!userInfo.value.birthday){
    userInfo.value.birthday = 0
  }

  api_updateUserInfo(userInfo.value).then(res=>{
    if(res.data.code == 200){
      message.success('用户信息编辑成功')
      router.push({path: '/transit', query: {path1:'/info', path2:'/admin/info'}})
    }else if(res.data.code == 300){
      message.error(res.data.msg)
    }
  })
}

const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  console.log(response)
  userInfo.value.avatar = response.url
}


const CommitButtonClick = () => {
  formRef.value?.validate((errors: any) => {
    if (!errors) {
      commit()
    }
  }) 
}

</script>

<template>
  <div class="edit-container">
    <n-popover trigger="hover" :show-arrow="false">
      <template #trigger>
        <div>

          <el-upload
            class="upload-container" 
            :action = "uploadURL" 
            :show-file-list="false"
            :on-success="handleAvatarSuccess">
            <div class="dragger-container">
              <img :src=userInfo.avatar alt="" class="edit-avatar">
            </div>
          </el-upload>
        </div>
      </template>

      <span>点击可以更换头像</span>
    </n-popover>

    <n-form ref="formRef" :model="userInfo" :rules="rules" :label-width="80" label-placement="left">
      <div class="form-item-container">
      <n-form-item path="gender" label="性别">
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
      </n-form-item>        
      </div>
      


      <div class="form-item-container">
        <n-form-item path="date" label="生日">
          <n-date-picker type="date" class="form-input picker" v-model:value="userInfo.birthday" />
        </n-form-item>        
      </div>



      <div class="form-item-container">
        <n-form-item path="phone" label="手机号">
          <n-input placeholder="手机号" class="form-input" v-model:value="userInfo.phone" />
        </n-form-item>        
      </div>

      <div class="form-item-container">
        <n-form-item path="email" label="邮箱">
          <n-input placeholder="邮箱" class="form-input" v-model:value="userInfo.email" />
        </n-form-item>        
      </div>

      <div class="form-item-container">
        <n-form-item path="signature" label="个性签名">
          <n-input placeholder="个性签名" class="form-input" v-model:value="userInfo.signature"/>
        </n-form-item>        
      </div>
    </n-form>
    <div class="form-item-container">
      <n-button strong secondary type="primary" class="commit-btn" @click="CommitButtonClick">
        提交
      </n-button>
    </div>
  </div>
</template>

<style scoped>
.edit-container {
  width: 300px;
  height: 500px;
}

.upload-container {
  height: 150px;
  display: flex;
  justify-content: center;
}

el-upload {
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
  margin-left: 50px;
  width: 200px;
}
</style>
