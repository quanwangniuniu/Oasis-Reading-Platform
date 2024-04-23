

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
const URL = 'http://127.0.0.1:5000/bookfile/1682939060264.epub'
import ePub from 'epubjs'

const book = new ePub(URL)
const rendition = book.renderTo('read', {
  witdh: window.innerWidth,
  height: window.innerHeight
})

const showEpub = () => {
  rendition.display()
}

onBeforeMount(() => {
  showEpub()
})


</script>

<template>
  <div>

    <div class="ebook">
      <div class="read_wrapper">
        <div id="read"></div>
        <div class="mask">
          <div class="lef"></div>
          <div class="center"></div>
          <div class="right"></div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
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
  width: 100px;
}

.mask .center {
  flex: 1
}

.mask .right {
  width: 100px;
  background-color: blue;
}
</style>

