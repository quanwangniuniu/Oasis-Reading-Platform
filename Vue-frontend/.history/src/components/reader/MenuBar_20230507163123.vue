<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline, Options, TextSharp, SunnyOutline } from '@vicons/ionicons5'

const props = defineProps(['ifTitleAndMenuShow'])

</script>

<template>
    <Transition name="slide-up">
        <div class="menu-wrapper" v-show="props.ifTitleAndMenuShow">
            <div class="icon-wrapper">
                <n-icon :component="Options" color="grey" size="20" />
            </div>
            <div class="icon-wrapper">
                <n-icon :component="ArrowBackOutline" color="grey" size="20" />
            </div>
            <div class="icon-wrapper">
                <n-icon :component="SunnyOutline" color="grey" size="20" />
            </div>
            <div class="icon-wrapper">
                <n-icon :component="TextSharp" color="grey" size="20" />
            </div>
        </div>
    </Transition>
</template>


<style scoped>


.menu-wrapper {
    position: absolute;
    bottom: 0;
    left: 0;
    z-index: 101;
    background-color: white;
    width: 100%;
    height: 60px;
    display: flex;
    box-shadow: 0 -8px 8px rgb(0, 0, 0, .15);
}

.menu-wrapper .icon-wrapper {
    flex: 1;
}

.icon-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

.slide-up-enter-from,
.slide-up-leave-to {
    transform: translate3d(0, 100%, 0);
}

.slide-up-enter-to,
.slide-up-leave-from {
    transform: translate3d(0, 0, 0);
}

.slide-up-enter-active,
.slide-up-leave-active {
    transition: all .3s linear;
}
</style>

