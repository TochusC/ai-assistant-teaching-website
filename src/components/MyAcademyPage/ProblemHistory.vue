<script setup>

import NoticeCard from "@/components/MyAcademyPage/GoToLearning/NoticeCard.vue";
import {onMounted, ref} from "vue";
import {useAuth} from "@/assets/static/js/useAuth.js";
import ProblemHistoryCard from "@/components/MyAcademyPage/ProblemHistory/ProblemHistoryCard.vue";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const problemHistory = ref([])
const fetchProblemHistory = async () => {
  const {user} = useAuth()
  axios.get(backendUrl + 'student/problem/history/' + user.value.ident).then(res => {
    problemHistory.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

onMounted(() => {
  fetchProblemHistory()
})
</script>

<template>
  <div style="height: 720px">
    <el-scrollbar>
      <el-divider content-position="left">
        <el-text style="font-size: 22px">
          做题历史
        </el-text>
      </el-divider>
      <div class="glowing-container" style="margin-top: 36px; max-height: 740px" >
        <el-scrollbar>
          <ProblemHistoryCard
              v-for="ph in problemHistory"
              :problemHistory="ph"
              style="margin-bottom: 24px"
          />
        </el-scrollbar>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>

</style>