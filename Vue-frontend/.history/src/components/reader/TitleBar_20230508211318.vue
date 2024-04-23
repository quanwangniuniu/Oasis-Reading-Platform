<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline } from '@vicons/ionicons5'
import { useRouter } from 'vue-router';

const props = defineProps(['ifTitleAndMenuShow', 'id'])

const router = useRouter();

const exit = () => {
    router.push({ path: '/transit', query: { path1: '/books/' + props.id, path2: '/admin/books/' + props.id } })
}

</script>

<template>
    <Transition name="slide-down">
        <div class="title-wrapper" v-show="props.ifTitleAndMenuShow">
            <div class="icon-wrapper">
                <n-icon :component="ArrowBackOutline" size="25" class="icon-exit" @click="exit"/>
            </div>

        </div>
    </Transition>
</template>


<style scoped>
.title-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 101;
    background-color: white;
    width: 100%;
    height: 60px;
    display: flex;
    box-shadow: 0 8px 8px rgb(0, 0, 0, .15);
}

.title-wrapper .left {
    width: 50px;
}

.title-wrapper .right {
    flex: 1;
}

.slide-down-enter-from,
.slide-down-leave-to {
    transform: translate3d(0, 0, 0);
}

.slide-down-enter-to,
.slide-down-leave-from {
    transform: translate3d(0, -100%, 0);
}

.slide-down-enter-active,
.slide-down-leave-active {
    transition: all .3s linear;
}

.icon-exit{
    width: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}
</style>

