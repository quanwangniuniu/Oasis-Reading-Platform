<script setup>
import { onBeforeMount, ref } from 'vue'
import { api_getUserAvatar } from '../../axios/user_api'

const avatarURL = ref()

onBeforeMount(() => {
  api_getUserAvatar().then(res => {
    console.log(res)
    avatarURL.value = res.data.data;
  })
})


let logout = () => {
  localStorage.clear('token')
  localStorage.clear('type')
}


</script>

<template>
  <div>
    <div class="container">
      <div class="logo">
        <img src="/logo/logo1.jpg" alt="">
      </div>
      <div class="avata">
        <img :src=avatarURL alt="">
      </div>
      <div class="nav"><router-link to="/explore">发现</router-link></div>
      <div class="nav"><router-link to="/books">图书</router-link></div>
      <div class="nav"><router-link to="/movies">影视</router-link></div>
      <div class="login"><router-link to="/explore" @click="logout()">登出</router-link></div>
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 60px;
  background-color: white;
  /* 边框模糊效果 */
  box-shadow: 0 0 5px 5px rgb(214, 214, 214);
  /* 开启flex布局 */
  display: flex;
  /* 设置元素靠右排列 */
  justify-content: flex-end;
  /* 设置元素垂直居中 */
  align-items: center;
}

.nav {
  box-sizing: border-box;
  width: 90px;
  height: 60px;
  padding-left: 20px;
  padding-right: 20px;
  /* 设置nav内部a标签水平居中 */
  text-align: center;
  /* 开启flex局部 */
  display: flex;
  /* 设置nav内部a标签垂直居中 */
  align-items: center;
  border-bottom: 2px solid transparent;
}

.nav a {
  width: 50px;
  /* 清除a标签默认样式 */
  text-decoration: none;
  color: black;
}

.nav:hover {
  border-bottom: 2px solid rgb(2, 108, 2);
  color: rgb(2, 108, 2);
}

.nav:hover a {
  color: rgb(2, 108, 2);
}


.login {
  padding: 5px 15px;
  box-sizing: border-box;
  margin-left: 20px;
  margin-right: 20px;
  background-color: #517E55;
  align-content: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login a {
  display: inline-block;
  line-height: 100%;
  text-align: center;
  text-decoration: none;
  color: white
}

a {
  font-size: 15px;
}

.avata {
  box-sizing: border-box;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
  display: flex;
  justify-content: center;
  align-items: center;
}

.avata img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}


.logo {
  box-sizing: border-box;
  width: 70px;
  height: 45px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 20px;
}

.logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
