<script setup>
import {onMounted, ref} from "vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";
import {useAuth} from "@/assets/static/js/useAuth.js";


const {user} = useAuth()
const sid = user.value.ident

const student = ref({})
const fetchStudent = () => {
  axios.get(backendUrl + 'student/' + sid).then(res => {
    student.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

const basicInfo = ref({})
const fetchBasicInfo = () => {
  axios.get(backendUrl + 'student/info/basic/' + sid).then(res => {
    basicInfo.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

onMounted(() => {
  fetchStudent();
  fetchBasicInfo();
})

</script>

<template>
  <div class="Space-Between-Flex">
    <div style="
          display:flex;
          align-content: center;
          justify-content: center;
          flex-direction: column; max-width: 300px">
      <div class="Center-Flex"
           style="flex-direction: column;margin-right: 64px;margin-left: 64px ">
        <el-popover
            trigger="hover"
            placement="top"
            width="240px"
            title="感谢陪伴"
        >
          <template #default>
            您的孩子于{{student.enrollment}}加入了通慧智教的大家庭🏠
          </template>
          <template #reference>
            <el-tag type="primary" style="margin-bottom: 24px">
              {{student.enrollment}}
            </el-tag>
          </template>
        </el-popover>
        <el-image
            alt="用户头像"
            ref="avatar"
            style="width: 150px; height: 150px; border-radius: 150px"
            :src = 'basicInfo.avatar'
            id = "custom-image"/>
      </div>
    </div>
    <el-card style="width: 100%;" shadow="hover">

      <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
        <el-text
            style="
                font-weight: bold;
                font-size: 16px"
        >基本信息</el-text>
      </div>
      <el-divider
          style="
              margin-top: 16px; margin-bottom: 16px"
      />
      <el-form label-width="auto">
        <el-form-item label="姓名">
          <el-input disabled placeholder="尚未设置姓名" v-model="student.name"/>
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group disabled v-model="basicInfo.gender" >
            <el-radio value="男">男</el-radio>
            <el-radio value="女">女</el-radio>
            <el-radio value="保密">保密</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="生日">
          <el-date-picker
              disabled
              v-model="basicInfo.birthday"
              type="date"
              placeholder="您的孩子尚未填写生日日期"
              style="width: 100%"
          />
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input
              disabled
              placeholder="尚未绑定邮箱"
              v-model="student.email"
          />
        </el-form-item>
        <el-form-item label="手机号">
          <el-input
              disabled
              placeholder="尚未绑定手机号"
              v-model="basicInfo.phone"
          />
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>

</style>