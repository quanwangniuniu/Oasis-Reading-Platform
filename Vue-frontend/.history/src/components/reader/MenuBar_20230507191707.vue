<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline, Options, TextSharp, SunnyOutline } from '@vicons/ionicons5'

const props = defineProps(['ifTitleAndMenuShow'])
const isSettingShow = ref(false)
const value = ref([50, 70])
const marks = {
    34: '太棒了',
    75: '不错'
}
const showSetting = () => {
    isSettingShow.value = !isSettingShow.value
}

</script>

<template>
    <div class="menu-bar">
        <Transition name="slide-up">
            <div class="menu-wrapper" v-show="props.ifTitleAndMenuShow">
                <div class="icon-wrapper">
                    <n-icon :component="Options" size="20" />
                </div>
                <div class="icon-wrapper">
                    <n-icon :component="ArrowBackOutline" size="20" />
                </div>
                <div class="icon-wrapper">
                    <n-icon :component="SunnyOutline" size="20" />
                </div>
                <div class="icon-wrapper" @click="showSetting">
                    <n-icon :component="TextSharp" size="20" />
                </div>
            </div>
        </Transition>

        <Transition name="slide-up">
            <div class="setting-wrapper" v-show="isSettingShow">
                <div class="setting-font-size">
                    <n-slider v-model:value="value" range :marks="marks" :step="10" />
                </div>
            </div>
        </Transition>

    </div>
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

.setting-wrapper {
    position: absolute;
    bottom: 60px;
    left: 0px;
    width: 100%;
    height: 60px;
    background: white;
    box-shadow: 0 -8px 8px rgb(0, 0, 0, .15);
}

.setting-font-size {}
</style>

