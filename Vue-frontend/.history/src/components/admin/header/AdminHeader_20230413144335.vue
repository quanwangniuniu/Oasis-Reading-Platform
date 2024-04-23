<script setup>

let logout = () =>{
    localStorage.clear('token')
    localStorage.clear('type')
}

</script>

<template>
    <div>
        <div class="container">
            <div class="left">
                <div class="nav"><router-link to="/books">图书管理</router-link></div>
                <div class="nav"><router-link to="/movies">影视管理</router-link></div>
            </div>

            <div class="right">
                <div class="nav avata"><router-link to="/info">头像</router-link></div>
                <div class="nav login"><router-link to="/explore" @click="logout">登出</router-link></div>
            </div>

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
    justify-content: space-between;
    /* 设置元素垂直居中 */
    align-items: center;
}

.left{
    display: flex;
    /* 设置元素垂直居中 */
    align-items: center;
    padding-left: 50px;
}

.right{
    display: flex;
    /* 设置元素垂直居中 */
    align-items: center;
    padding-right: 50px;
}

.nav{
    width: 80px;
    height: 30px;
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
    width: 80px;
    /* 清除a标签默认样式 */
    text-decoration: none;
    color: black;

}

.login{
    width: 120px;
    background-color: rgb(61, 61, 61);
}

.login a{
    width: 1200px;
    color: white;
}

.avata{
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: rebeccapurple;
}


</style>
