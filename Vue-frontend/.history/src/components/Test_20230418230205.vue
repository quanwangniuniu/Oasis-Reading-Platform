

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const previewImageUrlRef = ref("");
    function handlePreview(file) {
      const { url } = file;
      previewImageUrlRef.value = url;
      console.log(url)
    }
    return {
      handlePreview,
      previewImageUrl: previewImageUrlRef,
    };
  }
});
</script>

<template>
  <n-upload action="http://127.0.0.1:5000/upload/avatar" :headers="{
    'Authorization': `Bearer ${token}`
  }" list-type="image-card" @preview="handlePreview" />
</template>


<style scoped></style>

