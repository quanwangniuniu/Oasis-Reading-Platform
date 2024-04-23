

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline } from '@vicons/ionicons5'
import MenuBar from './MenuBar.vue'
import TitleBar from './TitleBar.vue'


const URL = 'http://127.0.0.1:5000/bookfile/1682939060264.epub'
const defaultFontSize = 16
import ePub from 'epubjs'

const ifTitleAndMenuShow = ref(false)

const book = new ePub(URL)
const rendition = book.renderTo('read', {
  witdh: window.innerWidth,
  height: window.innerHeight,
  spread: 'none'
})
const themes = rendition.themes

const menubar = ref()

const showEpub = () => {
  rendition.display()
  themes.fontSize(defaultFontSize)
  console.log(defaultFontSize)
}

const nextPage = () => {
  rendition.next();
}

const prevPage = () => {
  rendition.prev();
}

const setFontSize = (fontsize) => {
  themes.fontSize(fontsize + 'px')
}

const toggleTitleAndMenu = () => {
  ifTitleAndMenuShow.value = !ifTitleAndMenuShow.value
  if(!ifTitleAndMenuShow.value){
    menubar.value.hideSetting()
  }
}


onBeforeMount(() => {
  showEpub()
})


</script>

<template>
  <div>

    <div class="ebook">
    <TitleBar :ifTitleAndMenuShow="ifTitleAndMenuShow"></TitleBar>

      <div class="read_wrapper">
        <div id="read"></div>
        <div class="mask">
          <div class="left" @click="prevPage"></div>
          <div class="center" @click="toggleTitleAndMenu"></div>
          <div class="right" @click="nextPage"></div>
        </div>
      </div>

      <MenuBar :ifTitleAndMenuShow="ifTitleAndMenuShow" ref="menubar" @setFontSize="setFontSize"></MenuBar>
    </div>
  </div>
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

.slide-down-enter-from, .slide-down-leave-to {
  transform: translate3d(0, -100%, 0);
}

.slide-down-enter-to, .slide-down-leave-from {
  transform: translate3d(0, 0, 0);
}

.slide-down-enter-active, .slide-down-leave-active {
  transition: all .3s linear;
}

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

.slide-up-enter-from, .slide-up-leave-to {
  transform: translate3d(0, 100%, 0);
}

.slide-up-enter-to, .slide-up-leave-from {
  transform: translate3d(0, 0, 0);
}

.slide-up-enter-active, .slide-up-leave-active {
  transition: all .3s linear;
}

.ebook {
  position: relative;
}

.mask {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 100;
  display: flex;
  width: 100%;
  height: 100%;
}

.mask .left {
  width: 200px;
}

.mask .center {
  flex: 1;
  display: flex;
  justify-content: center;
}

.mask .right {
  width: 200px;
}
</style>

