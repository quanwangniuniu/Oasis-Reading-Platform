<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import BookCard from './BookCard.vue'
  import {getBooks} from '../../axios/api'

  let books = ref([])
  const input = ref('')

  onBeforeMount(() =>{
    getBooks().then(res=>{
      books.value = res.data
    })
  })


</script>

<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>书籍</span>&nbsp;<span>books</span>
      </div>
      <div class="search">
        <input class="search-input" v-model="input"/>
      </div>
    </div>
    <div class="container">
      <BookCard v-for="book in books" :key="book.id" class="card" :book-info="book"></BookCard>       
    </div>
  </div>
</template>

<style scoped>

    .top-container{
      margin: 50px 50px -30px 50px;
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

    .search{
      width: 400px;
    }

    .search-input{
      border: 0;/*清除自带的2px的边框*/
      padding: 0;/*清除自带的padding间距*/
      outline: none;/*清除input点击之后的黑色边框*/
      height: 40px;
      width: 400px;
    }
    .search-input:focus{
      border: 2px;
      border-color: green;
      outline-color: gray;
    }
    .container{
      display: flex;
      justify-content:space-between;
      flex-flow:row wrap;
      margin-left: 50px;
      margin-right: 50px;
    }
    .card{
      margin-top: 50px;
    }
</style>
