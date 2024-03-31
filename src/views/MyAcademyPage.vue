<script setup>
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {inject, onMounted, ref, watch} from "vue";
import axios from "axios";
import * as echarts from 'echarts/core';
import { useThemeVars } from 'naive-ui'
import AIOpinion from "@/components/utils/AIOpinion.vue";
import {ElMessage} from "element-plus";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import {StarFilled} from "@element-plus/icons-vue";
import AITextLong from "@/components/utils/AITextLong.vue";

const themeVars = useThemeVars()
const {user} = useAuth();

const notice = [
  {
    id: 1,
    type: "简答",
    tittle: "网络结构基础",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 1,
    type: "课程",
    tittle: "应用层基础",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 3,
    type: "简答",
    tittle: "TCP数据报",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 4,
    type: "简答",
    tittle: "TCP数据报",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 5,
    type: "简答",
    tittle: "TCP数据报",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
]

const learning_activity = [
  {
    name: '计算机网络原理',
    data: [120, 132, 101, 134, 90, 230, 210]
  },
  {
    name: '计算机组成原理',
    data: [220, 182, 191, 234, 290, 330, 310]
  },
  {
    name: '操作系统',
    data: [150, 232, 201, 154, 190, 330, 410]
  },
  {
    name: '数据结构',
    data: [320, 332, 301, 334, 390, 330, 320]
  },
  {
    name: '总学习时长',
    data: [820, 932, 901, 934, 1290, 1330, 1320]
  }
]

const course_progress = [
  {course: '计算机网络原理', progress: 90},
  {course: '计算机组成原理', progress: 70},
  {course: '操作系统', progress: 50},
  {course: '数据结构', progress: 10},
]

const isDark = inject('isDark')

const course_brief = ref([])
const chartContainer = ref(null)

let myChart = null
const option = { // 指定图表的配置项和数据
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['总学习时长', '计算机网络原理', '计算机组成原理', '操作系统', '数据结构']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['2024-03-22', '2024-03-23', '2024-03-24', '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '计算机网络原理',
      type: 'line',
      smooth: true,
      stack: 'Total',
      data: [120, 132, 101, 134, 90, 230, 210]
    },
    {
      name: '计算机组成原理',
      type: 'line',
      stack: 'Total',
      smooth: true,
      data: [220, 182, 191, 234, 290, 330, 310]
    },
    {
      name: '操作系统',
      type: 'line',
      stack: 'Total',
      smooth: true,
      data: [150, 232, 201, 154, 190, 330, 410]
    },
    {
      name: '数据结构',
      type: 'line',
      stack: 'Total',
      smooth: true,
      data: [320, 332, 301, 334, 390, 330, 320]
    },
    {
      name: '总学习时长',
      type: 'line',
      stack: 'Total',
      smooth: true,
      data: [820, 932, 901, 934, 1290, 1330, 1320]
    }

  ]
};


onMounted( //用户选课信息已经初始化了
  async() => {
    const formData = new URLSearchParams();
    let GetLessonUrl = backendUrl + 'api/choose/' + user.value.id;
    const response = await axios.get(GetLessonUrl);
    const resource = response.data;
    for (let lesson of resource){
      //console.log(lesson.Lesson_id) //用户选课的id
      let GetClassUrl = backendUrl + 'api/course/' + lesson.Lesson_id;
      const course = await axios.get(GetClassUrl)
      const CouseData = course.data
      console.log("brief数据",CouseData[0])
      course_brief.value.push(CouseData[0])
    }

    initChart()

    watch(isDark, (newVal) => {
     initChart()
    })

    window.addEventListener('resize', () => {
      myChart.resize()
    })

    window.addEventListener('showAssistant', () => {
      myChart.dispose()
      setTimeout(() => {
        initChart()
      }, 200)
    })
  }
)

const initChart = ()=>{
  // 使用刚指定的配置项和数据显示图表。
  if(isDark.value) {
    myChart = echarts.init(chartContainer.value, 'dark');
    let option = {
      ...option,
      backgroundColor: '#1a1a1a'
    }
  }
  else {
    myChart = echarts.init(chartContainer.value, 'light');
  }

  myChart.setOption(option);
}

const handleUpdateValue = (value) => {
  if(value === 'tab2'){
    setTimeout(() => {
      myChart.resize()
    }, 200)
  }
}

const currentTab = ref('tab1')
</script>

