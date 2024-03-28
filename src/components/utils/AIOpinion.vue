<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import {llmApi} from "@/assets/static/js/severConfig.js";
import {ElMessage} from "element-plus";
import {Connection, StarFilled} from "@element-plus/icons-vue";

const prop = defineProps(['prompt'])
const isLoading = ref(true)
const llmReply = ref('')

onMounted(() => {

  const formData = new FormData();
  formData.append('userText', prop.prompt);
  axios.post(llmApi, formData).then((response) => {
    llmReply.value = response.data
    let replyArray = response.data.split('|')
    if(replyArray.length>1){
      for (let i = 0; i < replyArray.length; i++) {
        if(replyArray[i].substring(0, 2) === '回复'){
          llmReply.value = replyArray[i].substring(5)
        }
      }
    }
    else{
      llmReply.value=llmReply.value.replace('回复文本：','')
    }
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
  axios.post(llmApi, formData).then((response) => {
    llmReply.value = response.data
    let replyArray = response.data.split('|')
    if(replyArray.length>1){
      for (let i = 0; i < replyArray.length; i++) {
        if(replyArray[i].substring(0, 2) === '回复'){
          llmReply.value = replyArray[i].substring(5)
        }
      }
    }
    else{
      llmReply.value=llmReply.value.replace('回复文本：','')
    }
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
      <div>
        <el-text type="primary" style="text-shadow: 2px 2px 12px var(--el-color-primary)">
          <el-icon class="is-loading">
            <StarFilled/>
          </el-icon>
          小慧（AI）：</el-text>
        <span>
          <el-text style="text-shadow: 2px 2px 12px var(--el-color-primary)">{{ llmReply}}</el-text>
        </span>
      </div>
      <div>
          <el-button
              @click="regenerate"
              :icon="Connection" type="primary" size="small">
            重新生成
          </el-button>
      </div>
    </div>

  </el-card>

</template>

<style scoped>

</style>