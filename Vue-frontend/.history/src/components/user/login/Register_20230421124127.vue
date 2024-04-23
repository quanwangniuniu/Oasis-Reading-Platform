<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { api_addUser } from '../../axios/user_api'
import { api_login } from '../../axios/api'
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'

const phoneRegEx = new RegExp("^1[3456789]\\d{9}$");
const usernameRegEx = new RegExp("^[\\u4E00-\\u9FA5A-Za-z0-9]+$")
const codeRegEx = new RegExp("^\\d{4}$")

const router = useRouter();
const rPasswordFormItemRef = ref(null);
const formRef = ref(null);

//注册表单
const registerForm = ref({
  username: '',
  password: '',
  reenteredPassword: '',
  phone: '',
  code: '',
})

const validatePasswordStartWith = (rule, value) => {
  return !!registerForm.value.password && registerForm.value.password.startsWith(value) && modelRef.value.password.length >= value.length;
}

const validatePasswordSame = (rule, value) => {
  return value === registerForm.value.password;
}

const validatePhone = (rule, value) => {
  if(!phoneRegEx.test(value)){
    return new Error("手机号格式不正确");
  }else{
    return true
  }
}

const validateUsername = (rule, value) => {
  if(!usernameRegEx.test(value)){
    return new Error("用户名不能包含特殊字符");
  }else{
    return true
  }
}

const validateCode = (rule, value) => {
  if(!code.test(value)){
    return new Error("验证码为四位数字");
  }else{
    return true
  }
}

const rules = {
  username: [
    {
      required: true,
      message: "用户名不能包含特殊字符",
      trigger: ["input", "blur"],
      validator: validateUsername
    },
  ],
  password: [
    {
      required: true,
      message: "请输入密码",
      trigger: ["blur"],
    }
  ],
  reenteredPassword: [
    {
      required: true,
      message: "请再次输入密码",
      trigger: ["input", "blur"]
    },
    {
      validator: validatePasswordStartWith,
      message: "两次密码输入不一致",
      trigger: "input"
    },
    {
      validator: validatePasswordSame,
      message: "两次密码输入不一致",
      trigger: ["blur", "password-input"]
    }
  ],
  phone:[
    {
      required: true,
      message:'手机号格式不正确',
      validator: validatePhone,
      trigger:["input", "blur"]
    }
  ]
};

const handlePasswordInput = () => {
  if (registerForm.value.reenteredPassword) {
    rPasswordFormItemRef.value?.validate({ trigger: "password-input" });
  }
}

//注册函数
let register = () => {
  api_addUser(registerForm.value).then((res) => {
    if (res.data.code === 200) {
      console.log(res)
      api_login(registerForm.value.username, registerForm.value.password).then(res => {
        if (res.data.code == 0) {
          //获取后端返回的token, 存到localstoreage里
          const token = res.data.data.token
          const type = res.data.data.type
          localStorage.setItem('type', type)
          localStorage.setItem('token', token)
          if (type == 1) {
            router.push('/explore')
          } else {
            router.push('/admin/books/add')
          }
        }
      })
    }
  })
}
</script>

<template>
  <div class="login-card">
    <div class="login-container">
      <div class="caption">注册</div>

      <n-form ref="formRef" :model="registerForm" :rules="rules">
        <n-form-item path="username" label="用户名">
          <n-input 
            placeholder="请输入用户名" 
            class="input" 
            v-model:value="registerForm.username"
          >
            <template #prefix>
              <n-icon :component="PersonOutline" color="black" />
            </template>
          </n-input>  
        </n-form-item>

        <n-form-item path="password" label="密码">
          <n-input 
            placeholder="请输入密码" 
            type="password" 
            class="input" 
            @input="handlePasswordInput"
            v-model:value="registerForm.password"
          >
            <template #prefix>
              <n-icon :component="LockClosedOutline" color="black" />
            </template>
          </n-input>
        </n-form-item>
    
        <n-form-item ref="rPasswordFormItemRef" path="reenteredPassword" label="确认密码">
          <n-input 
            placeholder="请再次输入密码" 
            type="password" 
            class="input" 
            v-model:value="registerForm.reenteredPassword"
          >
            <template #prefix>
              <n-icon :component="LockClosedOutline" color="black" />
            </template>
          </n-input>          
        </n-form-item>
      
        <n-form-item path="phone" label="手机号">
          <n-input 
            placeholder="请输入手机号" 
            class="input" 
            v-model:value="registerForm.phone"
          >
            <template #prefix>
              <n-icon :component="PhonePortraitOutline" color="black" />
            </template>
          </n-input>
        </n-form-item>

        <n-form-item path="code" label="验证码">
          <n-input 
            placeholder="验证码" 
            class="input"
            v-model:value="registerForm.code"
          >
            <template #prefix>
              <n-icon :component="ChatboxEllipsesOutline" color="black" />
            </template>

            <template #suffix>
              <div>发送验证码</div>
            </template>
          </n-input>
        </n-form-item>
      
      </n-form>
      <n-checkbox class="input">
        我已阅读并同意<a class="agreement">用户协议</a>、<a class="agreement">隐私协议</a>、
      </n-checkbox>
      <button class="commit-register-btn" @click="register()">注册</button>
    </div>

  </div>
</template>

<style scoped>
.login-card {
  margin: 100px;
  margin-top: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  height: 550px;
  width: 350px;
  padding: 30px;
  background-color: white;
  box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
  display: flex;
  flex-direction: column;
}

.caption {
  font-size: 25px;
  margin-bottom: 10px;
  font-family: siyuansongti;
  text-align: center;
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
</style>
