<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import BookCard from './BookCard.vue'
  import {getBooks} from '../../axios/api'

  let books = ref([])

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
        <span>书籍</span>&bnsp;<span>books</span>
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
    }
    .container{
      display: flex;
      justify-content:space-between;
      flex-flow:row wrap;
      margin-left: 50px;
      margin-right: 50px;
    }

    .title span:nth-child(1){
      font-size: 30px;
    }

    .card{
      margin-top: 50px;
    }
</style>
