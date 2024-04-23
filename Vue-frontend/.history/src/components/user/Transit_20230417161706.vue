<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  const route = useRoute()
  const router = useRouter()

  let title = route.query.title;

  onBeforeMount(() =>{
    router.push('/explore')
  })


</script>

<template>
  <div>
  </div>
</template>
