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
    padding: 10px;
}
.userinfo{
    display: flex;
}

.userinfo div{
    display: flex;
    flex-direction: column;
    justify-content: end;
}

.username{
    font-size: 30px;
}
.avatar img{
    height: 50px;
    width: 50px;
    border-radius: 50%;
}
</style>
