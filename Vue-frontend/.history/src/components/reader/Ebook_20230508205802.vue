

<script setup>
import { defineProps, onBeforeMount, ref } from 'vue';
import { useRouter } from 'vue-router';
import MenuBar from './MenuBar.vue'
import TitleBar from './TitleBar.vue'
import ePub from 'epubjs'

const router = useRouter();
const id = router.currentRoute.value.params.id

const URL = 'http://127.0.0.1:5000/bookfile/' + id + '.epub'

const defaultSetting = {
  fontSize: 16,
  theme: 0
}


const ifTitleAndMenuShow = ref(false)

const book = new ePub(URL)
const rendition = book.renderTo('read', {
  witdh: window.innerWidth,
  height: window.innerHeight,
  spread: 'none'
})
const themes = rendition.themes
let locations = null
let navigation = null

const bookAvailable = ref(false)

const menubar = ref()

const themeList = [
  {
    name: 'default',
    style:{
      body:{
        'color':'#000', 'background': '#fff'
      }
    }
  },
  {
    name: 'eye',
    style:{
      body:{
        'color':'#000', 'background': '#ceeaba'
      }
    }
  },
  {
    name: 'night',
    style:{
      body:{
        'color':'#fff', 'background': '#000'
      }
    }
  },
  {
    name: 'gold',
    style:{
      body:{
        'color':'#000', 'background': 'rgb(241,236,226)'
      }
    }
  },
]

const showEpub = () => {
  rendition.display()
  themes.fontSize(defaultSetting.fontSize + 'px')
  registerTheme()
  setTheme(defaultSetting.theme)
  book.ready.then(()=>{
    navigation = book.navigation
    console.log(navigation)
    return book.locations.generate()
  }).then(result=>{
    console.log(result)
    locations = book.locations
    console.log(locations.total)
    bookAvailable.value = true
  })
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

const registerTheme = () => {
  themeList.forEach(theme => {
    themes.register(theme.name, theme.style)
  })
}

const setTheme = (index) => {
  themes.select(themeList[index].name)
}

const onProgressChange = (progress) => {
  const percentage = progress / 100
  const location = percentage > 0 ? locations.cfiFromPercentage(percentage) : 0
  console.log(location)
  rendition.display(location)
}

const jumpTo = (href) => {
  rendition.display(href)
  hideTitleAndMenu()
}

const hideTitleAndMenu = () => {
  ifTitleAndMenuShow.value = false
  menubar.value.hideSetting()
}

const toggleTitleAndMenu = () => {
  ifTitleAndMenuShow.value = !ifTitleAndMenuShow.value
  if(!ifTitleAndMenuShow.value){
    menubar.value.hideSetting()
  }
}


onBeforeMount(() => {
  showEpub()
  console.log(id)
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

      <MenuBar 
      :ifTitleAndMenuShow="ifTitleAndMenuShow" 
      ref="menubar" 
      @setFontSize="setFontSize" 
      @setTheme="setTheme" 
      :themeList="themeList"
      :bookAvailable="bookAvailable"
      @onProgressChange="onProgressChange"
      @jumpTo = "jumpTo"
      :navigation="navigation"
      ></MenuBar>
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

