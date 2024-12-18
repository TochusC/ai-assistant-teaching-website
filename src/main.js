import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import 'dayjs/locale/zh-cn'
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import 'element-plus/theme-chalk/dark/css-vars.css'
import 'element-plus/dist/index.css'
import './assets/static/style/modify_element.css'

import Particles from "@tsparticles/vue3";
import { loadFull } from "tsparticles"

import App from './App.vue'
import router from './router/index.js'

import { zhCN, dateZhCN } from 'naive-ui'

import * as echarts from 'echarts';
import naive from 'naive-ui'

const app = createApp(App).use(Particles, {
    init: async engine => {
        await loadFull(engine); // you can load the full tsParticles library from "tsparticles" if you need it
    },
});

app.use(createPinia())
app.use(router)
app.use(naive)
app.use(ElementPlus, {
    locale: zhCn,
})
app.mount('#app')


