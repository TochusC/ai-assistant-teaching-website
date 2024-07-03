<script setup>
import {useAuth} from "@/assets/static/js/useAuth.js";
import {onMounted, ref} from "vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";
import {Bell, Search} from "@element-plus/icons-vue";
import router from "@/router/index.js";

const { user } = useAuth()
const students = ref([])
const fetchStudents = async () => {
  const studentUrl = backendUrl + 'teacher/student/' + user.value.ident
  axios.get(studentUrl)
      .then((response) => {
        students.value = response.data
        console.log(students.value)
      })
      .catch((error) => {
        console.log(error)
      })
}

onMounted(() => {
  fetchStudents()
})
</script>

<template>
  <div class="glowing-container">
    <el-table :data="students" style="width: 100%">
      <el-table-column prop="school" sortable label="学校"/>
      <el-table-column prop="sid" sortable label="学号" />
      <el-table-column prop="name" sortable label="姓名"/>
      <el-table-column prop="enrollment" sortable label="注册时间"/>
      <el-table-column prop="mental" sortable label="心理情况">
        <template #default="{row}">
          <el-tag v-if="row.mental === '一般常态心理'" type="success">一般常态心理</el-tag>
          <el-tag v-else-if="row.mental === '轻度失调心理'" type="warning">轻度失调心理</el-tag>
          <el-tag v-else-if="row.mental === '严重病态心理'" type="danger">严重病态心理</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="score" sortable label="心理量化分"/>
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button
              :icon="Search"
              @click="router.push('/teaching/student/info/' + scope.row.id)"
              type="primary" size="small">
            查看
          </el-button>
          <el-button
              :icon="Bell"
              type="warning" size="small">
            通知
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

</template>

<style scoped>

</style>