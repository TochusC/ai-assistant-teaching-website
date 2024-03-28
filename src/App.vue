<script setup>
import {onMounted, provide, ref} from 'vue'
import UnityComponent from "@/components/UnityComponent.vue";
import UnityInteraction from "@/components/UnityInteraction.vue";
import {useAuth} from "@/assets/static/js/useAuth.js";
import router from "@/router";
import BasicInfo from "@/components/AccountPage/BasicInfo.vue";
import {StarFilled} from "@element-plus/icons-vue";
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
const cdnServerUrl = ref("http://localhost:3000/assests/")
// 是否显示粒子效果
const showParticles = ref(true)

// 提供给子组件的数据
provide('showAssistant', showAssistant);
provide('windowWidth', windowWidth);
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

</script>

<template>
  <div id="AllContainer" >
    <div id="WebsiteContainer" ref="websiteContainer">
      <el-backtop :right="100" :bottom="100" />
        <RouterView v-slot="{ Component }" style="height: 100%">
          <component :is="Component" />
        </RouterView>

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
      :options="{
                    fpsLimit: 120,
                    interactivity: {
                        events: {
                            onClick: {
                                enable: true,
                                mode: 'push'
                            },
                            onHover: {
                                enable: true,
                                mode: 'repulse'
                            },
                        },
                        modes: {
                            bubble: {
                                distance: 400,
                                duration: 2,
                                opacity: 0.8,
                                size: 40
                            },
                            push: {
                                quantity: 2
                            },
                            repulse: {
                                distance: 50,
                                duration: 0.4
                            }
                        }
                    },
                    particles: {
                        color: {
                            value: '#8080ff'
                        },
                        move: {
                            direction: 'down',
                            enable: true,
                            outModes: 'bounce',
                            random: false,
                            speed: 0.4,
                            straight: false
                        },
                        number: {
                            density: {
                                enable: true,
                            },
                            value: 160
                        },
                        opacity: {
                            value: 0.5
                        },
                        shape: {
                            type: 'circle'
                        },
                        size: {
                            value: { min: 2, max: 6 }
                        }
                    },
                    detectRetina: true
                }"
  />
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
