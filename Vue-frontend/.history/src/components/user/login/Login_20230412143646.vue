<script setup>
  import axios from 'axios'
  import {ref} from 'vue'
  import { useRouter } from "vue-router";
  
  // 动态绑定用户名和密码
  let username = ref()
  let password = ref()
  const router = useRouter();

  let login = () => {
    axios.post('http://127.0.0.1:5000/login', {
      username: username.value,
      password: password.value
    }).then(res=>{
      if(res.data.code == 0){
        //获取后端返回的token, 存到localstoreage里
        const token = res.data.data.token
        localStorage.setItem('token', token)
        router.push('/explore')
      }
    })
  }
</script>

<template>
  <div>
      账号:<input type="text" v-model="username"><br>
      密码:<input type="password" v-model="password"><br>
      <button @click="login">登录</button>
  </div>
 
</template>

<style scoped>
</style>
