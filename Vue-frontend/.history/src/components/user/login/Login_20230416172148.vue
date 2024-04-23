<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { api_login } from '../../axios/api'
import { PersonOutline, LockClosedOutline, PhonePortraitOutline, ChatboxEllipsesOutline } from '@vicons/ionicons5'

// 动态绑定用户名和密码
let username = ref()
let password = ref()
const router = useRouter();

let login = () => {
  api_login(username.value, password.value).then(res => {
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
</script>

<template>
  <div class="login-card">
    <div class="login-container">
      <div class="caption">登录</div>
      <n-input placeholder="手机号" class="input">
        <template #prefix>
          <n-icon :component="PhonePortraitOutline" color="black" />
        </template>
      </n-input>

      <n-input placeholder="验证码" class="input">
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
  width: 500px;
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

.agreement{
  color: #517E55;
}
</style>
