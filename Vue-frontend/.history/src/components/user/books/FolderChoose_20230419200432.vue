<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px">
      <n-form>
        <n-radio-group name="radiogroup1">
          <n-space>
            <n-radio value="Radio 1">
              Radio 1
            </n-radio>
            <n-radio value="Radio 2">
              Radio 2
            </n-radio>
            <n-radio value="Radio 3">
              Radio 3
            </n-radio>
          </n-space>
        </n-radio-group>
      </n-form>
    </n-scrollbar>
  </div>
</template>

<style scoped></style>
