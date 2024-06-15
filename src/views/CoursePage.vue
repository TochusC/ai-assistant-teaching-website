<script setup>
import router from "@/router/index.ts";
import HeadNavi from "@/components/utils/HeadNavi.vue";
import InfoTabs from "@/components/CoursePage/InfoTabs.vue";
import CourseHeader from "@/components/CoursePage/CourseHeader.vue";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig";

import {inject, onMounted, ref} from "vue";
import {ElMessage} from "element-plus";

const route = router.currentRoute.value
const courseId = route.params.id

const course = ref({})
const statistics = ref({})
const chapters = ref({})
const announcements = ref({})
const questions = ref({})
const resources = ref({})
const assignments = ref({})

const info = ref({
  course: null,
  statistics: null,
  chapters: null,
  announcements: null,
  questions: null,
  resources: null,
  assignments: null,
})

const fetchInfo= (infoName) => {
  axios.get(backendUrl + 'course/'+ infoName + '/' + courseId)
      .then((res) => {
        info.value[infoName] = res.data;
      })
      .catch((err) => {
        console.log(err)
      })
  isLoading.value = false
}

const dynamicBannerPadding = ref(128)
const windowWidth = inject("windowWidth")
const updatePadding = () => {
  // 示例：根据窗口宽度动态调整padding值
  dynamicBannerPadding.value = windowWidth.value / 2000 * 164;
  if(windowWidth.value < 1024){
    dynamicBannerPadding.value = 16
  }
};
const rescaleElements = ()=>{
  updatePadding();
}

const tittle = ref(null)
const isLoading = ref(true)

onMounted(()=>{
  rescaleElements()
  setTimeout(() => {
    if(tittle.value){
      tittle.value.style.letterSpacing = '4px'
    }
  }, 500);
  window.addEventListener('resize',  rescaleElements);
  fetchInfo('course')
  fetchInfo('statistics')
  fetchInfo('chapters')
  fetchInfo('announcements')
  fetchInfo('questions')
  fetchInfo('resources')
  fetchInfo('assignments')

})


</script>

<template>
  <el-container>
    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>
    <el-main
        v-loading="isLoading"
        :style="{ paddingLeft: dynamicBannerPadding + 'px',
         paddingRight: dynamicBannerPadding + 'px'}"
         >
      <div id="banner">
        <div id="decorative-divider" >
          <h1 ref="tittle" id="tittle">{{ course.name }}</h1>
          <p id="illustration">
            {{ course.illustration }}
          </p>
        </div>
      </div>
      <div class="Center-Flex">
        <div id="course-info-container">
          <CourseHeader
              :image-url="course.image"
              :introduction="course.introduction"
              :statistics="statistics"
          />

          <el-divider id="add-course-divider">
            <el-button round style="width: 180px"
                       type="primary">加入课程</el-button>
          </el-divider>
          <InfoTabs :course="course"/>
        </div>
      </div>
    </el-main>
  </el-container>

</template>

<style scoped>
#add-course-divider{
  margin-top: 48px;
  margin-bottom: 48px;
}
#banner{
  margin-top: 16px;
  background: radial-gradient(circle,
  var(--el-color-primary),
  var(--el-color-primary-light-3));
  border-radius: 8px;
  box-shadow: #8080FF 0 0 16px;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 128px;
  padding-bottom: 24px;
  transition: 0.5s;
}
#tittle{
  color: var(--el-color-white);
  font-size: 32px;
  margin-bottom: 12px;
  letter-spacing: 0px;
  transition: 1s;
}
#illustration{
  color: var(--el-color-white);
  font-size: 14px;
}

#course-info-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 8px;
  margin: -24px 128px 0px;
  flex-direction: column;
  padding: 32px;
  background: var(--el-bg-color);
}

#decorative-divider{
  padding-left: 18px;
  padding-right: 18px;
  border-left: #efefefaa 1px solid;
  border-right: #efefefaa 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>