<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  const route = useRoute()
  const router = useRouter()

  let title = route.query.title;
  const userType = localStorage.getItem('type')

  onBeforeMount(() =>{
    console.log('transit')
    console.log(userType)
    if(userType == 1){
      router.push({ path: '/search', query: {title : title}})      
    }else{
      router.push({ path: '/admin/search', query: {title : title}})  
    }

  })


</script>

<template>
  <div>
  </div>
</template>
