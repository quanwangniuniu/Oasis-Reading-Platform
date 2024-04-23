

<script setup>
import { defineComponent, ref } from "vue";

const token = localStorage.getItem('token');
const previewImageUrlRef = ref("");

function handlePreview(file) {

}

const handleFinish = () => {
  console.log('success')
}

</script>

<template>
  <n-upload action="http://127.0.0.1:5000/upload/avatar" :headers="{
    'Authorization': `Bearer ${token}`
  }" show-file-list="false" @preview="handlePreview" @finish="handleFinish"  class="xxx"/>
</template>


<style scoped></style>

