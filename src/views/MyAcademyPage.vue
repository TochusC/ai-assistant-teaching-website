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

const themeVars = useThemeVars()
const {user} = useAuth();

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

onMounted( //用户选课信息已经初始化了
  async() => {
    const formData = new URLSearchParams();
    let GetLessonUrl = 'http://127.0.0.1:8000/api/choose/' + user.value.id;
    const response = await axios.get(GetLessonUrl);
    const resource = response.data;
    for (let lesson of resource){
      //console.log(lesson.Lesson_id) //用户选课的id
      let GetClassUrl = 'http://127.0.0.1:8000/api/course/' + lesson.Lesson_id;
      const course = await axios.get(GetClassUrl)
      const CouseData = course.data
      console.log("brief数据",CouseData[0])
      course_brief.value.push(CouseData[0])
    }

    // 指定图表的配置项和数据
    let option = {
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

    let myChart = null;
    // 使用刚指定的配置项和数据显示图表。
    if(isDark.value) {
      myChart = echarts.init(chartContainer.value, 'dark');
      option = {
        ...option,
        backgroundColor: '#1a1a1a'
      }
    }
    else {
      myChart = echarts.init(chartContainer.value, 'light');
    }

    myChart.setOption(option);

    watch(isDark, (newVal) => {
      if(newVal) {
        myChart.dispose()
        myChart = echarts.init(chartContainer.value, 'dark');
        option = {
          ...option,
          backgroundColor: themeVars.backgroundColorBase
        }
        myChart.setOption(option);
      }
      else {
        myChart.dispose()
        myChart = echarts.init(chartContainer.value, 'light');
        option = {
          ...option,
          backgroundColor: themeVars.backgroundColorBase
        }
        myChart.setOption(option);
      }
    })

    window.addEventListener('resize', () => {
      myChart.resize()
    })
}
)
</script>

<template>
  <el-scrollbar>

  <BlankPage>
    <template #default>
      <div id="info-div">
        <el-scrollbar>
          <el-divider content-position="left">
            <el-text style="font-size: 22px">
              重要提醒
            </el-text>
          </el-divider>
          <div id="info-container">
            <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
          </div>
        </el-scrollbar>
      </div>

      <div id="course-div">
        <el-scrollbar>
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
                :prompt="'以下是我的各课学习进度，给我来点一句简短的建议：' + course_progress"/>
          </div>
        </el-scrollbar>
      </div>

      <div id="course-div" style="margin-bottom: 24px">
        <el-scrollbar>
          <el-divider content-position="left">
            <el-text style="font-size: 22px">
              学习活动
            </el-text>
          </el-divider>
          <div id="info-container" style="width: 100%">
            <div ref="chartContainer" style="width: 100%; height: 360px; box-shadow: 0 0 8px #8080ff; border-radius: 8px"></div>
          </div>
        </el-scrollbar>
        <AIOpinion
            style="margin-top: 36px"
            :prompt="'以下是我的各课学习时长，给我来点一句简短的建议：' + learning_activity"/>
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
  width: 100%;
  height: 100%;
}
#course-div{
  width: 100%;
}
</style>