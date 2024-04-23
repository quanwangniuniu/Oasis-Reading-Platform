<script setup>
</script>

<template>
    <div>
        <div class="container">
            <div class="nav"><router-link to="/explore">发现</router-link></div>
            <div class="nav"><router-link to="/books">图书</router-link></div>
            <div class="nav"><router-link to="/movies">影视</router-link></div>
            <div class="nav login"><router-link to="/login">登录/注册</router-link></div>
        </div>        
    </div>

</template>

<style scoped>
.container{
    height: 80px;
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
    width: 50px;
    height: 80px;
    margin-left: 20px;
    margin-right: 20px;
    /* 设置nav内部a标签水平居中 */
    text-align: center;
    /* 开启flex局部 */
    display: flex;
    /* 设置nav内部a标签垂直居中 */
    align-items: center;
}

.nav a{
    width: 50px;
    /* 清除a标签默认样式 */
    text-decoration: none;
    color: black;
}

.nav a:hover{
    width: 50px;
    /* 清除a标签默认样式 */
    text-decoration: none;
    color: rgb(2, 108, 2);
}

.nav:hover{
    border: 5px solid rgb(2, 108, 2);
}
.login{
    width: 120px;
    background-color: rgb(61, 61, 61);
}

.login a{
    width: 1200px;
    color: white;
}


</style>
