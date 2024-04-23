<script setup>
const props = defineProps(['comment-info'])
</script>

<template>
    <div>
        <div class="container">
            <div class="userinfo">
                <div>
                    <img :src=props.commentInfo.avatar alt="">
                </div>
                <div>
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
</style>
