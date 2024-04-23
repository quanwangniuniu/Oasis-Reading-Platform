<script setup>
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { api_login } from '../../axios/api'
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'
import { useMessage } from 'naive-ui'

const router = useRouter();
const message = useMessage()

const info = () => {
  message.info(
    "请先阅读用户协议",
    {
      keepAliveOnHover: true
    }
  )
}

//登录方式选择
const isMessageLogin = ref(true);

//登录表单
const loginForm = ref({
  username: '',
  password: ''
})


const login = () => {

  api_login(loginForm.value.username, loginForm.value.password).then(res => {
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


const LoginByMessage = () => {
  if (isMessageLogin === false) {
    loginForm.username.value = ''
    loginForm.password.value = ''
  }
  isMessageLogin.value = true;
}

const LoginByPassword = () => {
  if (isMessageLogin === true) {
    loginForm.username.value = ''
    loginForm.password.value = ''
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
        <n-input placeholder="手机号" class="input" v-model:value="loginForm.username">
          <template #prefix>
            <n-icon :component="PhonePortraitOutline" color="black" />
          </template>
        </n-input>

        <n-input placeholder="验证码" class="input" v-model:value="loginForm.username">
          <template #prefix>
            <n-icon :component="ChatboxEllipsesOutline" color="black" />
          </template>

          <template #suffix>
            <div>发送验证码</div>
          </template>
        </n-input>
        <n-checkbox class="input">
          我已阅读并同意<a class="agreement">用户协议</a>、<a class="agreement">隐私协议</a>、
        </n-checkbox>
        <button class="commit-register-btn">注册</button>
      </div>

      <div v-if="!isMessageLogin">
        <n-input placeholder="账号" class="input" v-model:value="loginForm.username">
          <template #prefix>
            <n-icon :component="PersonOutline" color="black" />
          </template>
        </n-input>

        <n-input placeholder="密码" class="input" v-model:value="loginForm.password">
          <template #prefix>
            <n-icon :component="LockClosedOutline" color="black" />
          </template>
        </n-input>
        <n-checkbox class="input">
          我已阅读并同意<a class="agreement">用户协议</a>、<a class="agreement">隐私协议</a>、
        </n-checkbox>
        <button class="commit-register-btn" @click="login()">登录</button>
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
  height: 250px;
  width: 300px;
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
  display: flex;
  justify-content: space-evenly;
}

.input {
  margin: 10px 0px;
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
