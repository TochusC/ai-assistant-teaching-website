<script setup>
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const route = useRoute()
const sid = route.params.id

const instructor = ref({})
const fetchInstructor = () => {
  axios.get(backendUrl + 'student/info/instructor/' + sid).then(res => {
    instructor.value = res.data
  }).catch(err => {
    console.log(err)
  })
}
onMounted(() => {
  fetchInstructor()
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
      >辅导员信息</el-text>
    </div>
    <el-divider
        style="
          margin-top: 16px; margin-bottom: 16px"
    />

    <el-form label-width="auto">
      <el-form-item label="导员姓名" style="width: 100%; margin-right: 24px">
        <el-input
            disabled
            v-model="instructor.name"
            placeholder="学生尚未填写辅导员姓名"
        />
      </el-form-item>
      <el-form-item label="导员手机号码" style="width: 100%">
        <el-input
            disabled
            v-model="instructor.phone"
            placeholder="学生尚未填写导员的电话号码"
        />
      </el-form-item>
      <el-form-item label="导员电子邮箱" style="width: 100%; margin-right: 24px">
        <el-input
            disabled
            v-model="instructor.email"
            placeholder="学生尚未填写辅导员电子邮箱"
        />
      </el-form-item>
    </el-form>
  </el-card>
</template>

<style scoped>

</style>