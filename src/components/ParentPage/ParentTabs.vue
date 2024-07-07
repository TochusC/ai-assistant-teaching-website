<script setup>
import {inject, onMounted, ref, watch} from "vue";
import ChildInformation from "@/components/ParentPage/ParentTabs/ChildInformation.vue";
import ChildHomeSchoolInformation from "@/components/ParentPage/ParentTabs/ChildHomeSchoolInformation.vue";
import ChildEmotionRecord from "@/components/ParentPage/ParentTabs/ChildEmotionRecord.vue";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import {useThemeVars} from "naive-ui";
import * as echarts from "echarts/core";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import {useAuth} from "@/assets/static/js/useAuth.js";
import {StarFilled} from "@element-plus/icons-vue";
import AITextLong from "@/components/utils/AITextLong.vue";

const activeTab = ref('profile')
const themeVars = useThemeVars()
const isDark = inject('isDark')
const chartContainer = ref(null)
let myChart = null

const {user} = useAuth()
const sid = user.value.ident

const isActivityReady = ref(false)
const isProgressReady = ref(false)

const progress = ref([])
const progressValue = ref([])
const fetchProgress = async () => {
  axios.get(backendUrl + 'student/course/progress/' + user.value.ident).then(res => {
    progress.value = res.data
    for (let i = 0; i < progress.value.length; i++) {
      progressValue.value.push(progress.value[i].progress)
    }
    console.log(progress.value)
    isProgressReady.value = true
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
    isActivityReady.value = true
  }).catch(err => {
    console.log(err)
  })
}

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

const isEmotionReady = ref(false)
const emotion = ref('')
const fetchEmotion = async () => {
  axios.get(backendUrl + 'student/emotion/status/' + user.value.ident).then(res => {
    emotion.value = res.data.message
    isEmotionReady.value = true
  }).catch(err => {
    console.log(err)
  })
}

const handleUpdateValue = (value) => {
  if(value === 'learningProgress'){
    setTimeout(() => {
      myChart.resize()
    }, 200)
  }
}

onMounted( //用户选课信息已经初始化了
    async() => {
      await fetchProgress()
      await fetchActivity()
      await fetchEmotion()

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
</script>

<template>
  <el-scrollbar>
    <div class="Center-Flex" >
      <div class="glowing-container" style="width: 100%; max-width: 1024px">
        <el-backtop :right="100" :bottom="100" />
        <div id="course-div">
          <el-scrollbar>
            <el-tabs
                @tab-change="handleUpdateValue"
                v-model="activeTab">
              <el-tab-pane label="基本信息" name="profile">
                <ChildInformation/>
              </el-tab-pane>

              <el-tab-pane label="家校认证" name="homeSchool">
                <ChildHomeSchoolInformation/>
              </el-tab-pane>

              <el-tab-pane label="学习进度" name="learningProgress" display-directive="show:lazy">
                <div style="width: 100%;">
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
                        v-if="isProgressReady"
                        :prompt="'以下是我孩子的各课学习进度，请给我来点一句简短的建议：' + JSON.stringify(progress)"/>
                  </div>
                </div>
                <div style="width:100%; margin-bottom: 24px; margin-right: 12px; margin-left: 12px">
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
                      v-if="isActivityReady"
                      :prompt="'以下是我孩子的各课学习时长，请给我来一句简短的建议：' + JSON.stringify(activity)"/>
                </div>
              </el-tab-pane>
              <el-tab-pane label="情绪记录" name="emotion">
                <ChildEmotionRecord/>
              </el-tab-pane>
              <el-tab-pane  name="tab4" label="🌟AI评估">
                <div class="Center-Flex">
                  <el-button type="primary" :icon="StarFilled">让小慧重新生成一份~</el-button>
                </div>
                <AITextLong
                    style="margin-top: 36px; margin-left: 8px; margin-right: 8px;"
                    v-if="isActivityReady&&isProgressReady&&isEmotionReady"
                    :prompt="'以下是我孩子的各课学习进度：' + JSON.stringify(progress)
              + '以下是我孩子的每日学习时长' + JSON.stringify(activity)
              + '以下是我孩子的当前情绪活跃度（范围0-100）' + emotion +
              '请你根据这些数据，结合我孩子的情绪活跃度，总结评估我孩子的学习、心理情况，并为我孩子提出个性化学习方案和心理辅导建议，回复的时候请使用Markdown格式进行排版. 并进行标题分级，内容尽量详细充实。'"/>
                <div class="Center-Flex" style="flex-direction: column; margin-top: 24px">
                  <el-text>您对小慧为孩子进行的智能评估感到满意吗？</el-text>
                  <n-rate allow-half />
                </div>
              </el-tab-pane>
            </el-tabs>
          </el-scrollbar>
        </div>
      </div>
    </div>
  </el-scrollbar>
</template>

<style scoped>

#course-container{
  padding: 16px
}
#course-div{
  width: 100%;
}
</style>