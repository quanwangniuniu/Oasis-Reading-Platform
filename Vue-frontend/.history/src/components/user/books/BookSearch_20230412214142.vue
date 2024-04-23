<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import BookCard from './BookCard.vue'
  import {getBooks, getBookByTitle} from '../../axios/api'
  import { useRouter } from 'vue-router'

  let books = ref([])
  const search_input = ref('')

  const getAllBooks = () =>{
    getBooks().then(res=>{
      books.value = res.data
    })
  }

  const search = () =>{
    router.push({ path: 'search' })
    // getBookByTitle(search_input.value).then(res=>{
    //   books.value = res.data
    // })
  }

  onBeforeMount(() =>{
    getAllBooks()
  })


</script>

<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>搜索</span>&nbsp;<span>books</span>
      </div>
      <div class="search">
        <input class="search-input" v-model="search_input"/>
        <el-icon class="search-icon" @click="search"><Search /></el-icon>
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
      display: flex;
      justify-content: right;
    }

    .search-input{
      border: 0px;
      padding: 0;
      outline: none; 
      box-shadow: 0px 0px 3px 1px rgb(214, 214, 214);
      height: 40px;
      width: 400px;
      z-index: 1;
    }

    .search-icon{
      z-index: 2;
      margin-left: -40px;
    }
    .search-input:focus{
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
