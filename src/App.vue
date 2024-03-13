<script setup lang="ts">
import {onMounted, provide, ref} from 'vue'
import UnityComponent from "@/components/UnityComponent.vue";
import MainPage from "@/views/MainPage.vue";
import LoginPage from "@/views/LoginPage.vue";

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
const isDark = ref(false)


// 提供给子组件的数据
provide('showAssistant', showAssistant);
provide('windowWidth', windowWidth);
provide('isDark', isDark);

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

onMounted(() => {
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

// 点击按钮，显示或隐藏AI助手
const CallAssistant = () => {
  showAssistant.value = !showAssistant.value

  buttonText.value = showAssistant.value ? '再见，小慧！' : '嗨，小慧！'

  const event = new Event('showAssistant')
  window.dispatchEvent(event)
}
</script>

<template>
  <div id="AllContainer">
      <div id="WebsiteContainer">
        <RouterView/>
          <el-button
              type="primary"
              class="floating-button"
              size="large"
              :style="{right: buttonDynamicLeft}"
              @click="CallAssistant" round>
            {{ buttonText }}
          </el-button>
      </div>

  <!--    用来存放AI教学助理的容器-->
      <div id="AssistantContainer">
          <UnityComponent
              ref="unityComponent"
              v-if="showAssistant"
              :initial-unity-canvas-height="windowHeight - 48"
              :initial-unity-canvas-width="windowWidth / 3"
          />
      </div>
    </div>
</template>

<style scoped>

#AllContainer {
  display: flex;
  width: 100%;
  height: 100%;
}

#WebsiteContainer {
  flex: 3;
  height: 100%;
  width: 100%;
}
#AssistantContainer {
  flex: 0;
  transition: 0.5s;
  border: 1px solid #ccc;
  height: 100%;
}

.floating-button {
  position: absolute;
  bottom: 50%
}

</style>
