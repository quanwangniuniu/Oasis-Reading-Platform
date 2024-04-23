<script setup>
import { reactive, ref, h } from 'vue'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import { api_getBookById } from '../../axios/api'
import { CashOutline as CashIcon } from '@vicons/ionicons5'
const router = useRouter();
const id = router.currentRoute.value.params.id
const showModal = ref(false)
let book = ref({})

onBeforeMount(() => {
  api_getBookById(id).then(res => {
    console.log('xxx')
    console.log(res)
    book.value = res.data
  })
});

const renderIcon = () => {
  return h(CashIcon);
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
            <div>
              出版社:&nbsp;{{ book.publisher }}
            </div>
            <div>
              出版时间:&nbsp;{{ book.publish_year }}
            </div>
            <div>
              页数:&nbsp;{{ book.page }}
            </div>
            <div>
              定价:&nbsp;{{ book.price }}
            </div>
            <div>
              装帧:&nbsp;{{ book.binding }}
            </div>
            <div>
              丛书:&nbsp;{{ book.series }}
            </div>
            <div>
              ISBN:&nbsp;{{ book.ISBN }}
            </div>

          </div>

        </div>
      </div>
      <div class="subtitle">
        标记 - &nbsp; - &nbsp; - &nbsp; -
      </div>
      <div class="write-comments">
        <n-button secondary strong :render-icon="renderIcon">
          +100 元
        </n-button>
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
  margin: 20px 50px 0px 50px;
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

.write-comments {
  padding: 10px 0px 0px 30px;
  height: 300px;
  background-color: rgb(218, 188, 224);
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
</style>
