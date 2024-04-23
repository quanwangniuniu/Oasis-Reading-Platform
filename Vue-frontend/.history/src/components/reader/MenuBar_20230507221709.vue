<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline, Options, TextSharp, SunnyOutline } from '@vicons/ionicons5'

const props = defineProps(['ifTitleAndMenuShow', 'themeList', 'bookAvailable'])
const themeList = props.themeList
const isSettingShow = ref(false)
const showTag = ref(null)
const progress = ref(0)
const fontsize = ref(40)
const theme = ref(0)
const marks =  {
        0: '0',
        20: '20',
        40: '40',
        60: '60',
        80: '80',
        100: '100',
      }

const emit = defineEmits(['setFontSize', 'setTheme']);

const setFontSize = () => {
  emit('setFontSize', 12 + fontsize.value / 10);
}

const setTheme = (index) => {
  theme.value = index
  emit('setTheme', index)
}


const showSetting = (tag) => {
    if(!isSettingShow.value){
        isSettingShow.value = true
        showTag.value = tag
    }else{
        if(showTag.value == tag){
            isSettingShow.value = false
        }else{
            showTag.value = tag
        }
    }

}

const hideSetting = () => {
    isSettingShow.value = false
} 


defineExpose({ hideSetting })

</script>

<template>
    <div class="menu-bar">
        <Transition name="slide-up">
            <div class="menu-wrapper" v-show="props.ifTitleAndMenuShow" :class="{'hide-box-shadow':isSettingShow || !ifTitleAndMenuShow}">
                <div class="icon-wrapper">
                    <n-icon :component="Options" size="20" />
                </div>
                <div class="icon-wrapper" @click="showSetting(2)">
                    <n-icon :component="ArrowBackOutline" size="20" />
                </div>
                <div class="icon-wrapper" @click="showSetting(1)">
                    <n-icon :component="SunnyOutline" size="20" />
                </div>
                <div class="icon-wrapper" @click="showSetting(0)">
                    <n-icon :component="TextSharp" size="20" />
                </div>
            </div>
        </Transition>

        <Transition name="slide-up">
            <div class="setting-wrapper" v-show="isSettingShow" @click="setFontSize" @click.stop>
                <div class="setting-font-size" v-if="showTag === 0">
                    <n-slider v-model:value="fontsize" :marks="marks" step="mark" class="slider" />
                </div>

                <div class="setting-theme" v-else-if="showTag === 1">
                    <div class="setting-theme-item" v-for="(item, index) in themeList" :key="index" @click="setTheme(index)">
                        <div class="preview" :style="{'background':item.style.body.background}"></div>
                        <div class="text" :class="{'selected': index == theme}">{{ item.name }}</div>
                    </div>
                </div>

                <div class="setting-progress" v-else-if="showTag === 2">
                    <div class="progress-slide">
                        <n-slider v-model:value="progress" :step="1" :disabled="!bookAvailable" />
                    </div>

                    <div class="progress-text" v-if="bookAvailable">
                        {{ progress + '%' }}
                    </div>
                    <div class="progress-text" v-if="!bookAvailable">
                        加载中...
                    </div>
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
    z-index: 101;
}

.hide-box-shadow{
    box-shadow: none;
}

.setting-font-size{
    padding: 0 100px;
}

.setting-theme{
    height: 100%;
    display: flex;
}

.setting-theme-item{
    flex:1;
    display: flex;
    flex-direction: column;
    padding: 5px;
    box-sizing: border-box;
}

.setting-theme-item .preview{
    flex:1;
    border: 1px solid #ccc;
}

.setting-theme-item .text{
    height: 20px;
    font-size: 14px;
    text-align: center;
    color: rgb(181, 181, 181);
}

.selected{
    color: black !important;
}

.setting-progress{
    height: 100%;
    display: flex; 
    flex-direction: column; 
}

.progress-slide{
    padding: 0 100px;
    flex:1;
    display: flex;
    flex-direction: column;
    justify-content: end;
}

.progress-text{
    height: 20px;
    text-align: center;
}

</style>

