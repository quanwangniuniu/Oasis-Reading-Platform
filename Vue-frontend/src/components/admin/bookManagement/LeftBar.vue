<script setup>

</script>

<template>
    <div class="leftbar-container">
        <div class="card">
            <router-link to='/admin/managebooks/add'>新增图书</router-link>
        </div>
        <div class="card">
            <router-link to='/admin/managebooks/list'>编辑图书</router-link>
        </div>
        <!-- <div class="card">
            <router-link to='/admin/managebooks/analyse'>数据分析</router-link>
        </div> -->
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

a, a:visited {
  text-decoration: none;
  color: #000;
}
</style>
