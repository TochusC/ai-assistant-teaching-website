<script setup>
import {Notebook } from "@element-plus/icons-vue";
import {onMounted, ref} from "vue";
import router from "@/router/index.js";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import NegativeProgressBar from "@/components/utils/NegativeProgressBar.vue";
import PositiveProgressBar from "@/components/utils/PositiveProgressBar.vue";

const props = defineProps(
    {
      problem:{
        data:Object,
        required:true,
      }
    }
)

const tagType = ref("primary")
const tagTextClass = ref('primary-text')
const courseName = ref('')

const fetchCourseName = async () => {
  const res = await axios.get(backendUrl + '/course/' + props.problem.cid)
  courseName.value = res.data.name
}

onMounted(()=>{
  fetchCourseName();

  if(props.problem){
    if(props.problem.type === "简答")
    {
      tagType.value = "primary"
      tagTextClass.value = "primary-text"
    }
    else if(props.problem.type === "考勤"){
      tagType.value = "success"
      tagTextClass.value = "success-text"
    }
    else{
      tagType.value = "warning"
      tagTextClass.value = "warning-text"
    }
  }
})

const handleCheckout = () => {
  if(props.problem.type === "简答"){
    router.push('/academy/problem/' + props.problem.id)
  }
}

</script>

<template>
  <el-card
      id = "info-card"
      shadow="never"
  >
  <template #header>
    <div class="Space-Between-Flex">
      <el-tag :type="tagType">
        <el-text ref="tagText" :class="tagTextClass">
          <el-icon><Notebook /></el-icon>
          {{ props.problem.type }}
        </el-text>
      </el-tag>
      <el-button
          type="primary"
          size="small"
          @click="handleCheckout"
      >查看</el-button>
    </div>
  </template>
    <el-text>
      {{ courseName }}
    </el-text>
    <p style="margin-top: 4px; margin-bottom: 8px">
      {{ props.problem.title }}
    </p>
    <n-progress type="line" :percentage="problem.difficulty"
                :height="8" status="error">难度</n-progress>
    <n-progress type="line" :percentage="problem.importance"
                :height="8" status="warning">重要度</n-progress>
    <n-progress type="line" :percentage="problem.innovation"
                :height="8" status="info">创新度</n-progress>
    <n-progress type="line" :percentage="problem.holistic"
                :height="8" status="success">综合度</n-progress>
  </el-card>
</template>

<style scoped>
.primary-text{
  color: var(--el-color-primary);
}
.success-text{
  color: var(--el-color-success);
}
.warning-text{
  color: var(--el-color-warning);
}

#info-card{
  min-width: 256px;
  margin: 12px;
  transition: 0.2s;
  box-shadow: 0 0 1px #1a1a1a;
}

#info-card:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #1a1a1a;
}

* {
  white-space: nowrap;
}
</style>