<script setup>
import { reactive, ref, h, watch, computed } from 'vue'
import { useMessage } from 'naive-ui'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import { api_getBookById } from '../../axios/api'
import { api_addComment, api_isCommented, api_getComments } from '../../axios/comment_api'
import { api_addFavourite } from '../../axios/favourite_api'
import { TimeOutline, BookmarksOutline, PencilOutline,FileTrayFullOutline } from '@vicons/ionicons5'
import CommentCard from './CommentCard.vue'
import { inject } from 'vue'

const router = useRouter();
//naive的message对象
const message = useMessage()
// 当前书的id, 从books组件传过来的, 再根据这个id查询书的详细信息挂载到页面上
const id = router.currentRoute.value.params.id
// 书的详细信息, onBeforeMount时向后端请求
const book = ref({})
// 控制书的完整简介的Model组件展开的变量, 点击时该变量为true展开Model组件
const showModal = ref(false)
// 控制评分Model展开的变量
const showModal_rate = ref(false)
// 书籍评分对象
const rateObj = ref({
  book_id: id,
  rate: null,
  comment: ''
})

//收藏 想读对象
const favouriteObj = ref({
  book_id: id,
  type: null
})

// 操作对象状态
const operationState = ref({
  isWanted: false,
  isFavourited: false,
  isRated: false
})
const noComment = ref(true)
//评论列表
const comments = ref({})

onBeforeMount(() => {
  loadBook()
});


const loadBook = () => {
  api_getBookById(id).then(res => {
    console.log('xxx')
    console.log(res)
    book.value = res.data
  })

  api_isCommented(id).then(res=>{
    console.log(res.data)
    operationState.value.isRated = res.data.data.isRated
    operationState.value.isWanted = res.data.data.isWanted
    operationState.value.isFavourited = res.data.data.isFavourited
  })

  api_getComments(id, 1).then(res => {
    comments.value = res.data.data
    if(comments.value.length > 0){
      noComment.value = false
      console.log(noComment.value)
    }
  })  
}

const changeRate = (rate) => {
  rateObj.value.rate = rate
}

const rateMovelClose = () => {
  rateObj.value.comment = ''
  rateObj.value.rate = ''
  console.log('xxx')
}

const addFavourite = (type) => {
  favouriteObj.value.type = type
  if(type == 1){
    operationState.value.isWanted = true
  }else{
    operationState.value.isFavourited = true
  }
  api_addFavourite(favouriteObj.value).then(res=>{
    if(type == 1){
      message.success('已标记为想读')
    }else{
      message.success('添加收藏成功')
    }
    console.log(res.data)
  })
}


const commitRate = () => {
  api_addComment(rateObj.value).then(res=>{
    if(res.data.code == 200){
      operationState.value.isRated = true
      showModal_rate.value = false 
      loadBook()   
    }
  })
}
const renderIcon1 = () => {
  return h(TimeOutline)
}

const renderIcon2 = () => {
  return h(BookmarksOutline)
}

const renderIcon3 = () => {
  return h(PencilOutline)
}
</script>


