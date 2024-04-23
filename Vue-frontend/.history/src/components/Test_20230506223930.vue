

<script setup>

import Ebook from '../components/reader/Ebook.vue'


</script>

<template>
  <Ebook></Ebook>
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

