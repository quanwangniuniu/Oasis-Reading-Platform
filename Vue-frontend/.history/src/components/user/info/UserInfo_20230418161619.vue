<script setup>
import {ref, onBeforeMount} from 'vue'
import {api_getUserInfo} from '../../axios/user_api'

const userInfo = ref({})

onBeforeMount(()=>{
  api_getUserInfo().then((res)=>{
    if(res.data.code == 200){
      userInfo.value = res.data.data      
    }

  })
})
</script>

<template>
  <div>
    <div class="top-container">
      <div class="top-title">
        <span>个人主页</span>&nbsp;<span>home</span>
      </div>
    </div>

    <div class="container">
      <div class="subtitle">
        个人资料 - &nbsp; - &nbsp; - &nbsp; -
      </div>
      <div class="user-info">
        <div>
          <img :src=userInfo.avatar alt="">
        </div>
        <div>
        </div>
      </div>
    </div>
  </div>
 
</template>

<style scoped>
.top-container {
  margin: 50px 50px 0px 50px;
  display: flex;
  justify-content: space-between;
}

.top-title {
  width: 200px;
  font-family: siyuansongti;
}

.top-title span:nth-child(1) {
  font-size: 30px;
}

.top-title span:nth-child(2) {
  font-size: 20px;
}

.container {
  height: 500px;
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti;
  background-color: rgb(218, 245, 245);
}

.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}

.user-info{
  padding: 30px 0px 0px 30px;
  display: flex;
}

.user-info img{
  height: 100px;
  width: 100px;
}
</style>
