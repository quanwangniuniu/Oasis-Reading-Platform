<script setup>
import { computed } from 'vue'
const props = defineProps(['comment-info'])

//计算属性, 将数据库中的时间戳转换为yyyy-mm-dd格式的字符串
const created_time = computed(() => {
  let timestamp = props.commentInfo.created_time;
  const date = new Date(timestamp);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  const formattedDate = `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`; // 格式化为年月日字符串，注意月份和日期需要补零
  return formattedDate
})
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
                    <n-rate allow-half readonly :default-value=props.commentInfo.rate/2 size="small" />
                </div>
                <div class="time">
                {{ created_time }}
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
    margin-bottom: 15px;
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
.time{
    padding-bottom: 3px;
    color: grey;
}
</style>
