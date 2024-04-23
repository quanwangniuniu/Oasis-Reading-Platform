

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const previewImageUrlRef = ref("");
    function handlePreview(file) {
      const { url } = file;
      previewImageUrlRef.value = url;
      showModalRef.value = true;
    }
    return {
      handlePreview,
      previewImageUrl: previewImageUrlRef,
    };
  }
});
</script>

<template>
  <n-upload
    action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
    list-type="image-card"
    @preview="handlePreview"
  />
</template>


<style scoped></style>

