<script setup>
import {reactive, ref} from 'vue'
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const router = useRouter();
const id = router.currentRoute.value.params.id

let book = reactive()
let url = ref()
// onBeforeMount(async function(){
//   book.value = await getBookById(id).data
// })


onBeforeMount(() =>{
    getBookById(id).then(res=>{
      book = res.data
      url.value = book.url
      console.log(book.value.url)
    })
});

</script>


<template>
  {{ book.url }}
  <div>
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      <div class="book-info">
        <div class="img">
            <img :src="url" alt="">
        </div>

        <div>

        </div>
      </div>
      <div class="add-rate"></div>
      <div class="book-description"></div>
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

    .book-info{
      box-sizing:border-box;
      width: 60%;
      height: 400px;
      padding: 30px;
      display: flex;
    }
    
    .add-rate{
      width: 40%;
      height: 400px;
      background-color: green;
    }

    .book-description{
      width: 100%;
      height: 200px;
      background-color: burlywood;
    }

    .book-comments{
      width: 100%;
      height: 200px;
      background-color: blue;
    }



</style>
