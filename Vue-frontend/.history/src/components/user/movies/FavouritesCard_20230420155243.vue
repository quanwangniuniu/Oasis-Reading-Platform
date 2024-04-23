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
    <div class="subtitle">
      {{ folder.name }} - &nbsp; - &nbsp; - &nbsp; -
    </div>

    <div v-if="folder.books.length != 0" class="bookcard-container">
      <BookCard v-for="book in folder.books" :key="book.id" class="card" :book-info="book"></BookCard>
    </div>

    <div v-if="folder.books.length == 0" class="on-data-container">
      <div>
          <n-icon size="20"  :depth="2">
            <FolderOpenOutline />
          </n-icon>          
        </div>
      该收藏夹还没有收藏书籍哦
    </div>
  </div>
  <n-divider />
</template>

<style scoped>
.subtitle {
  font-size: 20px;
  color: rgb(2, 128, 2);
  font-family: deyihei;
  margin-bottom: 20px;
}

.on-data-container{
  height: 50px;
  display: flex;
  justify-content: center;
}

.bookcard-container{
  display: flex;
  justify-content: left;
  flex-flow: row wrap;
  margin-right: 0px;
}

.bookcard-container > div{
  margin-right: 20px;
}
</style>
