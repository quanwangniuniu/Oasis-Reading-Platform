<script setup>
import {ref} from 'vue'
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import {getBookById} from '../../axios/api'
const $router = useRouter();
const id = $router.currentRoute.value.params.id

let book = ref()

onMounted(() => {
    getBookById(id).then(res=>{
      book.value = res.data
    })
});

</script>


<template>
  <div>
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
    </div>
    <div class="container">
      {{book}}
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
    .container{
      display: flex;
      justify-content:space-between;
      flex-flow:row wrap;
      margin-left: 50px;
      margin-right: 50px;
      margin-top: 50px;
    }
    .card{
      margin-top: 50px;
    }
</style>
