<script setup>
import {Notebook, Promotion} from "@element-plus/icons-vue";
import router from "@/router/index.js";

const props = defineProps({
  problemHistory: {
    type: Object,
    required: true
  },
})

</script>

<template>
  <el-card  style="margin-left: 12px; margin-right: 12px">
    <div class="Space-Between-Flex">
      <div class="Space-Between-Flex" style="flex: 1">
        <div class="Center-Flex" style="flex-direction: column; width:100%">
            <el-tag type="primary">
            <el-text ref="tagText" style="color: var(--el-color-primary)">
              <el-icon><Notebook /></el-icon>
              {{ props.problemHistory.type }}
            </el-text>
          </el-tag>
          <p>{{props.problemHistory.title}}</p>
        </div>
        <div class="Center-Flex" style="width:100%; flex-direction: column">
          <n-progress type="line"
                      :percentage="props.problemHistory.difficulty"
                      :height="8" status="error">难度: {{ props.problemHistory.difficulty }}</n-progress>
          <n-progress type="line" :percentage="props.problemHistory.importance"
                      :height="8" status="warning">重要度: {{ props.problemHistory.importance }}</n-progress>
          <n-progress type="line" :percentage="props.problemHistory.innovation"
                      :height="8" status="info">创新度: {{ props.problemHistory.innovation }}</n-progress>
          <n-progress type="line" :percentage="props.problemHistory.holistic"
                      :height="8" status="success">综合度: {{ props.problemHistory.holistic }}</n-progress>
        </div>
      </div>
      <div class="Space-Between-Flex" style="flex: 1">
        <div class="Space-Between-Flex" style="flex: 1"></div>
        <div style="flex: 1; margin-right: 24px">
          <n-progress type="circle"
                      :status="props.problemHistory.score >= 80 ? 'success' :
                 props.problemHistory.score >= 60 ? 'info':
                 props.problemHistory.score >= 40 ? 'default':
                 props.problemHistory.score >= 20 ? 'warning' : 'danger'"
                      :percentage="props.problemHistory.score" >
            <span style="font-size: 24px">{{props.problemHistory.score}}分</span>
          </n-progress>
        </div>
        <div class="Center-Flex" style="flex-direction: column">
          <el-tag type="primary" style="margin-bottom: 12px">
            {{ props.problemHistory.time }}
          </el-tag>
          <el-button type="primary" :icon="Promotion" @click="router.push('/academy/problem/' + props.problemHistory.pid)">
            前往重做
          </el-button>
        </div>
      </div>
    </div>
  </el-card>
</template>

<style scoped>

</style>