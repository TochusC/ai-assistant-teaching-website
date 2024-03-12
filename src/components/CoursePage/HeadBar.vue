<template>
  <div class="Header-Container" >
    <div class="Header-Item" ref="logoContainer">
      <el-popover
          placement="top-start"
          :width="200"
          trigger="hover"
      >
        <template #reference>
          <img
              class="icon"
              src="../../assets/static/img/unity-logo-light.png" alt="" style="height:64px; width: auto"/>
        </template>
        <span style=" white-space: nowrap;">守得云开见月明</span>
        <span>
      <el-switch
          v-model="isDark"
          @change="$emit('changeTheme', isDark)"
          style="margin-left: 22px"
          inline-prompt
          :active-icon="MoonNight"
          :inactive-icon="Sunset"
      /></span>
      </el-popover>
      <div class="Multiple-Header-Item-Container">
        <h1 class="keyword">
          AI赋能 |
        </h1>
        <h1 class="tittle">
          &nbsp 智能教学运营服务平台
        </h1>
      </div>
    </div>

    <el-divider direction="vertical" />

    <div class="Header-Item" :style="{width:dynamicSearchBarWidth}">
      <el-input
          placeholder="搜索更多好课..."
          class="input-with-select"
          size="large"
      >
        <template #prepend>
          <el-select  placeholder="搜索内容" style="width: 115px" size="large">
            <el-option label="课程" value="1" />
            <el-option label="文章" value="2" />
            <el-option label="视频" value="3" />
          </el-select>
        </template>
        <template #append>
          <el-button :icon="Search" size="large"/>
        </template>
      </el-input>
    </div>

    <el-divider direction="vertical" />

    <div class="Header-Item" style="margin-right: 24px" ref="mineContainer">

      <div class="Multiple-Header-Item-Container">

      <el-switch
          v-model="isDark"
          style="margin-right: 38px"
          size="large"
          inline-prompt
          :active-icon="MoonNight"
          :inactive-icon="Sunset"
      />

      <el-link type="primary"
               style="margin-right: 36px;
               font-size: 20px;
                white-space: nowrap;
               font-weight: bolder"
      >我的学堂</el-link>

      </div>

<!--          头像-->
      <el-popover
          placement="top-start"
          :width="160"
          trigger="hover"
      >
        <template #reference>
          <img
              class="icon"
              src="../../assets/static/img/boy.png" alt="" style="height:64px; width: auto"/>
        </template>
        <el-menu>
          <el-menu-item index="1">个人中心</el-menu-item>
          <el-menu-item @click="showLogoutDialog=true">退出登录</el-menu-item>
        </el-menu>
      </el-popover>

    </div>

  </div>
  <LogoutDialog v-model="showLogoutDialog"/>
</template>

<script setup>
import {ref, onMounted, inject} from 'vue'
const activeIndex = ref('1')
import { useDark } from '@vueuse/core'
import {MoonNight, Star, Sunset, Search} from "@element-plus/icons-vue";
import router from "@/router";
import LogoutDialog from "@/components/MainPage/LogoutDialog.vue";

const tittle = ref(null)
const isCollapse = ref(true)
const showLogoutDialog = ref(false)

// 响应式搜索栏宽度
const dynamicSearchBarWidth = ref('560px')

// 注入全局状态
const showAssistant = inject('showAssistant')
const isDark = useDark()

// 盛放页面Logo和Mine的容器
const logoContainer = ref(null)
const mineContainer = ref(null)

const windowWidth = ref(null)
const windowHeight = ref(null)

// 响应式调整元素
const rescaleElement = () => {
  if(showAssistant.value){
    windowWidth.value = window.innerWidth / 4 * 3;
  }
  else {
    windowWidth.value = window.innerWidth;
  }

  dynamicSearchBarWidth.value = windowWidth.value / 4 * 3 - logoContainer.value.offsetWidth - mineContainer.value.offsetWidth + 'px'

  if (windowWidth < 620) {
    if(tittle.value){
      tittle.value.style.fontSize = '0px'
    }
  }
  else {
    if(tittle.value) {
      tittle.value.style.fontSize = '18px'
    }
    isCollapse.value = false
  }
}

onMounted(() => {
  rescaleElement()

  window.addEventListener('resize', () => {
    rescaleElement()
  })
  window.addEventListener('showAssistant', () => {
    rescaleElement()
  })
})

const handleLogout = () => {

}
</script>

<style scoped>

.Header-Container {
  width: 100%;
  margin: 0px;
  padding-top: 36px;
  padding-bottom: 36px;
  box-shadow: 0 0 4px #101010;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.Multiple-Header-Item-Container{
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

.Header-Item {
  display: inline-flex;
}

.tittle{
  color: #000000;
  font-size: 18px;
  white-space: nowrap;
}
.tittle:hover{
  color: #101010;
  white-space: nowrap;
}
.keyword{
  white-space: nowrap;
  text-shadow: 0 0 36px #fff;
  color: #8080FF;
}
.keyword:hover{
  white-space: nowrap;
  font-size: 24px;
  text-shadow: 0 0 24px #fff;
  color: #4242e0;
}
</style>