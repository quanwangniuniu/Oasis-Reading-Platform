<script setup>
import { FolderOpenOutline } from '@vicons/ionicons5'
</script>

<template>
  <div>
    <div class="container">
      <div class="no-data-icon">
        <n-icon size="50"  :depth="2">
          <FolderOpenOutline />
        </n-icon>
        <div class="no-data">
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
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
}

.no-data-icon{
  display: block;
}

.no-data{
  display: flex;
  justify-content: center;
}

</style>
