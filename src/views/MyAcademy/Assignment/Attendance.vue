<script setup lang="ts">
import {useRoute} from "vue-router";
import {SuccessFilled, CircleCloseFilled, Loading} from "@element-plus/icons-vue";
import BlankPage from "@/views/BlankPage.vue";
import {ref} from "vue";
import router from "@/router/index.js";

const route = useRoute()

const attendanceId = route.params.id

const attendance = {
  id: 1,
  name: "第一次课堂考勤",
  description: "常规考勤",
  type:"常规考勤",
  startTime: "2024.03.16 21:23",
  endTime: "2024.04.15 00.00",
  announceTime: "2024.03.16 21:23",
  course: {
    id: 1,
    name: "计算机网络原理"
  },
  allowDelay: true,
  allowRedo: true,
}

const handleCheckAttendance = ()=>{
  showAttendance.value=false;
  attendanceConfirm.value=true
}

const userInput = ref("")
const showAttendance = ref(true)
const attendanceConfirm = ref(false)
</script>

<template>
  <BlankPage>
    <template #default>
      <div style="width: 100%; height: 100%;" class="Center-Flex">
        <div v-if="attendanceConfirm" class="Center-Flex" style="flex-direction: column;">
          <el-icon :size="100" color="#67c23a"><SuccessFilled /></el-icon>
          <h1 style="margin: 24px">签到成功!</h1>
          <el-button style="width: 128px" type="primary" @click="router.push('/academy')">
            返回
          </el-button>
        </div>

        <div v-if="!attendanceConfirm && !showAttendance" class="Center-Flex" style="flex-direction: column;">
          <el-icon :size="100" color="#f56c6c"><CircleCloseFilled /></el-icon>
          <h1 style="margin: 24px">签到失败!</h1>
          <el-button style="width: 128px" type="primary" @click="showAttendance=true">
            重新签到
          </el-button>
        </div>

        <div v-if="showAttendance" class="Center-Flex" style="flex-direction: column;">
          <el-icon :size="100" class="is-loading" color="#8080ef"><Loading /></el-icon>
          <h1 style="margin: 24px">签到中...</h1>
        </div>
      </div>
    </template>
  </BlankPage>
  <el-dialog v-model="showAttendance" :width="380" style="border: 1px solid #1a1a1a; padding: 36px; border-radius: 32px">
    <div style="width: 100%; height: 400px; flex-direction: column" class="Center-Flex">
      <div class="Center-Flex" style="flex-direction: column;">
        <h1>{{ attendance.course.name }}</h1>
        <h3 style="margin-top: 32px; margin-bottom: 8px">{{attendance.name}}</h3>
        <el-text style="margin-bottom: 16px">{{attendance.description}}</el-text>

        <el-button type="primary" style="margin: 32px; height: 64px; width: 128px" size="large" round @click="handleCheckAttendance">考勤签到</el-button>
        <el-tag effect="plain" type="info" style="margin: 12px 12px 12px 0px">
          {{ attendance.startTime }} - {{ attendance.endTime }}
        </el-tag>
      </div>
    </div>
  </el-dialog>
</template>

<style scoped>

</style>