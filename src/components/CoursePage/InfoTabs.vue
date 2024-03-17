<script setup lang="ts">

import CourseDesign from "@/components/CoursePage/TabPane/CourseDesign.vue";
import OnlineTutorial from "@/components/CoursePage/TabPane/OnlineTutorial.vue";
import {ChatLineSquare, DataBoard, Edit, MessageBox, Monitor, Tickets} from "@element-plus/icons-vue";
import CourseAnnouncement from "@/components/CoursePage/TabPane/CourseAnnouncement.vue";
import CourseQA from "@/components/CoursePage/TabPane/CourseQA.vue";
import CourseResources from "@/components/CoursePage/TabPane/CourseResources.vue";
import CourseHomework from "@/components/CoursePage/TabPane/CourseHomework.vue";

const props = defineProps({
  course:{
    type: Object,
    required: true
  }
})
</script>

<template>
  <el-tabs
      id="info-tabs"
      tab-position="left">

    <el-tab-pane>
      <template #label>
                <span>
                  <el-icon class="tab-icon"><Edit /></el-icon>
                  <span>课程设计</span>
                </span>
      </template>

      <CourseDesign :design="props.course.design"/>
    </el-tab-pane>

    <el-tab-pane>
      <template #label>
                <span>
                  <el-icon class="tab-icon">
                    <Monitor />
                  </el-icon>
                  <span>在线教程</span>
                </span>
      </template>
      <OnlineTutorial :catalog="props.course.catalog"/>
    </el-tab-pane>

    <el-tab-pane>
      <template #label>
                <span>
                  <el-icon class="tab-icon">
                    <DataBoard />
                  </el-icon>
                  <span>课程公告</span>
                </span>
      </template>

      <CourseAnnouncement :announcement="props.course.announcement"/>
    </el-tab-pane>

    <el-tab-pane>
      <template #label>
                <span>
                  <el-icon class="tab-icon">
                    <ChatLineSquare />
                  </el-icon>
                  <span>课程问答</span>
                </span>
      </template>
      <CourseQA :qa="course.qa"/>
    </el-tab-pane>

    <el-tab-pane>
      <template #label>
        <span>
          <el-icon class="tab-icon">
            <MessageBox />
          </el-icon>
          <span>课程资源</span>
        </span>
      </template>
      <CourseResources :resources="course.resources"/>
    </el-tab-pane>

    <el-tab-pane>
      <template #label>
                <span>
                  <el-icon class="tab-icon">
                    <Tickets />
                  </el-icon>
                  <span>作业测试</span>
                </span>
      </template>
      <CourseHomework :homework="course.homework"/>
    </el-tab-pane>
  </el-tabs>
</template>

<style scoped>
#info-tabs{
  width: 100%;
  height: 600px;
  border-radius: 8px;
}
.tab-icon{
  margin-right: 6px;
}
</style>