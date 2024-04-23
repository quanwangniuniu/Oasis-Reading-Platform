<script setup>
const props = defineProps(['bookAvailable', 'navigation'])
const emit = defineEmits(['jumpTo']);

const jumpTo = (href) => {
    emit('jumpTo', href);
}

</script>

<template>
    <transition name="slide-right">
        <div class="content">
            <div class="content-wrapper" v-if="bookAvailable">
                <div class="content-item" v-for="(item, index) in props.navigation.toc" :key="index"
                    @click="jumpTo(item.href)">
                    <span class="text">{{ item.label }}</span>
                </div>
            </div>
            <div class="empty" v-if="!bookAvailable">加载中...</div>
        </div>
    </transition>
</template>

<style scoped>
.content {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 103;
    width: 30%;
    height: 100%;
    background: white;
}

.content-wrapper {
    width: 100%;
    height: 100%;
    overflow: auto;
}

.content-item {
    padding: 20px 20px;
    border-bottom: 1px solid #f4f4f4;
}

.text {
    font-size: 14px;
    color: #333;
}

.empty {
    width: 100%;
    height: 100%;
    font-size: px2rem(16);
    color: #333;
    display: flex;
    justify-content: center;
  }
</style>
