<script setup>
  import axios from 'axios'
  import {ref} from 'vue'
  import { useRouter } from "vue-router";
  import {api_login} from '../../axios/api'
  
  // 动态绑定用户名和密码
  let username = ref()
  let password = ref()
  const router = useRouter();

  let login = () => {
    api_login(username.value, password.value).then(res=>{
      if(res.data.code == 0){
        //获取后端返回的token, 存到localstoreage里
        const token = res.data.data.token
        const type = res.data.data.type
        localStorage.setItem('type', type)
        localStorage.setItem('token', token)
        if(type == 1){
          router.push('/explore')          
        }else{
          router.push('/admin/books/add') 
        }

      }
    })
  }
</script>

<template>
  <div class="container">
      账号:<input type="text" v-model="username"><br>
      密码:<input type="password" v-model="password"><br>
      <button @click="login">登录</button>
  </div>
 
</template>

<style scoped>
.container{
  margin: 50px 50px -30px 50px;
  display: flex;
  justify-content: space-between;
  background-color: red;
}
</style>
