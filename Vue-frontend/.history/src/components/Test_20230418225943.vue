

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const showModalRef = ref(false);
    const previewImageUrlRef = ref("");
    function handlePreview(file) {
      const { url } = file;
      previewImageUrlRef.value = url;
      showModalRef.value = true;
    }
    return {
      handlePreview,
      showModal: showModalRef,
      previewImageUrl: previewImageUrlRef,
    };
  }
});
</script>

<template>
  <n-divider />
  <n-upload
    action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
    list-type="image-card"
    @preview="handlePreview"
  />
    <img :src="previewImageUrl" style="width: 100%">
  </n-modal>
</template>


<style scoped></style>

