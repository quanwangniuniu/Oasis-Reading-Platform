

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
      previewFileList: ref([
        {
          id: "react",
          name: "我是react.png",
          status: "finished",
          url: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        },
        {
          id: "vue",
          name: "我是vue.png",
          status: "finished",
          url: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        }
      ])
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
  <n-modal
    v-model:show="showModal"
    preset="card"
    style="width: 600px"
    title="一张很酷的图片"
  >
    <img :src="previewImageUrl" style="width: 100%">
  </n-modal>
</template>


<style scoped></style>

