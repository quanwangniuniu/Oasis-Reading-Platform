

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
const URL = 'http://127.0.0.1:5000/bookfile/1682939060264.epub'
import ePub from 'epubjs'

const book = new ePub(URL)
const rendition = book.renderTo('read',{
  witdh: window.innerWidth,
  height: window.innerHeight
})

const showEpub = () => {
  rendition.display()
}

onBeforeMount(()=>{
  showEpub()
})


</script>

<template>

<div>
  <div id="read"></div>
</div>
</template>


<style scoped>
</style>

