<script setup>
import { ref, onBeforeMount, computed } from 'vue'
import { api_getUserInfo } from '../../axios/user_api'
import { MaleFemaleOutline, TodayOutline, PhonePortraitOutline, MailOpenOutline } from '@vicons/ionicons5'
import EditInfo from './EditInfo.vue'
import RecentComment from './RecentComment.vue'
//原始用户信息
const userInfo = ref({})
//编辑后的用户信息
const editedUserInfo = ref({})
const showModal = ref(false)

// 计算属性, 将数字表示的性别转换为字符串
const gender = computed(() => {
  if (userInfo.value.gender == 0) {
    return '未知'
  } else if (userInfo.value.gender == 1) {
    return '男'
  } else {
    return '女'
  }
})

//计算属性, 将数据库中的时间戳转换为yyyy-mm-dd格式的字符串
const birthday = computed(() => {
  let timestamp = userInfo.value.birthday;
  if(timestamp == 0){
    return '未绑定'
  }else{
    const date = new Date(timestamp);
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    const formattedDate = `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`; // 格式化为年月日字符串，注意月份和日期需要补零
    return formattedDate    
  }
})

const signature = computed(()=>{
  if(userInfo.value.signature == ''){
    return '快去设置个性签名吧！'
  }else{
    return userInfo.value.signature 
  } 
})

onBeforeMount(() => {
  loadUserInfo()
})

const loadUserInfo = () => {
  api_getUserInfo().then((res) => {
    if (res.data.code == 200) {
      const jsonStr = JSON.stringify(res.data.data)
      userInfo.value = JSON.parse(jsonStr)
      editedUserInfo.value = JSON.parse(jsonStr)
      console.log(userInfo.value)
      console.log('xxx')
      console.log(editedUserInfo.value)
    }
  })
}

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

    <div class="panel">
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
              {{ signature }}
            </div>
            <div class="info-list">
              <div>
                <n-icon size="18" :component="MaleFemaleOutline" />&nbsp;性别: &nbsp; {{ gender }}
              </div>
              <div>
                <n-icon size="18" :component="TodayOutline" />&nbsp;生日: &nbsp; {{ birthday }}
              </div>
              <div>
                <n-icon size="18" :component="PhonePortraitOutline" />&nbsp;手机号: &nbsp; {{ userInfo.phone == '' ? '未绑定'
                  :
                  userInfo.phone }}
              </div>
              <div>
                <n-icon size="18" :component="MailOpenOutline" />&nbsp;邮箱: &nbsp; {{ userInfo.email == '' ? '未绑定' :
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
          <RecentComment></RecentComment>

        </div>
      </div>
      <n-divider />
      <!-- <n-divider />
      <div>
        <div class="subtitle">
          我的收藏 - &nbsp; - &nbsp; - &nbsp; -
        </div>
        <div class="fav-container">
          sdfsdf
        </div>
      </div>       -->
    </div>




    <n-modal v-model:show="showModal" style="width: 600px" class="custom-card" preset="card" title="编辑资料" size="huge"
      :bordered="false">
      <EditInfo :user="editedUserInfo"></EditInfo>
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

.panel{
  /* height: 500px; */
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti; 
  padding: 0px 30px 30px 30px;
}
.container {
  /* height: 500px;
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti; */
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
  padding: 30px 0px 0px 50px;
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

.info-list>div {
  margin-bottom: 10px;
}

.edit-container {
  width: 500px;
  height: 500px;
}

.edit-avatar {
  height: 150px;
  width: 150px;
  border-radius: 50%;
}

.dragger-container {
  width: 500px;
  display: flex;
  justify-content: center;
}

.avatar-upload-dragger {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  padding: 0px;
}

.n-divider:not(.n-divider--vertical){
  margin-top: 10px;
  margin-bottom: 10px;
}

.fav-container{
  padding: 30px 0px 0px 30px
}
</style>
