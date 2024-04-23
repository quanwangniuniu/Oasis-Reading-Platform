<script setup>
</script>

<template>
    <div>
        <div class="container">
            <div class="nav"><router-link to="/explore">发现</router-link></div>
            <div class="nav"><router-link to="/books">图书</router-link></div>
            <div class="nav"><router-link to="/movies">影视</router-link></div>
            <div class="login"><router-link to="/login">登录</router-link></div>
            <div class="register"><router-link to="/login">注册</router-link></div>
        </div>        
    </div>

</template>

<style scoped>
.container{
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

.nav{
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

.nav a{
    width: 50px;
    /* 清除a标签默认样式 */
    text-decoration: none;
    color: black;
}

.nav:hover{
    border-bottom: 2px solid rgb(2, 108, 2);
    color: rgb(2, 108, 2);
}

.nav:hover a{
    color: rgb(2, 108, 2);
}


.login{
    box-sizing: border-box;
    padding-left: 20px;
    padding-right: 20px;
    background-color: rgb(61, 61, 61);
}


</style>
