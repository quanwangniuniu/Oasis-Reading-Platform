<script setup>
import Test from './components/Test.vue';
</script>

<template>
  <n-message-provider>
    <div style="height:100%">
      <!-- <Test></Test> -->
      <router-view></router-view>
    </div>
  </n-message-provider>
</template>

<style scoped></style>
