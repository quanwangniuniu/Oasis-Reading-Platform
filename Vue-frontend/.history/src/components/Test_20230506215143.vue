

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { ArrowBackOutline } from '@vicons/ionicons5'
const URL = 'http://127.0.0.1:5000/bookfile/1682939060264.epub'
import ePub from 'epubjs'

const book = new ePub(URL)
const rendition = book.renderTo('read', {
  witdh: window.innerWidth,
  height: window.innerHeight,
  spread: 'none'
})

const showEpub = () => {
  rendition.display()
}

function nextPage() {
    rendition.next();
}

function prevPage() {
    rendition.prev();
}


onBeforeMount(() => {
  showEpub()
})


</script>

<template>
  <div>

    <div class="ebook">
      <div class="title-wrapper">
        <div class="left">
          <n-icon :component="ArrowBackOutline" color="grey" size="20" />
        </div>
        <div class="right">
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

      <div class="read_wrapper">
        <div id="read"></div>
        <div class="mask">
          <div class="left" @click="prevPage"></div>
          <div class="center"></div>
          <div class="right" @click="nextPage"></div>
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
  background-color: red;
  width: 100%;
  height: 100px;
}

.title-wrapper .left{

}

.title-wrapper .right{
  
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

