<script setup>
import {onMounted, ref} from "vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import {useAuth} from "@/assets/static/js/useAuth.js";
import axios from "axios";
import {ElMessage} from "element-plus";
import EmotionCard from "@/components/UseCenterPage/EmotionRecord/EmotionCard.vue";

const emotionRecord = ref({})
const fetchEmotionRecord = () => {
  const {user} = useAuth()
  const emotionUrl = backendUrl + 'student/emotion/' + user.value.id
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
      >您孩子的任何一丝小情绪都被我们时刻关注着✨~</el-text>
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