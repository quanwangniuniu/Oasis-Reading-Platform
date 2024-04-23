<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px">
      <n-form size="medium">
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

<style scoped>
.n-space{
  display: block  !important;
}

.n-radio .n-radio__dot{
  border-radius:0% !important;
}

n-radio{
  font-size: 30px;
}
</style>
