<script setup>
  
  import {ref, onBeforeMount} from 'vue'
  import BookCard from './BookCard.vue'
  import { useRoute, useRouter } from 'vue-router'
  const route = useRoute()
  const router = useRouter()

  let title = route.query.title;

  onBeforeMount(() =>{
    router.push({ name: 'search', query: {title : search_input.value}})
  })


</script>

<template>
  <div>
  </div>
</template>
