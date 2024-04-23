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
                <div class="rating">
                    <n-rate readonly :default-value=props.commentInfo.rate/2 size="small" />
                </div>
                <div class="rating">
                {{ props.commentInfo.created_time }}
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
    margin-right: 5px;
    margin-bottom: 5px;
}

.username{
    font-size: 25px;
}
.avatar img{
    height: 50px;
    width: 50px;
    border-radius: 50%;
}

.rating{
    padding-bottom: 7px;
}

.n-rate .n-rate__item:not(:first-child){
    margin-left:1px
}
</style>
