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
                <div>
                    <n-rate readonly default-value="5" size="small" />
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
    background-color: white;
    padding: 10px;
    box-shadow: 0px 1px 8px 2px rgb(214, 214, 214);
}
.userinfo{
    display: flex;
}

.userinfo > div{
    display: flex;
    flex-direction: column;
    justify-content: end;
}

.username{
    font-size: 25px;
}
.avatar img{
    height: 50px;
    width: 50px;
    border-radius: 50%;
    margin-right: 5px;
}
</style>
