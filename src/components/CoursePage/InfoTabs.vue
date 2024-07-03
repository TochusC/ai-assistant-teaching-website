<script setup>
import CourseDesign from "@/components/CoursePage/TabPane/CourseDesign.vue";
import OnlineTutorial from "@/components/CoursePage/TabPane/OnlineTutorial.vue";
import {ChatLineSquare, DataBoard, Edit, MessageBox, Monitor, Tickets} from "@element-plus/icons-vue";
import CourseAnnouncement from "@/components/CoursePage/TabPane/CourseAnnouncement.vue";
import CourseQA from "@/components/CoursePage/TabPane/CourseQA.vue";
import CourseResources from "@/components/CoursePage/TabPane/CourseResources.vue";
import CourseHomework from "@/components/CoursePage/TabPane/CourseHomework.vue";
import {onMounted} from "vue";

const props = defineProps({
  course:{
    required: true
  },
  chapters:{
    required: true
  },
  announcements:{
    required: true
  },
  questions:{
    required: true
  },
  resources:{
    required: true
  },
  assignments:{
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

      <CourseDesign
          :background="props.course.background"
          :target="props.course.target"
          :principle="props.course.principle"
      />
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
      <OnlineTutorial :chapters="props.chapters"/>
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

      <CourseAnnouncement :announcement="props.announcements"/>
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
      <CourseQA :qa="props.questions"/>
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
      <CourseResources :resources="props.resources"/>
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
      <CourseHomework :homework="props.assignments"/>
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