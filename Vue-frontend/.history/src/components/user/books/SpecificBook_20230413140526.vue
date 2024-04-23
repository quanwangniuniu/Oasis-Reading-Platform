<script setup>
import {reactive, ref} from 'vue'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const router = useRouter();
const id = router.currentRoute.value.params.id

let book = ref({})

onBeforeMount(
  async function(){
    book.value = (await getBookById(id)).data
    console.log(book.value)
  }
)

// onBeforeMount(() =>{
//     getBookById(id).then(res=>{
//       book.value = res.data
//     })
// });

</script>


<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="book-info">
        <div class="img" v-show="book.url">
            <img :src=book.url alt="">
        </div>

        <div class="info">
          <div class="book-info-title">
              {{ book.title }}
          </div>

          <div class="book-info-author">
            {{ book.author }}
          </div>
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

        <div class="rate">
          {{ book.rate_avg }}
        </div>
        <div>

        </div>
      </div>
      <div class="add-rate"></div>
      <div class="book-description">
        {{ book.description }}  

      </div>
      <div class="book-comments"></div>
    </div>
  </div>
</template>

<style scoped>

    .top-container{
      margin: 50px 50px 0px 50px;
      display: flex;
      justify-content: space-between;
    }
    
    .title{
      width: 200px;
      font-family: siyuansongti;
    }

    .title span:nth-child(1){
      font-size: 30px;
    }
    .title span:nth-child(2){
      font-size: 20px;
    }
    .container{
      display: flex;
      justify-content:space-between;
      flex-flow:row wrap;
      margin: 20px 50px 0px 50px;
      background-color: white;
      box-shadow: 0 0 5px 3px rgb(214, 214, 214); 
    }

      .book-info div{
      margin: 10px;
    }

    .book-info{
      box-sizing:border-box;
      flex:2;
      height: 500px;
      padding: 25px 0px 0px 25px;
      display: flex;
      background-color: rgba(154, 77, 227, 0.1);
    }

    .info{
      box-sizing:border-box;
      padding: 0px;
      height: 400px;
      width: 100%;
      background-color: rgb(202, 114, 114,0.1);
      font-family: siyuansongti; 
    }

    .title-and-rate{
      margin: 0px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .book-info-rate{
      margin: 0px !important;
      font-size: 30px;
    }

    .book-info-title{
      font-size:30px;
    }

    .book-info-author{
      font-size:20px;   
      color:rgb(84, 84, 84);
    }

    .img{
      height: 400px;
      width: 250px;
    }

    .img img{
      height: 400px;
      width: 250px;
    }
    
    .add-rate{
      /* box-sizing:border-box;
      flex:2;
      height: 500px;
      padding: 50px 25px 0px 50px;
      display: flex; */
      box-sizing:border-box;
      width: 500px;
      height: 500px;
      padding: 25px 25px 0 10px;
      background-color: rgb(52, 155, 52,0.1);
    }

    .rate{
      width: 200px;
      height: 400px;
      margin: 10px 0px !important;
      background-color: red;
      font-size: 40px;
    }
    .book-description{
      width: 100%;
      padding: 0px 50px 0 50px;
      white-space: pre-line;
      font-size: medium;
      color:rgb(73, 73, 73);
      font-family: siyuansongti;   
    }

    .book-comments{
      width: 100%;
      height: 200px;
      background-color: blue;
    }
</style>
