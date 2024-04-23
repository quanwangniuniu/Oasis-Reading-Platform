

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline } from '@vicons/ionicons5'
const URL = 'http://127.0.0.1:5000/bookfile/1682939060264.epub'
import ePub from 'epubjs'

const ifTitleAndMenuShow = ref(false)

const book = new ePub(URL)
const rendition = book.renderTo('read', {
  witdh: window.innerWidth,
  height: window.innerHeight,
  spread: 'none'
})

const showEpub = () => {
  rendition.display()
}

const nextPage = () => {
    rendition.next();
}

const prevPage = () => {
    rendition.prev();
}

const toggleTitleAndMenu = () => {
  ifTitleAndMenuShow.value = !ifTitleAndMenuShow.value
}


onBeforeMount(() => {
  showEpub()
})


</script>

<template>
  <div>

    <div class="ebook">
      <transition name="slide-down">
        <div class="title-wrapper" v-show="ifTitleAndMenuShow">
          <div class="left">
            <n-icon :component="ArrowBackOutline" color="grey" size="20" />
          </div>
          <div class="right">
          </div>
        </div>        
      </transition>


      <div class="read_wrapper">
        <div id="read"></div>
        <div class="mask">
          <div class="left" @click="prevPage"></div>
          <div class="center" @click="toggleTitleAndMenu"></div>
          <div class="right" @click="nextPage"></div>
        </div>
      </div>

      <div class="menu-wrapper" v-show="ifTitleAndMenuShow">
        <div class="icon-wrapper">
          <n-icon :component="ArrowBackOutline" color="grey" size="20" />
        </div>
        <div class="icon-wrapper">
          <n-icon :component="ArrowBackOutline" color="grey" size="20" />
        </div>
        <div class="icon-wrapper">
          <n-icon :component="ArrowBackOutline" color="grey" size="20" />
        </div>
        <div class="icon-wrapper">
          <n-icon :component="ArrowBackOutline" color="grey" size="20" />
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>

.title-wrapper{
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

.title-wrapper .left{
  width: 50px;
}

.title-wrapper .right{
  flex: 1;
}

.slide-down-enter{
  transform: translate3d(0, -100%, 0);
}

.slide-down-enter-to{
  transform: translate3d(0, 0, 0);
}

.slide-down-enter-active{
  transform: all .3s linear;
}

.menu-wrapper{
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

.menu-wrapper .icon-wrapper{
  flex: 1;
}

.icon-wrapper{
  display: flex;
  justify-content: center;
  align-items: center;
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

