<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { api_login } from '../../axios/api'
import { PersonOutline } from '@vicons/ionicons5'

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
      <div class="caption">注册</div>

      <n-input placeholder="搜索">
        <template #prefix>
          <n-icon :component="PersonOutline" />
        </template>
      </n-input>
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
  height: 400px;
  width: 300px;
  padding: 30px;
  background-color: white;
  box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.caption{
  font-size: 25px;
  font-family: siyuansongti;
}
</style>
