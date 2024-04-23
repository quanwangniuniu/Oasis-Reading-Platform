<script setup>

</script>

<template>
    <div class="leftbar-container">
        <div class="card">
            <router-link to='/admin/books/add'>图书管理</router-link>
        </div>
        <div class="card">
            <router-link to='/admin/books/edit'>影视管理</router-link>
        </div>
        <div class="card">
            数据分析
        </div>
    </div>
 
</template>

<style scoped>
.leftbar-container{
    width: 250px;
    height: 600px;
}

.card{
    width: 200px;
    height: 50px;
    background: white;
    /* 设置卡片阴影 */
    box-shadow: 0px 1px 3px 2px rgb(214, 214, 214);
    /* 开启flex布局 文字水平垂直居中 */
    display: flex;  
    justify-content: center;
    align-items:center;
    margin-bottom: 10px;
}

.card:hover{
    transform:scale(1.1);
}
</style>
