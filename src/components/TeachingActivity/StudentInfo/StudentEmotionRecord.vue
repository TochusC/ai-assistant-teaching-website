<script setup>
import {onMounted, ref} from "vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";
import {ElMessage} from "element-plus";
import EmotionCard from "@/components/UseCenterPage/EmotionRecord/EmotionCard.vue";
import {useRoute} from "vue-router";

const route = useRoute()
const sid = route.params.id

const emotionRecord = ref({})
const fetchEmotionRecord = () => {
  const emotionUrl = backendUrl + 'student/emotion/' + sid
  axios.get(emotionUrl).then((res) => {
    emotionRecord.value = res.data
  }).catch((err) => {
    ElMessage({
      message: '获取情绪记录失败😣',
      type: 'error'
    })
  })
}
onMounted(() => {
  fetchEmotionRecord()
})
</script>

<template>
  <el-card
      shadow="hover"
  >
    <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
      <el-text
          style="
            font-weight: bold;
            font-size: 16px"
      >该同学的情绪记录如下</el-text>
    </div>
    <el-divider
        style="
          margin-top: 16px; margin-bottom: 16px"
    />
    <div style="height: 960px">
      <el-scrollbar>
        <EmotionCard
            v-for="record in emotionRecord"
            :emotion-record="record"
            style="margin-bottom: 12px"
        />
      </el-scrollbar>
    </div>
  </el-card>
</template>

<style scoped>

</style>