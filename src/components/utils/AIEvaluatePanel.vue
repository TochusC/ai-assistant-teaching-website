<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import {basicLLMApi} from "@/assets/static/js/severConfig.js";
import {ElMessage} from "element-plus";
import {Close, Connection, StarFilled} from "@element-plus/icons-vue";

const prop = defineProps(['prompt'])
const isLoading = ref(true)
const llmReply = ref('')
const emit = defineEmits(['closeText'])
const contentContainer = ref(null)
const score = ref(0)


onMounted(() => {
  const formData = new FormData();
  formData.append('userText', prop.prompt);
  axios.post(basicLLMApi, formData).then((response) => {
    llmReply.value = response.data

    let match = llmReply.value.match(/<(\d+)>/);

    if (match) {
      // 如果匹配成功，提取得分并打印
      score.value = match[1];
    } else {
      score.value = 0;
    }

    contentContainer.value.innerHTML = marked.parse(llmReply.value);
    isLoading.value=false;
  }).catch((error) => {
    ElMessage(
        {
          message: '小慧好像暂时不在线哦。',
          type: 'warning'
        }
    )
    llmReply.value = '小慧好像暂时不在线，请稍后再试试吧'
    isLoading.value=false;
  })
})

const regenerate = ()=>{
  isLoading.value=true;
  const formData = new FormData();
  formData.append('userText', prop.prompt);
  axios.post(basicLLMApi, formData).then((response) => {
    llmReply.value = response.data

    let match = llmReply.value.match(/<(\d+)>/);

    if (match) {
      // 如果匹配成功，提取得分并打印
      score.value = match[1];
    } else {
      score.value = 0;
    }

    contentContainer.value.innerHTML = marked.parse(llmReply.value);
    isLoading.value=false;
  }).catch((error) => {
    ElMessage(
        {
          message: '小慧好像暂时不在线哦。',
          type: 'warning'
        }
    )
    llmReply.value = '小慧好像暂时不在线，请稍后再试试吧'
    isLoading.value=false;
  })

}
</script>

<template>
  <el-card shadow="hover" v-loading="isLoading"
           style="
           border: 0 0 8px var(--el-color-primary);
           border-radius: 5px;
           box-shadow: 0 0 12px var(--el-color-primary)">
    <div class="Space-Between-Flex">
      <div style="margin-right: 24px">
        <el-text type="primary" style="text-shadow: 2px 2px 12px var(--el-color-primary)">
          <el-icon class="is-loading">
            <StarFilled/>
          </el-icon>
          小慧（AI）：</el-text>
        <span ref="contentContainer">
        </span>
      </div>
      <div style="display: flex; flex-direction: column">
        <el-button
            style="margin-left: 12px; width: 96px; margin-bottom: 12px"
            @click="regenerate"
            :icon="Connection" type="primary" size="small">
          重新生成
        </el-button>
        <el-button
            style="width: 96px"
            @click="emit('closeText')"
            :icon="Close" type="danger" size="small">
          关闭提示
        </el-button>
      </div>
    </div>
    <el-divider/>
    <div class="Center-Flex">
      <n-progress
          type="dashboard"
          :status="score > 80 ? 'success' : score>60 ? 'default': score > 40? 'warning':'error'"
          gap-position="bottom"
          :percentage="score"  >
        <el-text size="large">
          {{ score }}分
        </el-text>
      </n-progress>
    </div>
  </el-card>
</template>

<style scoped>

</style>