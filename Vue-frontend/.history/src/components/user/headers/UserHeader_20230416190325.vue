<script setup>
let logout = () => {
  localStorage.clear('token')
  localStorage.clear('type')
}

</script>

<template>
  <div>
    <div class="container">
      <div class="avata">头像</div>
      <div class="nav"><router-link to="/explore">发现</router-link></div>
      <div class="nav"><router-link to="/books">图书</router-link></div>
      <div class="nav"><router-link to="/movies">影视</router-link></div>
      <div class="login"><router-link to="/explore" @click="logout">登出</router-link></div>
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

.avata{
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
</style>
