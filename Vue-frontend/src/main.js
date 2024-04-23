import { createApp } from 'vue'
import { provide, ref, nextTick } from 'vue'
import ElementPlus from 'element-plus'
import naive from 'naive-ui'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './components/router/router'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import './assets/font/font.css'
import './assets/css/element.css'

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.use(naive)
app.mount('#app')
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
