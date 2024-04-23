<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['book-info'])
const userType = ref(localStorage.getItem('type'))

</script>

<template>
    <div class="card-container">
        <div class="img">
            <img :src=props.bookInfo.url alt="">
        </div>

        <div class="content">
            <div class="title">
                <router-link v-if="userType == 2" :to="'/admin/books/' + props.bookInfo.id" class="name">{{ props.bookInfo.title }}</router-link>
                <router-link v-if="userType != 2" :to="'/books/' + props.bookInfo.id" class="name">{{ props.bookInfo.title }}</router-link>
                <p class="author">{{ props.bookInfo.author }}</p>
            </div>

            <div class="description">
                {{ props.bookInfo.description }}
            </div> 
        </div>
    </div>
</template>

<style scoped>
.card-container{
    width:300px;
    height: 150px;
    background-color: white;
    padding: 15px;
    box-shadow: 0px 1px 8px 2px rgb(214, 214, 214);  /*左边阴影(h-shadow为负数，v-shadow为0为左边阴影)  绿色*/
    display: flex;
}

.img{
    height: 150px;
    width: 90px;
}

.img img{
    height: 150px;
    width: 90px;
    object-fit: fill;
}

.content{
    margin-left: 10px;
    height: 100%;
    width: 100%;
}

.name{
    text-decoration: none;
    color: black;
    font-size: 20px;
}

.author{
    font-size: 5px;
    color: gray;
}

.title{
    height: 50px;
}

.description{
    width: 100%;
    height: 100px;
	overflow:hidden; 
    font-size: 12px;
    line-height: 20px;
}
</style>
