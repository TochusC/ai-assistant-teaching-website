<template>
  <div class="Header-Container" >
    <div class="Header-Item" ref="logoContainer">
      <el-popover
          placement="top-start"
          :width="200"
          trigger="hover"
      >
        <template #reference @click="toMainPage">
          <img
              class="website-logo"
              src="@/assets/static/img/logo/favicon.png"
              alt=""
          />
        </template>
        <span style=" white-space: nowrap;">守得云开见月明</span>
        <span>
          <el-switch
              v-model="showParticles"
              style="margin-left: 22px"
              inline-prompt
              :active-icon="MoonNight"
              :inactive-icon="Sunset"
          />
        </span>
      </el-popover>
      <div class="Multiple-Header-Item-Container" @click="toMainPage">
        <h1 class="keyword">
          通慧智教 |
        </h1>
        <h1 class="tittle" ref="tittle">
          &nbsp 有温度、有感情的个性化智能教学平台
        </h1>
      </div>
    </div>


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

        <el-button
            plain
            :type="route.path==='/'?'primary':'default'"
            style="margin-right: 24px">
          <el-link type="primary"
                   style="
                       font-size: 18px;
                        white-space: nowrap;
                       font-weight: bolder"
                   @click="handleToMainPage"
          >首页</el-link>
        </el-button>

        <el-popover placement="bottom-start">
          <template #reference>
            <el-badge :value="3" style="margin-right: 36px">
              <el-button
                  :type="route.path==='/academy'?'primary':'default'"
                  plain>
                <el-link type="primary"
                         style="
                       font-size: 18px;
                        white-space: nowrap;
                       font-weight: bolder"
                         @click="handleToTeachingPortal"
                >教学首页</el-link>
              </el-button>
            </el-badge>
          </template>
          <div class="Space-Between-Flex">
            <el-statistic title="课程" :value="1" />
            <el-statistic title="考勤" :value="1" />
          </div>
          <el-statistic title="待完成作业" :value="1" />
        </el-popover>
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
              src="@/assets/static/img/boy.png" alt="" style="height:52px; width: auto"/>
        </template>
        <el-menu>
          <el-menu-item @click="toUserCenter" index="1">个人中心</el-menu-item>
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
import {MoonNight, Sunset, Search} from "@element-plus/icons-vue";
import router from "@/router/index.ts";
import LogoutDialog from "@/components/MainPage/LogoutDialog.vue";
import {useRoute} from "vue-router";
import {ElMessage, ElNotification} from "element-plus";


const tittle = ref(null)
const isCollapse = ref(true)
const showLogoutDialog = ref(false)
const showParticles = inject('showParticles')

const showSearchSelection = ref(true)
// 响应式搜索栏宽度
const dynamicSearchBarWidth = ref('560px')

const toUserCenter = () => {
  if(route.path === '/user'){
    ElNotification({
      message: '你已经在个人中心啦',
      type: 'success',
      offset: 64,
      duration: 1000
    })
    return
  }
  else{
    router.push('/user')
  }
}

// 注入全局状态
const showAssistant = inject('showAssistant')
const isDark = useDark()

// 盛放页面Logo和Mine的容器
const logoContainer = ref(null)
const mineContainer = ref(null)

const windowWidth = ref(null)
const windowHeight = ref(null)

const notification = [
  {
    type: '作业',
    num: 1,
  }
]

const toMainPage = () => {
  router.push('/')
}
// 响应式调整元素
const rescaleElement = () => {
  if(showAssistant.value){
    windowWidth.value = window.innerWidth / 4 * 3;
  }
  else {
    windowWidth.value = window.innerWidth;
  }

  dynamicSearchBarWidth.value = (windowWidth.value - logoContainer.value.offsetWidth - mineContainer.value.offsetWidth) * 0.75 + 'px'


  if (windowWidth.value < 764) {
    tittle.value.style.fontSize = '0px';
    isCollapse.value = true;
  }
  else {
    tittle.value.style.fontSize = '18px'
    isCollapse.value = false
  }
}

const route = useRoute();

onMounted(() => {
  rescaleElement()

  window.addEventListener('resize', () => {
    rescaleElement()
  })
  window.addEventListener('showAssistant', () => {
    rescaleElement()
  })
})

const handleToTeachingPortal = () => {
  if(route.path === '/teaching/portal'){
    ElNotification({
      message: '您已经在教学首页啦',
      type: 'success',
      offset: 64,
      duration: 1000
    })
    return
  }
  router.push("/academy")
}
const handleToMainPage = () => {
  if(route.path === '/portal'){
    ElNotification({
      message: '你已经在首页啦',
      type: 'success',
      offset: 64,
      duration: 1000
    })
    return
  }
  router.push("/")
}
</script>

<style scoped>
.website-logo {
  cursor: pointer;
  height: 64px;
  margin-right: 12px;
  width: auto;
}
.Header-Container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  box-shadow: 0 0 8px #8080ff;
  background: var(--el-bg-color);
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
}
html.dark .Header-Container{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  box-shadow: 0 0 4px var(--el-color-primary);
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
}

.Multiple-Header-Item-Container{
  cursor: pointer;
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

.Header-Item {
  display: inline-flex;
}

.tittle{
  transition: 0.5s;
  font-size: 18px;
  white-space: nowrap;
}
.tittle:hover{
  white-space: nowrap;
}
.keyword{
  transition: 0.5s;
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

html.dark .keyword:hover{
  white-space: nowrap;
  font-size: 24px;
  text-shadow: 0 0 24px #fff;
  color: #dedede;
}
</style>