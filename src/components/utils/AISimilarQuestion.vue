<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import {llmApi} from "@/assets/static/js/severConfig.js";
import {ElMessage} from "element-plus";
import {Close, Connection, Delete, Position, Promotion, StarFilled} from "@element-plus/icons-vue";

import SimilarProblemDialog from "@/components/MyAcademyPage/ProblemPage/SimilarProblemDialog.vue";
const prop = defineProps(['prompt'])
const isLoading = ref(true)
const llmReply = ref('')
const emit = defineEmits(['closeText', 'generateComplete'])
const contentContainer = ref(null)
const score = ref(0)
const questionDiaVis = ref(false)


onMounted(() => {
  regenerate()
})
const question = ref("");
const ansBtnAvailable = ref(true)

const regenerate = () => {
  isLoading.value = true;
  const formData = new FormData();
  formData.append('userText', prop.prompt);
  const questionGenerateApi = llmApi + 'question/generate/'

  axios.post(questionGenerateApi, formData).then((response) => {
    llmReply.value = response.data
    let match = llmReply.value.match(/<(\d+%)>/);
    if (match) {
      // 如果匹配成功，提取得分并打印
      score.value = match[1].slice(0, -1);
    } else {
      score.value = 0;
    }
    question.value = llmReply.value.slice(5);
    contentContainer.value.innerHTML = marked.parse(llmReply.value.slice(5));
    isLoading.value = false;
    emit('generateComplete', llmReply)
  }).catch((error) => {
    ElMessage(
        {
          message: '小慧好像暂时不在线哦。',
          type: 'warning'
        }
    )
    llmReply.value = '小慧好像暂时不在线，请稍后再试试吧'
    ansBtnAvailable.value = false
    contentContainer.value.innerHTML = marked.parse(llmReply.value);
    emit('generateComplete', llmReply)
    isLoading.value = false;
  })
}
</script>

<template>
  <el-card shadow="hover" v-loading="isLoading"
           style="
           margin-left: 8px;
            margin-right: 8px;
            margin-bottom: 24px;
           border: 8px var(--el-color-primary);
           border-radius: 5px;
           box-shadow: 0 0 12px var(--el-color-primary)">
    <div class="Space-Between-Flex">
      <div style="margin-right: 24px">
        <el-text type="primary" style="text-shadow: 2px 2px 12px var(--el-color-primary)">
          <el-icon class="is-loading">
            <StarFilled/>
          </el-icon>
          小慧（AI）：
        </el-text>
        <span ref="contentContainer">
        </span>
      </div>
      <div class="Space-Between-Flex">
        <n-progress
            type="dashboard"
            :status="score > 80 ? 'success' : score>60 ? 'default': score > 40? 'warning':'error'"
            gap-position="bottom"
            :percentage="score">
          <n-text style="white-space: nowrap">
            相似度{{ score }}%
          </n-text>
        </n-progress>
          <div style="display: flex; flex-direction: column; margin-left: 24px">
            <el-button
              :icon="Position"
              type="success"
              size="small"
              @click="questionDiaVis = true"
              :disabled="!ansBtnAvailable"
              style="margin-bottom: 24px; padding: 0"
              >
              前往作答
            </el-button>
            <el-button
                @click="regenerate"
                style="margin: 0"
                size="small"
                :icon="Connection"
                type="primary"
            >
              重新生成
            </el-button>
          </div>
          <SimilarProblemDialog
              v-model="questionDiaVis"
              :question="question"
              @closeDial="questionDiaVis = false"
          />
      </div>
    </div>
  </el-card>
</template>

<style scoped>

</style>