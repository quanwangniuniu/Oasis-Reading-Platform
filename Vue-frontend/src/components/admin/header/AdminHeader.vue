<script setup>
import { onBeforeMount, ref } from 'vue'
import { api_getUserAvatar } from '../../axios/user_api'
import { useRouter } from 'vue-router'

const router = useRouter()
const avatarURL = ref()

onBeforeMount(() => {
  api_getUserAvatar().then(res => {
    // console.log(res)
    avatarURL.value = res.data.data;
  })
})

let logout = () => {
    localStorage.clear('token')
    localStorage.clear('type')
}

const gotoUserCenter = () => {
  router.push({path:'/admin/info'})
}


</script>

<template>
    <div>
        <div>
            <div class="container">
                <div class="left">
                    <div class="nav"><router-link to="/admin/managebooks/add">图书管理</router-link></div>
                </div>

                <div class="right">
                    <div class="avata" @click="gotoUserCenter()">
                        <img :src=avatarURL alt="">
                    </div>
                    <div class="nav"><router-link to="/admin/info">个人主页</router-link></div>
                    <div class="nav"><router-link to="/admin/books">图书</router-link></div>
                    <div class="nav"><router-link to="/admin/favourites">收藏</router-link></div>
                    <div class="login"><router-link to="/login" @click="logout()">登出</router-link></div>                    
                </div>


            </div>
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

  display: flex;
  justify-content: space-between;
}

.left, .right{
    display: flex;
    align-items: center;
}

.nav {
  box-sizing: border-box;
  width: 90px;
  height: 60px;
  padding-left: 10px;
  padding-right: 10px;
  /* 设置nav内部a标签水平居中 */
  text-align: center;
  /* 开启flex局部 */
  display: flex;
  /* 设置nav内部a标签垂直居中 */
  align-items: center;
  border-bottom: 2px solid transparent;
}

.nav a {
  width: 70px;
  /* 清除a标签默认样式 */
  text-decoration: none;
  color: black;
}

.left .nav{
  margin-left: 10px;
    width: 100px;
}

.left .nav a{
    width: 100px;
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
  margin-right: 20px;
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
