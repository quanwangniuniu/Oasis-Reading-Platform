<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['comment'])
const commentObj = ref(props.comment)

const showModal = ref(false)


//计算属性, 将数据库中的时间戳转换为yyyy-mm-dd格式的字符串
const created_time = computed(() => {
  let timestamp = commentObj.value.created_time;
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
      <div class="img-container"><img :src="commentObj.url" alt=""></div>
      <div class="comment-container">
        <div class="comment-info">
          <div class="title">
            {{ commentObj.title }}
          </div>
          <div class="rating">
            <n-rate readonly :default-value=commentObj.rate/2 size="small" />
          </div>
          <div class="date">
            {{ created_time }}
          </div>
        </div>
        <div class="comment" @click="showModal=true">
          <n-ellipsis style="max-height:60px; max-width: 100%;">
            {{ commentObj.comment }}
          </n-ellipsis>
        </div>
      </div>
    </div>
  </div>



  <n-modal v-model:show="showModal">
    <n-card style="width: 600px" :title=commentObj.title :bordered="false" size="huge" role="dialog" aria-modal="true">
      <n-scrollbar style="max-height:300px">
        <div class="book-desc">
          {{ commentObj.comment }}
        </div>
      </n-scrollbar>

    </n-card>
  </n-modal>
</template>

<style scoped>
.container {
  /* background-color: rgb(158, 246, 155); */
  height: 120px;
  margin-bottom: 15px;
  box-shadow: 0px 0px 2px 2px rgb(214, 214, 214);
}

.container {
  display: flex;
  align-items: center;
}

.img-container,
.img-container img {
  height: 120px;
  width: 75px;
}

.comment-info {
  display: flex;
  margin-left: 10px;
}

.comment-info>div {
  display: flex;
  flex-direction: column;
  justify-content: end;
  margin-right: 5px;
}

.title {
  font-size: 25px;
}

.comment {
  height: 60px;
  margin-left: 10px;
  font-size: 20px;
}

.rating {
  padding-bottom: 10px;
}

.date {
  padding-bottom: 7px;
  color: grey;
}
</style>
