<script setup>
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { api_login } from '../../axios/api'
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'
import { useMessage } from 'naive-ui'
import {validatePhone} from '../../../util/validate'


import 'animate.css';
const formRef = ref(null);

const router = useRouter();
const message = useMessage()
//用户协议是否已勾选
const agreementChecked = ref(false)
//登录方式选择
const isMessageLogin = ref(true);


const error = () => {
  message.error('用户名不存在或密码错误')
}

//登录表单
const loginForm = ref({
  phone: '',
  password: ''
})

const rules = {
  password: [
    {
      required: true,
      message: '密码不能为空',
      trigger: ["blur"],
    }
  ],
  phone:[
    {
      required: true,
      validator: validatePhone,
      trigger:["input", "blur"]
    }
  ],
};

const LoginButtonClick = () => {
  formRef.value?.validate((errors) => {
    if (!errors) {
      login()
    }
  }) 
}

const login = () => {
  if (agreementChecked.value === false) {
    message.info("请先阅读用户协议")
  } else {
    api_login(loginForm.value.phone, loginForm.value.password).then(res => {
      if (res.data.code == 200) {
        message.success('登录成功')
        //获取后端返回的token, 存到localstoreage里
        const token = res.data.data.token
        const type = res.data.data.type
        localStorage.setItem('type', type)
        localStorage.setItem('token', token)
        if (type == 1) {
          router.push('/books')
        } else {
          router.push('/admin/managebooks/add')
        }
      } else if(res.data.code == 300 || res.data.code == 400){
        message.error(res.data.msg)
        loginForm.value.password = ''
      }
    })
  }

}


const LoginByMessage = () => {
  if (isMessageLogin.value === false) {
    console.log('xxx')
    loginForm.value.phone = ''
    loginForm.value.password = ''
  }
  isMessageLogin.value = true;
}

const LoginByPassword = () => {
  if (isMessageLogin.value === true) {
    loginForm.value.phone = ''
    loginForm.value.password = ''
  }
  isMessageLogin.value = false;
}
</script>

<template>
  <div class="login-card">
    <div class="login-container">
      <div class="caption">
        <button @click="LoginByMessage()" :class="{ notActive: !isMessageLogin }">短信登录</button>
        <button @click="LoginByPassword()" :class="{ notActive: isMessageLogin }">密码登录</button>
      </div>


      <div v-if="isMessageLogin">
        <n-form >
          <n-form-item label="手机号">
            <n-input placeholder="手机号" class="input" disabled>
              <template #prefix>
                <n-icon :component="PersonOutline" color="black" />
              </template>
            </n-input>
          </n-form-item>

          <n-form-item label="验证码">
            <n-input placeholder="验证码" type="password" disabled>
              <template #prefix>
                <n-icon :component="LockClosedOutline" color="black" />
              </template>
            </n-input>
          </n-form-item>
        </n-form>
        <n-checkbox class="input" disabled>
          我已阅读并同意<a class="agreement">用户协议</a>、<a class="agreement">隐私协议</a>、
        </n-checkbox>
        <button class="commit-register-btn" disabled>登录</button>
      </div>


      <div v-if="!isMessageLogin">
        <n-form ref="formRef" :model="loginForm" :rules="rules">
          <n-form-item path="phone" label="手机号">
            <n-input placeholder="手机号" class="input" v-model:value="loginForm.phone">
              <template #prefix>
                <n-icon :component="PersonOutline" color="black" />
              </template>
            </n-input>
          </n-form-item>

          <n-form-item path="password" label="密码">
            <n-input placeholder="密码" type="password" class="input" v-model:value="loginForm.password">
              <template #prefix>
                <n-icon :component="LockClosedOutline" color="black" />
              </template>
            </n-input>
          </n-form-item>
        </n-form>
        <n-checkbox class="input" v-model:checked="agreementChecked">
          我已阅读并同意<a class="agreement">用户协议</a>、<a class="agreement">隐私协议</a>、
        </n-checkbox>
        <button class="commit-register-btn" @click="LoginButtonClick()">登录</button>
      </div>
    </div>

  </div>
</template>

<style scoped>
.login-card {
  margin: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  height: 300px;
  width: 300px;
  padding: 30px;
  background-color: white;
  box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
  display: flex;
  flex-direction: column;
}

.caption {
  font-size: 25px;
  margin-bottom: 20px;
  font-family: siyuansongti;
  text-align: center;
  display: flex;
  justify-content: space-evenly;
}

.commit-register-btn {
  margin-top: 10px;
  width: 100%;
  height: 35px;

  border: 0px;
  color: white;
  background-color: #517E55;
}

.agreement {
  color: #517E55;
}

.caption button {
  font-size: 25px;
  border: none;
  background-color: transparent;
  font-family: siyuansongti;
}

.notActive {
  color: rgb(176, 176, 176);
}
</style>
