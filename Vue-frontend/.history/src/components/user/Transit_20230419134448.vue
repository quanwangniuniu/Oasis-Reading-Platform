<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  const route = useRoute()
  const router = useRouter()

  let path1 = route.query.path1;
  let path2 = route.query.path2;

  onBeforeMount(() =>{
    console.log(path1)
    console.log(path2)
    // router.push('/explore')
  })


</script>

<template>
  <div>
  </div>
</template>
