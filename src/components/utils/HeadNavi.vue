<template>
  <StudentHeadNavi v-if="user.role === 'student'"/>
  <TeachHeadNavi v-else-if="user.role === 'teacher'"/>
  <ParentHeadNavi v-else/>
  <LogoutDialog v-model="showLogoutDialog"/>
</template>

<script setup>
import {ref, onMounted, inject} from 'vue'
import LogoutDialog from "@/components/MainPage/LogoutDialog.vue";
import {useRoute} from "vue-router";
import {useAuth} from "@/assets/static/js/useAuth.js";
import TeachHeadNavi from "@/components/TeachingActivity/utils/TeachHeadNavi.vue";
import ParentHeadNavi from "@/components/ParentPage/ParentHeadNavi.vue";
import StudentHeadNavi from "@/components/MyAcademyPage/StudentHeadNavi.vue";


const tittle = ref(null)
const { user } = useAuth()
const isCollapse = ref(true)
const showLogoutDialog = ref(false)

// 注入全局状态
const showAssistant = inject('showAssistant')

const windowWidth = inject('windowWidth');
// 响应式调整元素
const rescaleElement = () => {
  if(tittle.value === null) return
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
  rescaleElement();
  window.addEventListener('resize', () => {
    rescaleElement();
  })
  window.addEventListener('showAssistant', () => {
    rescaleElement();
  })
})


</script>

<style scoped>
html.dark .Header-Container{
  width: 100%;
  height: 100%;
  box-shadow: 0 0 4px var(--el-color-primary);
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
}

html.dark .keyword:hover{
  white-space: nowrap;
  font-size: 24px;
  text-shadow: 0 0 24px #fff;
  color: #dedede;
}
</style>