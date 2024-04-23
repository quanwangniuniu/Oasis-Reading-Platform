<script setup>
const props = defineProps(['comment-info'])
</script>

<template>
    <div>
        <div class="container">
            <div class="userinfo">
                <div class="avatar">
                    <img :src=props.commentInfo.avatar alt="">
                </div>
                <div class="username">
                    {{ props.commentInfo.username }}
                </div>
            </div>
            <div class="">
                {{ props.commentInfo.comment }}
            </div>
        </div>        
    </div>

 
</template>

<style scoped>
.container{
    height: 200px;
    background-color: red;
}

.avatar img{
    height: 70px;
    width: 70px;
    border-radius: 50%;
}
</style>
