<script setup>
import { FolderOpenOutline } from '@vicons/ionicons5'
</script>

<template>
  <div>
    <div class="container">
      <div class="content">
        <n-icon size="50" class="no-data-icon" :depth="2">
          <FolderOpenOutline />
        </n-icon>
        <div>
          暂无数据
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 420px;
  background-color: rgb(187, 246, 246);
}

.no-data-icon{
  font-weight: lighter;
}
</style>
