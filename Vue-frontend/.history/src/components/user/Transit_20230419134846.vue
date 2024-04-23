<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  const route = useRoute()
  const router = useRouter()

  const userType = localStorage.getItem('type')
  let path1 = route.query.path1;
  let path2 = route.query.path2;

  onBeforeMount(() =>{
    // console.log(path1)
    // console.log(path2)
    if(!userType){
      router.push({ path: '/explore'})   
    }else if(userType == 1){
      router.push({ path: path1})      
    }else{
      router.push({ path: path2})  
    }
    // router.push('/explore')
  })


</script>

<template>
  <div>
  </div>
</template>