<template>
  <div>
    <div class="top-container">
      <div class="top-title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="subtitle">
        内容简介 - &nbsp; - &nbsp; - &nbsp; -
      </div>
      <div class="book-info">
        <div class="cover">
          <img :src=book.url alt="">
        </div>
        <div class="title-and-desc">
          <div class="book-title">
            <div>{{ book.title }}</div>
          </div>
          <div class="book-author">
            <div>{{ book.author }}</div>
          </div>
          <div class="book-desc">
            <div @click="showModal = true">
              <n-ellipsis line-clamp="13" :tooltip="false">
                {{ book.description }}
              </n-ellipsis>
            </div>

            <n-modal v-model:show="showModal">
              <n-card style="width: 600px" :title=book.title :bordered="false" size="huge" role="dialog"
                aria-modal="true">
                <n-scrollbar style="max-height:300px">
                  <div class="book-desc">
                    {{ book.description }}
                  </div>
                </n-scrollbar>

              </n-card>
            </n-modal>
          </div>

        </div>
        <div class="info-and-rate">
          <div class="rate-container">
            <div class="book-rate">
              <div>{{ book.rate_avg }}</div>
            </div>
            <div class="book-star"><n-rate readonly :default-value="3" /></div>
          </div>

          <div class="info">
            <div v-if="book.publisher">
              出版社:&nbsp;{{ book.publisher }}
            </div>
            <div v-if="book.publish_year">
              出版时间:&nbsp;{{ book.publish_year }}
            </div>
            <div v-if="book.page">
              页数:&nbsp;{{ book.page }}
            </div>
            <div v-if="book.price">
              定价:&nbsp;{{ book.price }}
            </div>
            <div v-if="book.binding">
              装帧:&nbsp;{{ book.binding }}
            </div>
            <div v-if="book.series">
              丛书:&nbsp;{{ book.series }}
            </div>
            <div v-if="book.ISBN">
              ISBN:&nbsp;{{ book.ISBN }}
            </div>

          </div>

        </div>
      </div>
      <div class="subtitle">
        标记 - &nbsp; - &nbsp; - &nbsp; -
      </div>
      <div class="operation">
        <n-button secondary strong :render-icon="renderIcon1" class="operation-btn" color="rgb(2, 108, 2)" v-if="!operationState.isWanted" @click="addFavourite(1)">
          想读
        </n-button>

        <n-button secondary strong :render-icon="renderIcon1" class="operation-btn" color: rgb(247, 99, 99); v-if="operationState.isWanted">
          取消想读
        </n-button>


        <n-button secondary strong :render-icon="renderIcon2" class="operation-btn" color="rgb(2, 108, 2)" v-if="!operationState.isFavourited" @click="addFavourite(2)">
          添加到收藏夹
        </n-button>

        <n-button disabled secondary strong :render-icon="renderIcon1" class="operation-btn" color="rgb(2, 108, 2)" v-if="operationState.isFavourited">
          已添加到收藏夹
        </n-button>

        <n-button secondary strong :render-icon="renderIcon3" class="operation-btn" color="rgb(2, 108, 2)" v-if="!operationState.isRated"
          @click="showModal_rate = true">
          写短评
        </n-button>

        <n-button disabled secondary strong :render-icon="renderIcon1" class="operation-btn" color="rgb(2, 108, 2)" v-if="operationState.isRated">
          已写短评
        </n-button>

      </div>

      <div class="subtitle">
        评论 - &nbsp; - &nbsp; - &nbsp; -
      </div>

      <div class="comment-container">
        <CommentCard v-for="comment in comments" :key="comment.id" :comment-info="comment"></CommentCard>
        <div v-if="noComment">
          <div>
            no comments
          </div>
        </div>
      
      </div>

    </div>
  </div>

  <n-modal 
    v-model:show="showModal_rate" 
    class="rate-card" 
    preset="card" 
    title="写短评" 
    style="width: 600px"
    :bordered="false" 
    :on-after-leave="rateMovelClose" 
    :on-mask-click="rateMovelClose"
  >
    <div>点击星星评分</div>
    <div>
      <n-rate allow-half :on-update:value="changeRate"/>
    </div>
    <div>
      <n-input type="textarea" maxlength="500" placeholder="说说你读过之后的感受吧" v-model:value="rateObj.comment" resize="none"
        :autosize="{
          minRows: 3,
          maxRows: 5
        }" show-count 
      />
    </div>
    <div>
      <n-button strong secondary type="primary" class="commit-rate-btn" @click="commitRate()">
        提交
      </n-button>
    </div>
  </n-modal>
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
  margin: 20px 50px 50px 50px;
  background-color: white;
  box-shadow: 0 0 5px 3px rgb(214, 214, 214);
  font-family: siyuansongti;
}

.subtitle {
  padding: 30px 0px 0px 30px;
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
}

.book-info {
  /* background-color: rgb(188, 224, 188); */
  padding: 10px 30px 30px 30px;
  display: flex;

}

.operation {
  padding: 10px 0px 0px 30px;
  /* background-color: rgb(218, 188, 224); */
}

.operation-btn {
  margin-right: 20px;
}

.cover {
  height: 400px;
  width: 250px;
  /* background-color: rgb(255, 182, 133); */
  margin-right: 30px;
}

.cover img {
  height: 400px;
  width: 250px;
  margin: 0px;
}

.rate-container {
  display: flex;
  /* background-color: rgb(235, 119, 119); */
  align-items: center;
  margin-bottom: 10px;
}

.rate {
  display: flex;
}

.rate-card div {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
  color: gray;
}

.commit-rate-btn{
  width: 200px;
}

.n-card-header {
  padding: 0px;
}

.book-star {
  height: 50px;
  /* background-color: yellow; */
  display: flex;
  flex-direction: column;
  justify-content: end;

  padding-bottom: 10px;
}

.book-rate {
  height: 60px;
  /* background-color: green; */
  display: flex;
  flex-direction: column;
  justify-content: end;
  font-size: 40px;
  margin-right: 10px;
}

.title-and-desc {
  flex: 1;
  /* background-color: rgb(154, 231, 231); */
}

.title {
  display: flex;
}

.book-title {
  font-size: 40px;
}

.book-author {
  font-size: 20px;
  color: grey;
  margin-bottom: 10px;
}

.book-desc {
  white-space: pre-line;
}

.info-and-rate {
  height: 300px;
  width: 300px;
  /* background-color: rgb(142, 142, 244); */
  margin-top: 50px;
  margin-left: 30px;
  padding-left: 50px;
  border-left: 3px rgb(232, 232, 232) solid;
}

.info {
  font-size: 15px;
}

.info div {
  margin-bottom: 10px;
}

.comments {
  height: 500px;
  /* background-color: rgb(212, 192, 231); */
  padding: 30px;
}

.comment-container {
  padding: 10px 30px 30px 30px;
  /* background-color: rgb(200, 255, 237); */
}
</style>
