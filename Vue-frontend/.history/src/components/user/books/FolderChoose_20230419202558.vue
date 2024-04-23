<script setup>
import { defineProps, computed, ref } from 'vue';
const props = defineProps(['favouriteObj'])
const favouriteObj = ref(props.favouriteObj)
</script>

<template>
  <div>
    <n-scrollbar style="max-height: 300px">
      <n-form size="large">
        <n-radio-group name="radiogroup1">
          <n-space>
            <n-radio value="Radio 1" class="radio-item">
              Radio 1
            </n-radio>
            <n-radio value="Radio 2" class="radio-item">
              Radio 2
            </n-radio>
            <n-radio value="Radio 3" class="radio-item">
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
.n-radio{
  --n-radio-size:20px !important
}

::v-deep .n-radio__dot{
  border-radius:0% !important;
}

.radio-item{
  font-size: 30px;
}
</style>
