<script setup lang="ts">

import {StarFilled} from "@element-plus/icons-vue";
import QuestionDrawer from "@/components/MyAcademyPage/MyCoursePage/CourseTabs/QACard/QuestionDrawer.vue";
import {ref} from "vue";

const qa = {
  id: 1,
  question: "当数据包在网络中传输时，用于确定数据包的最佳路径的协议是什么？",
  date: "2024-03-27",
  aiAnswer: "用于确定数据包的最佳路径的协议是路由协议，例如常见的协议有OSPF（Open Shortest Path First）、RIP（Routing Information Protocol）和BGP（Border Gateway Protocol）。",
  user: "通慧小助手",
}

const showQuestionDrawer = ref(false)


</script>

<template>

  <el-card shadow="hover">
      <div class="Space-Between-Flex"
           style="margin-bottom: 32px; width: 100%"
      >
        <el-text truncated size="large" style="color:var(--el-color-primary)">
          {{qa.question}}
        </el-text>
        <div style="white-space: nowrap">
          <el-tag type="info" effect="plain" style="margin-right: 12px">
            {{qa.date}}
          </el-tag>
          <el-tag type="primary" effect="plain">
            提问：{{qa.user}}
          </el-tag>
        </div>
      </div>
    <el-divider/>
    <div class="Space-Between-Flex">
      <div>

        <el-text truncated: line-clamp="2" style="max-width: 1024px" class="description-text">
          <el-text style="white-space: nowrap" type="primary">
            <el-icon><StarFilled/></el-icon>
            小慧（AI精调回答）：
          </el-text>
          {{qa.aiAnswer}}
        </el-text>
      </div>
      <el-button type="primary" @click="showQuestionDrawer=true" style="width: 128px">查看问题</el-button>
    </div>
    <QuestionDrawer v-model="showQuestionDrawer"/>
  </el-card>
</template>

<style scoped>

</style>