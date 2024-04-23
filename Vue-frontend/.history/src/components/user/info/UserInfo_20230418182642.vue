<script setup>
import { ref, onBeforeMount, computed } from 'vue'
import { api_getUserInfo } from '../../axios/user_api'
import { MaleFemaleOutline, TodayOutline, PhonePortraitOutline, MailOpenOutline } from '@vicons/ionicons5'
const userInfo = ref({})

const showModal = ref(false)

const gender = computed(() => {
  if (userInfo.value.gender == 0) {
    return '未知'
  } else if (userInfo.value.gender == 1) {
    return '男'
  } else {
    return '女'
  }
})

onBeforeMount(() => {
  api_getUserInfo().then((res) => {
    if (res.data.code == 200) {
      userInfo.value = res.data.data
      console.log(userInfo.value)
    }

  })
})

const editUserInfo = () => {
  showModal.value = true;
}
</script>

<template>
  <div>
    <div class="top-container">
      <div class="top-title">
        <span>个人主页</span>&nbsp;<span>home</span>
      </div>
    </div>

    <div class="container">
      <div class="left-container">
        <div class="subtitle">
          个人资料 - &nbsp; - &nbsp; - &nbsp; -
        </div>

        <div class="user-info">
          <div class="avatar">
            <div>
              <img :src=userInfo.avatar alt="">
              <div>
                {{ userInfo.username }}
              </div>
            </div>
            {{ userInfo.signature }}
          </div>
          <div class="info-list">
            <div>
              <n-icon size="18" :component="MaleFemaleOutline" />&nbsp;性别: &nbsp; {{ gender }}
            </div>
            <div>
              <n-icon size="18" :component="TodayOutline" />&nbsp;生日: &nbsp; {{ userInfo.birthday }}
            </div>
            <div>
              <n-icon size="18" :component="PhonePortraitOutline" />&nbsp;手机号: &nbsp; {{ userInfo.phone == null ? '未绑定' :
                userInfo.phone }}
            </div>
            <div>
              <n-icon size="18" :component="MailOpenOutline" />&nbsp;邮箱: &nbsp; {{ userInfo.email == null ? '未绑定' :
                userInfo.email }}
            </div>
            <div>
              <n-button strong secondary type="primary" class="edit-btn" @click="editUserInfo()">
                编辑信息
              </n-button>
            </div>

          </div>
        </div>
      </div>

      <div class="right-container">
        <div class="subtitle">
          最近评论 - &nbsp; - &nbsp; - &nbsp; -
        </div>

      </div>
    </div>

    <n-modal 
      v-model:show="showModal" 
      style="width: 600px"
      class="custom-card" 
      preset="card" 
      title="编辑资料" 
      size="huge"
      :bordered="false">
      <div class="edit-container">

      </div>
    </n-modal>

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
  /* background-color: rgb(218, 245, 245); */
  display: flex;
}

.left-container {
  flex: 1;
}

.right-container {
  flex: 2;
}

.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}

.user-info {
  padding: 30px 0px 0px 30px;
}

.user-info>div {
  margin-bottom: 20px;

}

.left {
  background-color: rgb(227, 170, 170);
}

.user-info img {
  height: 80px;
  width: 80px;
  margin-right: 10px;
}

.avatar div {
  display: flex;
  align-items: end;
  font-size: 40px;
  color: black;
}

.edit-btn {
  width: 200px;
}

.info-list {
  font-size: 20px;
}

.edit-container{
  height: 500px;
}
</style>
