<script setup>
import {inject, onMounted, ref, watch} from "vue";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import * as echarts from "echarts/core";

const progress = ref([])
const progressValue = ref([])
const fetchProgress = async () => {
  axios.get(backendUrl + 'student/course/progress/' + user.value.ident).then(res => {
    progress.value = res.data
    for (let i = 0; i < progress.value.length; i++) {
      progressValue.value.push(progress.value[i].progress)
    }
    console.log(progress.value)
  }).catch(err => {
    console.log(err)
  })
}

const activity = ref([])
const fetchActivity = async () => {
  axios.get(backendUrl + 'student/activity/' + user.value.ident).then(res => {
    activity.value = res.data
    console.log(activity.value)
    initChart()
  }).catch(err => {
    console.log(err)
  })
}

const isDark = inject('isDark')
const chartContainer = ref(null)
let myChart = null

const initChart = ()=>{
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

  let xData = []
  let yValue = []
  for (let i = 0; i < activity.value.length; i++) {
    xData.push(activity.value[i].date)
    yValue.push(activity.value[i].time)
  }
  // 使用刚指定的配置项和数据显示图表。
  let option = { // 指定图表的配置项和数据
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['总学习时长']
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
      data: xData
    },
    yAxis: {
      type: 'value'

    },
    series: [
      {
        name: '总学习时长',
        type: 'line',
        stack: '总量',
        data: yValue
      }
    ]
  };

  for(let i = 0; i < progress.value.length; i++) {
    let cname = progress.value[i].cname
    let cid = progress.value[i].cid
    option.legend.data.push(cname)

    let data = []
    let yValue = []
    axios.get(backendUrl + 'student/course/activity/'
        + user.value.ident + '/' + cid).then(res => {
      data = res.data
      for (let i = 0; i < data.length; i++) {
        yValue.push(data[i].time)
      }
      option.series.push({
        name: cname,
        type: 'line',
        stack: '总量',
        data: yValue
      })
      myChart.setOption(option);
    }).catch(err => {
      console.log(err)
    })
  }
}

onMounted(async =>{
  fetchProgress()
  fetchActivity()
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
})
</script>

<template>
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
               v-for="item in progress">
            <el-text size="large" style="width:160px; white-space: nowrap">
              {{ item.cname }}：
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
              :percentage="progressValue"
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
    <div id="info-container" class="Center-Flex" style="width: 100%">
      <div ref="chartContainer"
           style="width: 92%; height: 360px; margin-top: 24px;
                     box-shadow: 0 0 8px #8080ff; border-radius: 8px"></div>
    </div>
    <AIOpinion
        style="margin-top: 36px; margin-right: 24px"
        :prompt="'以下是我的各课学习时长，给我来点一句简短的建议：' + JSON.stringify(learning_activity)"/>
  </div>
</template>

<style scoped>

</style>