<script setup>
import {onMounted, provide, ref} from 'vue'
import UnityComponent from "@/components/UnityComponent.vue";
import UnityInteraction from "@/components/UnityInteraction.vue";
import {useAuth} from "@/assets/static/js/useAuth.js";
import router from "@/router";
import { NConfigProvider } from 'naive-ui'
import {particleOption} from "@/assets/static/js/particleOption.js";
// 窗口大小
const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)

// 决定是否显示AI助手
const showAssistant = ref(false)
// 按钮的位置
const buttonDynamicLeft = ref('0px')
// 按钮的文字
const buttonText = ref('嗨，小慧！')

// 用来存放Unity组件的引用
const unityComponent = ref(null)
// 是否是深色模式
const isDark = useDark()
const cdnServerUrl = ref("http://localhost:3000/assests/")
// 是否显示粒子效果
const showParticles = ref(true)
import { darkTheme } from 'naive-ui'
import {useDark} from "@vueuse/core";

// 提供给子组件的数据
provide('showAssistant', showAssistant);
provide('windowWidth', windowWidth);
provide('windowHeight', windowHeight);
provide('isDark', isDark);
provide('unityComponent', unityComponent);
provide('cdnServerUrl', cdnServerUrl);
provide('showParticles', showParticles);

// 根据窗口重新计算按钮的位置
function rescaleElement() {
  if(showAssistant.value){
    windowWidth.value = window.innerWidth / 4 * 3;
    windowHeight.value = window.innerHeight;
  }
  else {
    windowWidth.value = window.innerWidth;
  }

  if(showAssistant.value){
    buttonDynamicLeft.value = window.innerWidth / 4 + buttonDynamicLeft.value.length + 'px'
  }
  else {
    buttonDynamicLeft.value = buttonDynamicLeft.value.length + 'px'
  }
}

const { isAuthenticated, user } = useAuth();

onMounted(() => {
  if(isAuthenticated.value !== true){
    router.replace('/login')
  }

  rescaleElement()

  window.addEventListener('resize', () => {
    rescaleElement()
  })
  window.addEventListener('showAssistant', () => {
    rescaleElement()
  })
  window.addEventListener('fullscreenchange', () => {
    const event = new Event('resize')
    window.dispatchEvent(event)
  })
})
const isCallBtnLoading = ref(false)
// 点击按钮，显示或隐藏AI助手
const CallAssistant = () => {
  if(showAssistant.value === false){
    isCallBtnLoading.value = true

    setTimeout(() => {
      isCallBtnLoading.value = false
    }, 2000)
  }

  showAssistant.value = !showAssistant.value

  buttonText.value = showAssistant.value ? '再见，小慧！' : '嗨，小慧！'

  const event = new Event('showAssistant')
  window.dispatchEvent(event)
}

const handleChangeRemoteServer = (id) => {
  console.log(id)
}

const themeOverrides = {
  common: {
    primaryColor: '#8080ff',
    infoColor: '#8080ff',
    successColor: 'var(--el-color-success)',
    warningColor: 'var(--el-color-warning)',
    errorColor: 'var(--el-color-error)',
  },
}

const darkThemeOverrides = {
  common: {
    primaryColor: '#8080ff',
    infoColor: '#8080ff',
  },
}
</script>

<template>
  <el-backtop :right="100" :bottom="100" />
  <div id="AllContainer" >
    <div id="WebsiteContainer" ref="websiteContainer">
      <el-backtop :right="100" :bottom="100" />
      <n-config-provider style="height: 100%" :theme-overrides="isDark?darkThemeOverrides:themeOverrides" :theme="isDark?darkTheme:''">
          <RouterView />
      </n-config-provider>
      <el-button
          type="primary"
          class="floating-button"
          size="large"
          :loading="isCallBtnLoading"
          :style="{right: buttonDynamicLeft}"
          @click="CallAssistant" round>
        {{ buttonText }}
      </el-button>
    </div>

  <!--    用来存放AI教学助理的容器-->
    <div id="AssistantContainer">
      <el-watermark
          :content="'通慧智教'">
      <UnityInteraction
          :is-call-btn-loading="isCallBtnLoading"
          :show-assistant="showAssistant"
          @changeRemoteServer="handleChangeRemoteServer"
          />
        <UnityComponent
            ref="unityComponent"
            v-if="showAssistant"
            :initial-unity-canvas-height="windowHeight - 48"
            :initial-unity-canvas-width="windowWidth / 3"
        />
      </el-watermark>
    </div>
  </div>

  <vue-particles
      v-if="showParticles"
      id="tsparticles"
      :options="particleOption"
  />
</template>

<style scoped>

#AllContainer {
  display: flex;
  width: 99%;
  height: 100%;
}

#WebsiteContainer {
  flex: 3;
  height: 100%;
  z-index: 2;
  width: 100%;
}
#AssistantContainer {
  position: relative;
  flex: 0;
  z-index: 2;
  transition: 0.5s;
  border: 1px solid #ccc;
  height: 100%;
}

.floating-button {
  position: absolute;
  bottom: 50%
}
#tsparticles {
  position: fixed;
  margin: 0;
  padding: 0;
  left: 0;
  top: 0;
  z-index: 0;
  width: 100%;
  height: 100%;
}
</style>
