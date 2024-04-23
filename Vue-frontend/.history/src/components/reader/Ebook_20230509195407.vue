

<script setup>
import { defineProps, onBeforeMount, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { ChevronBack, ChevronForward } from '@vicons/ionicons5'
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
const ifPrevPageShow = ref(false)
const ifNextPageShow = ref(false)

var book = new ePub(URL)
var rendition = book.renderTo('read', {
  width: "800",
  height: window.innerHeight, // 分页模式下 最好固定宽高
  flow: "paginated",
  spread: 'none', // none-单栏 both-两栏
  allowScriptedContent: true,
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
        'color':'#000', 'background': '#f0f2f5;'
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

const leftEnter = () => {
  ifPrevPageShow.value = true
}

const leftLeave = () => {
  ifPrevPageShow.value = false
}

const rightEnter = () => {
  ifNextPageShow.value = true
}

const rightLeave = () => {
  ifNextPageShow.value = false
}

onBeforeMount(() => {
  // showEpub()
  // console.log(id)
  rendition.display();
})


</script>

<template>
  <!-- <div id="read"></div> -->
  <div>

    <div class="ebook">
    <TitleBar :ifTitleAndMenuShow="ifTitleAndMenuShow" :id="id"></TitleBar>

      <div class="read_wrapper">
        <div id="read"></div>
        <div class="mask">
          <div class="left" @click="prevPage" @mouseenter="leftEnter" @mouseleave="leftLeave">
            <n-icon :component="ChevronBack" size="40" color="black" v-if="ifPrevPageShow" />
          </div>
          <div class="center" @click="toggleTitleAndMenu"></div>
          <div class="right" @click="nextPage" @mouseenter="rightEnter" @mouseleave="rightLeave">
            <n-icon :component="ChevronForward" size="40" color="black" v-if="ifNextPageShow" />
          </div>
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
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.mask .left:hover {
  background-color: rgba(68, 68, 68, 0.5);
}

.mask .center {
  flex: 1;
  display: flex;
  justify-content: center;
}

.mask .right {
  width: 200px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}


.mask .right:hover {
  background-color: rgba(126, 126, 126, 0.2);
}

.epub-view{
  width: 600px !important;
}

#id{
  width: 600px;
}
</style>