<template>
  <el-scrollbar>

  <BlankPage>

    <template #default>
      <el-tabs
          v-model="currentTab"
          @tab-change="handleUpdateValue"
          animated style="height: 100%">
        <el-tab-pane name="tab1" label="前往学习" display-directive="show:lazy">
          <div id="info-div">
            <el-scrollbar style="margin-top:18px; border: 1px solid #8080ff88; border-radius: 8px; box-shadow: 0 0 3px #8080ff">
              <el-divider content-position="left">
                <el-text style="font-size: 22px">
                  推荐题目
                </el-text>
              </el-divider>
              <div id="info-container">
                <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
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
              <div id="course-container">
                <MyCourseCard
                    style="margin-bottom: 24px"
                    v-for="brief in course_brief"
                    :brief="brief"/>
              </div>
            </el-scrollbar>
          </div>
        </el-tab-pane>
        <el-tab-pane  name="tab2" label="学习进度" display-directive="show:lazy">
          <div id="course-div">
              <el-divider content-position="left">
                <el-text style="font-size: 22px">
                  学习进度
                </el-text>
              </el-divider>
              <div id="course-container">
                <div class="Space-Between-Flex">
                  <div style="width: 70%">
                    <div style="display:flex; margin-bottom: 12px; margin-left: 24px; margin-right: 24px"
                         v-for="item in course_progress">
                      <el-text size="large" style="width:160px; white-space: nowrap">
                        {{ item.course }}：
                      </el-text>
                      <n-progress
                          type="line"
                          :indicator-placement="'inside'"
                          :height="24"
                          :status="item.progress > 80 ? 'success' : item.progress>60 ? 'default': item.progress > 40? 'warning':'error'"
                          :percentage="item.progress"
                          processing
                      />
                    </div>
                  </div>
                  <div style="width: 30%; height:100%;" class="Center-Flex">
                    <n-progress
                        type="multiple-circle"
                        processing
                        :stroke-width="6"
                        :circle-gap="0.5"
                        :percentage="[
                        90,
                        70,
                        50,
                        10,
                      ]"
                        :color="[
                        themeVars.successColor,
                        themeVars.infoColor,
                        themeVars.warningColor,
                        themeVars.errorColor
                      ]"
                        :rail-style="[
                        { stroke: themeVars.successColor, opacity: 0.3 },
                        { stroke: themeVars.infoColor, opacity: 0.3 },
                        { stroke: themeVars.warningColor, opacity: 0.3 },
                        { stroke: themeVars.errorColor, opacity: 0.3 }
                      ]"
                    >
                      <el-text type="primary" size="large">学习圆环</el-text>
                    </n-progress>
                  </div>
                </div>
                <AIOpinion
                    style="margin-top: 36px"
                    :prompt="'以下是我的各课学习进度，给我来点一句简短的建议：' + JSON.stringify(course_progress)"/>
              </div>
          </div>
          <div id="course-div" style="margin-bottom: 24px; margin-right: 12px; margin-left: 12px">
              <el-divider content-position="left">
                <el-text style="font-size: 22px">
                  学习活动
                </el-text>
              </el-divider>
              <div id="info-container" style="width: 100%">
                <div ref="chartContainer" style="width: 100%; height: 360px; box-shadow: 0 0 8px #8080ff; border-radius: 8px"></div>
              </div>
              <AIOpinion
                  style="margin-top: 36px; margin-right: 24px"
                  :prompt="'以下是我的各课学习时长，给我来点一句简短的建议：' + JSON.stringify(learning_activity)"/>
          </div>
        </el-tab-pane>
        <el-tab-pane name="tab3" label="做题历史">
          <div style="height: 720px">
            <el-scrollbar>
              <el-divider content-position="left">
                <el-text style="font-size: 22px">
                  做题历史
                </el-text>
              </el-divider>
              <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
            </el-scrollbar>
          </div>
        </el-tab-pane>
        <el-tab-pane  name="tab4" label="AI评估">
          <div class="Center-Flex">
            <el-button type="primary" :icon="StarFilled">让小慧重新生成一份~</el-button>
          </div>
          <AITextLong
              style="margin-top: 36px; margin-left: 8px; margin-right: 8px;"
              :prompt="'以下是我的各课学习时长，给我来点一句简短的建议：' + JSON.stringify(course_progress)
                + JSON.stringify(learning_activity) + '请你根据这些数据，总结评估我的学习情况，并为我提出个性化学习方案，回复的时候请使用Markdown格式进行排版. 并进行标题分级，内容尽量详细充实。'"/>
          <div class="Center-Flex" style="flex-direction: column; margin-top: 24px">
            <el-text>你对小慧为你定制的学习计划感到满意吗？</el-text>
            <n-rate allow-half />
          </div>
        </el-tab-pane>
      </el-tabs>
    </template>
  </BlankPage>
  </el-scrollbar>
</template>

<style scoped>

#info-container{
  display: inline-flex;
  padding: 16px
}

#course-container{
  padding: 16px
}

#academy-info-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  flex-direction: column;
  padding: 32px;
  background: var(--el-bg-color);
  margin: 32px 256px 0;
}

#info-div{
  padding-right: 24px;
  width: 100%;
  height: 100%;
}
#course-div{
  width: 100%;
}
</style>