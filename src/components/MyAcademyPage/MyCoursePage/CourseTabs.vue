<script setup>

import OnlineTutorial from "@/components/CoursePage/TabPane/OnlineTutorial.vue";
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import QACard from "@/components/MyAcademyPage/MyCoursePage/CourseTabs/QACard.vue";
import {Star} from "@element-plus/icons-vue";
import {onMounted, ref} from "vue";
import QuestionDialog from "@/components/MyAcademyPage/MyCoursePage/CourseTabs/QACard/QuestionDrawer.vue";
import FormulatingQuestionDialog from "@/components/MyAcademyPage/MyCoursePage/CourseTabs/FormulatingQuestionDialog.vue";

const props = defineProps({
  course: {
    type: Object,
    required: true
  }
})

onMounted(()=>{
  console.log(props.course)
})
const activeTab = ref('resource')
const qaDynamicClass = ref('default')
const qaLogoDynamicClass = ref('default')
const handleChangeTab = () => {
  if(activeTab.value === 'qa'){
    qaDynamicClass.value = 'primary_tab'
    qaLogoDynamicClass.value = 'is-loading'
  }
  else {
    qaDynamicClass.value = 'default'
    qaLogoDynamicClass.value = 'default'
  }
}


const notice = [
  {
    id: 1,
    type: "作业",
    tittle: "第一次课堂作业",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 1,
    type: "考勤",
    tittle: "第一次课堂考勤",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 1,
    type: "课程",
    tittle: "第一章课程",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
]


const showQuestionDialog = ref(false)
</script>

<template>
  <el-tabs
      v-model="activeTab"
      style="width: 100%"
      @tab-change="handleChangeTab"
  >
    <el-tab-pane label="学习资源" name="resource">
      <OnlineTutorial :catalog="props.course.catalog"/>
    </el-tab-pane>
    <el-tab-pane label="学习任务" name="assignment">
      <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
    </el-tab-pane>
    <el-tab-pane label="作业考试" name="exam">

      <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
    </el-tab-pane>
    <el-tab-pane  label="问答讨论" name="qa">
      <template #label>
        <el-badge value="AI" type="primary">
          <el-text :class="qaDynamicClass">
            问答讨论
            <el-icon :class="qaLogoDynamicClass">
              <Star/>
            </el-icon >
          </el-text>
        </el-badge>
      </template>
      <QACard style="margin-bottom: 24px"/>
      <div class="Center-Flex">
        <el-button type="success" style="width: 24%" @click="showQuestionDialog=true">我有问题！</el-button>
      </div>
      <FormulatingQuestionDialog v-model="showQuestionDialog"/>
    </el-tab-pane>
  </el-tabs>
</template>

<style scoped>
.primary_tab{
  color: var(--el-color-primary)
}
</style>