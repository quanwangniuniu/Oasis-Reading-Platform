<script setup>
</script>

<template>
  <div class="main">
    <div class="top-container">
      <div class="title">
        <span>图书</span>&nbsp;<span>books</span>
      </div>
      <div>
        <n-input placeholder="搜索" class="input" v-model:value="search_input" @keyup.enter="search()">
          <template #prefix>
            <n-icon :component="Search" color="black" />
          </template>
        </n-input>

      </div>

    </div>
  </div>
</template>

<style scoped>
</style>
