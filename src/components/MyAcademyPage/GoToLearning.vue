<script setup>

import {StarFilled} from "@element-plus/icons-vue";
import ProblemCard from "@/components/MyAcademyPage/GoToLearning/ProblemCard.vue";
import {onMounted, ref} from "vue";
import {useAuth} from "@/assets/static/js/useAuth.js";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";
import {ElNotification} from "element-plus";
import MyCourseCard from "@/components/MyAcademyPage/GoToLearning/MyCourseCard.vue";

const problems = ref([]);
const fetchProblem = async () => {
  const {user} = useAuth()

  const problemUrl = backendUrl + 'student/problem/unfinished/'
      + user.value.school + '/' + user.value.id;
  axios.get(problemUrl)
      .then((res) => {
        problems.value = res.data
      })
      .catch((err) => {
        ElNotification({
          title: '错误',
          message: '获取题目推荐失败' + err,
          type: 'error',
          offset: 64,
          duration: 2000
        })
      })
}

const course = ref([])
const fetchCourse = () => {
  const {user} = useAuth()
  axios.get(backendUrl+'/student/course/' + user.value.ident)
      .then((res) => {
        course.value = res.data
      })
      .catch((err) => {
        ElNotification({
          title: '错误',
          message: '获取课程信息失败' + err,
          type: 'error',
          offset: 64,
          duration: 2000
        })
      })
}

onMounted(
    async () => {
      fetchProblem();
      fetchCourse();
    }
)
</script>

<template>
  <div id="info-div">
    <el-scrollbar style="width: 100%;margin-top:18px; border: 1px solid #8080ff88; border-radius: 8px; box-shadow: 0 0 3px #8080ff">
      <el-divider content-position="left">
        <el-text style="font-size: 22px">
          推荐题目
        </el-text>
      </el-divider>
      <div id="info-container" style="max-width: 720px">
        <ProblemCard  v-for="problem in problems" :problem="problem"/>
      </div>
    </el-scrollbar>
    <div style="width: 100%; display: flex; justify-content: flex-end; margin-top: 16px">
      <el-button type="primary" :icon="StarFilled">点击让小慧换一组推荐题目</el-button>
    </div>
  </div>
  <div id="course-div">
    <el-scrollbar>
      <el-divider content-position="left">
        <el-text style="font-size: 22px">
          我的课程
        </el-text>
      </el-divider>
      <div id="course-container" style="height: 640px">
        <el-scrollbar>
          <MyCourseCard
              style="margin-bottom: 24px"
              v-for="brief in course"
              :brief="brief"/>
        </el-scrollbar>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>
#info-container {
  display: inline-flex;
  padding: 16px
}
#info-div{
  padding-right: 24px;
  height: 100%;
}
</style>