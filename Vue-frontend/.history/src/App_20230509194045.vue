<script setup>
import Test from './components/Test.vue';
</script>

<template>
  <n-dialog-provider>
    <n-message-provider>
      <div>
        <Test></Test>
        <!-- <router-view></router-view> -->
      </div>
    </n-message-provider>    
  </n-dialog-provider>

</template>

<style scoped></style>
