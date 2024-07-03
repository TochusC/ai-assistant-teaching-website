<script setup>
import AITextLong from "@/components/utils/AITextLong.vue";
import {useThemeVars} from "naive-ui";
import {llmApi} from "@/assets/static/js/severConfig.js";
import {Help, HelpFilled, StarFilled} from "@element-plus/icons-vue";
import {onMounted, ref} from "vue";
import axios from "axios";
import {ElMessage} from "element-plus";

const themeVars = useThemeVars()
const showPrompt = ref(false)
const props = defineProps({
  problem: {
    type: Object,
    required: true
  },
  keyConcepts: {
    type: Array,
    required: true
  },
})
const isLoading = ref(true)
const icons = [Help, Help, HelpFilled]


onMounted(() => {
})
</script>

<template>
  <div style="margin-bottom: 12px">
    <h3>题目解析</h3>
    <el-divider content-position="left">相关知识点</el-divider>
    <div style="padding: 24px">
      <el-popover
          v-for="keyConcept in props.keyConcepts"
          placement="top-start"
          :title="keyConcept.title"
          :width="200"
          trigger="hover"
      >
        <template #reference>
          <el-tag type="primary">{{keyConcept.title}}</el-tag>
        </template>
        <template #default>
          {{ keyConcept.description }}
          <p style="margin-top: 6px">难度</p>
          <el-rate
              v-model="keyConcept.difficulty"
              disabled
              :icons="icons"
              show-score
              :colors="['#ef5350', '#ef5350', '#ef5350']"
              text-color="#ef5350"
              score-template="{value} 级"
          />
          <p>重要度</p>
          <el-rate
              v-model="keyConcept.importance"
              disabled
              show-score
              text-color="#ff9900"
              score-template="{value} 星"
          />
        </template>
      </el-popover>
    </div>
    <el-divider content-position="left">维度分析</el-divider>
    <div class="Space-Between-Flex" style="padding: 12px">
      <div style="width: 100%; padding-right: 32px">
        <n-progress type="line" :percentage="props.problem.difficulty" style="margin-bottom: 12px"
                    height="18" status="error">难度</n-progress>
        <n-progress type="line" :percentage="props.problem.importance" style="margin-bottom: 12px"
                    height="18" status="warning">重要度</n-progress>
        <n-progress type="line" :percentage="props.problem.innovation" style="margin-bottom: 12px"
                    height="18" status="info">创新度</n-progress>
        <n-progress type="line" :percentage="props.problem.holistic" style="margin-bottom: 12px"
                    height="18" status="success">综合度</n-progress>
      </div>
      <el-divider direction="vertical"/>
      <div>
        <n-progress
            type="multiple-circle"
            :stroke-width="6"
            :circle-gap="0.5"
            :percentage="[
                        props.problem.holistic,
                        props.problem.innovation,
                        props.problem.importance,
                        props.problem.difficulty,
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
          <div style="text-align: center">
            题目维度环
          </div>
        </n-progress>
      </div>
    </div>
    <el-divider content-position="left">智能解析</el-divider>
    <div class="Center-Flex">
      <el-button
          @click="showPrompt = !showPrompt"
          :icon="StarFilled"
          type="primary"
          style="margin-top: 8px;"
          v-if="!showPrompt">点击让小慧给点建议吧？</el-button>
      <AITextLong v-else style="margin-top: 24px; width: 100%; margin-left: 24px; margin-right: 24px"
                  :prompt="'请用简要的一句话帮我分析一下题目' + problem.description"/>
    </div>
  </div>
</template>

<style scoped>

</style>