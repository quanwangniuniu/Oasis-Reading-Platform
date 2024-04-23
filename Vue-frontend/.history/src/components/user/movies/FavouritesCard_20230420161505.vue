<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { FolderOpenOutline } from '@vicons/ionicons5'
import BookCard from '../../user/books/BookCard.vue'
const props = defineProps(['folder'])
const folder = props.folder

onBeforeMount(() => {
  console.log(folder.books.length)
})
</script>

<template>
  <div>
    <div v-if="folder.books.length != 0" class="bookcard-container">
      <BookCard v-for="book in folder.books" :key="book.id" class="card" :book-info="book"></BookCard>
    </div>

    <div v-if="folder.books.length == 0" class="on-data-container">
      <n-empty description="该收藏夹还没有内容哦">
      </n-empty>
    </div>
  </div>
</template>

<style scoped>
.on-data-container {
  height: 100px;
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.bookcard-container {
  display: flex;
  justify-content: left;
  flex-flow: row wrap;
  margin-right: 0px;
}

.bookcard-container>div {
  margin-right: 40px;
}
</style>
