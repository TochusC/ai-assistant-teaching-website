<script setup>

import BlankPage from "@/views/BlankPage.vue";
import MyCourseHeader from "@/components/MyAcademyPage/MyCoursePage/MyCourseHeader.vue";
import CourseTabs from "@/components/MyAcademyPage/MyCoursePage/CourseTabs.vue";
import { onMounted ,ref} from "vue";
import router from "@/router/index.ts";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const route = router.currentRoute.value
const courseId = route.params.id //获取到当前界面你需要查询的courseid
const isLoading = ref(true)

const course = ref(null)
onMounted(
  async() => {
    const courseUrl = backendUrl + 'api/course-design/' + courseId
    const response = await axios.get(courseUrl)
    course.value=response.data
    course.value = course.value[0]
    isLoading.value = false
  }
)

</script>

<template>
  <BlankPage>
    <template #default v-if="!isLoading">
      <MyCourseHeader
          :image-url="course.image"
          :name="course.name"
          :illustration="course.illustration"
          :course-id="course.id"
          :progress="70"
      />
      <el-divider/>
      <CourseTabs :course="course"/>
    </template>
    <template #default v-else>
      <el-skeleton :rows="5" />
    </template>
  </BlankPage>
</template>

<style scoped>

</style>