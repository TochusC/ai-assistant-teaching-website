<script setup>
import {schools} from "@/assets/static/js/resources";
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const route = useRoute()
const sid = route.params.id

const student = ref({})
const fetchStudent = () => {
  axios.get(backendUrl + 'student/' + sid).then(res => {
    student.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

const studentInfo = ref({})
const fetchStudentInfo = () => {
  axios.get(backendUrl + 'student/info/basic/' + sid).then(res => {
    studentInfo.value = res.data
    schoolIndex.value = findSchoolIndex(studentInfo.value.school)
    departmentIndex.value = findDepartmentIndex(studentInfo.value.department)
    majorIndex.value = findMajorIndex(studentInfo.value.major)
  }).catch(err => {
    console.log(err)
  })
}

const schoolIndex = ref(0)
const departmentIndex = ref(-1)
const majorIndex = ref(-1)
const findSchoolIndex = (school) => {
  for (let i = 0; i < schools.length; i++) {
    if (schools[i].label === school) {
      return i
    }
  }
  return -1
}
const findDepartmentIndex = (department) => {
  for (let i = 0; i < schools[schoolIndex.value].departments.length; i++) {
    if (schools[schoolIndex.value].departments[i].label === department) {
      return i
    }
  }
  return -1
}
const findMajorIndex = (major) => {
  for (let i = 0; i < schools[schoolIndex.value].departments[departmentIndex.value].majors.length; i++) {
    if (schools[schoolIndex.value].departments[departmentIndex.value].majors[i].label === major) {
      return i
    }
  }
  return -1
}

onMounted(() => {
  fetchStudent()
  fetchStudentInfo()
})
</script>

<template>
  <el-card shadow="hover">
    <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
      <el-text
          style="
                font-weight: bold;
                font-size: 16px"
      >学生认证</el-text>
    </div>
    <el-divider
        style="
              margin-top: 16px; margin-bottom: 16px"
    />
    <el-form label-width="auto">
      <el-form-item label="学校">
        <el-input disabled placeholder="尚未绑定学校" v-model="student.school"/>
      </el-form-item>
      <el-form-item label="学号">
        <el-input disabled placeholder="尚未绑定学号" v-model="student.id"/>
      </el-form-item>
      <div class="Space-Between-Flex" style="width: 100%">
        <el-form-item style="flex: 1" label="入学时间">
          <el-date-picker
              disabled
              v-model="studentInfo.entry"
              type="date"
              placeholder="该同学尚未选择入学年份"
              style="width: 100%"
          />
        </el-form-item>
        <el-form-item label="学制" style="flex: 1">
          <el-select
              disabled
              v-model="studentInfo.duration"
              placeholder="该同学尚未选择学制"
              style="width: 240px"
          >
            <el-option
                key="叁"
                label="叁"
                value="叁"
            />
            <el-option
                key="肆"
                label="肆"
                value="肆"
            />
            <el-option
                key="伍"
                label="伍"
                value="伍"
            />
          </el-select>
        </el-form-item>
      </div>
      <el-form-item label="教学院部">
        <el-select
            disabled
            v-model="studentInfo.department"
            placeholder="该同学尚未选择教学院部"
            @change="departmentIndex = findDepartmentIndex($event)"
        >
          <el-option
              v-if = "schoolIndex !== -1"
              v-for="item in schools[schoolIndex].departments"
              :key="item.label"
              :label="item.label"
              :value="item.label"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="所属专业">
        <el-select
            disabled
            v-model="studentInfo.major"
            placeholder="该同学尚未选择所属专业"
            @change="majorIndex = findMajorIndex($event)"
        >
          <el-option
              v-if="departmentIndex !== -1"
              v-for="item in schools[schoolIndex].departments[departmentIndex].majors"
              :label="item.label"
              :value="item.label"
              :key="item.label"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="所属教学班">
        <el-select
            disabled
            v-model="studentInfo.class"
            placeholder="该同学尚未选择教学班"
        >
          <el-option
              v-if="majorIndex !== -1"
              v-for="item in schools[schoolIndex].departments[departmentIndex].majors[majorIndex].classes"
              :label="item.label"
              :value="item.label"
              :key="item.label"
          />
        </el-select>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<style scoped>

</style>