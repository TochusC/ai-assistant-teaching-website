<script setup>
import {schools} from "@/assets/static/js/resources";
import {onMounted, ref} from "vue";
import {Edit, Promotion} from "@element-plus/icons-vue";
import {useAuth} from "@/assets/static/js/useAuth.js";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const {user} = useAuth()

const educationBtnText = ref('编辑信息')
const educationBtnType = ref('primary')
const educationBtnIcon = ref(Edit)

const isEducationEditable = ref(false)
const handleEducationEdit = () => {
  isEducationEditable.value = !isEducationEditable.value
  if(isEducationEditable.value){
    educationBtnText.value = '保存上传'
    educationBtnType.value = 'success'
    educationBtnIcon.value = Promotion
  }
  else{
    educationBtnText.value = '编辑信息'
    educationBtnType.value = 'primary'
    educationBtnIcon.value = Edit
  }
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

const authenticationInfo = ref({})
const fetchAuthenticationInfo = () => {
  axios.get(backendUrl + 'student/info/academy/' + user.value.ident).then(res => {
    authenticationInfo.value = res.data
    schoolIndex.value = findSchoolIndex(user.value.school)
    departmentIndex.value = findDepartmentIndex(authenticationInfo.value.department)
    majorIndex.value = findMajorIndex(authenticationInfo.value.major)
  }).catch(err => {
    console.log(err)
  })
}

onMounted(() => {
  fetchAuthenticationInfo();
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
      >学生认证</el-text>
      <el-button
          @click="handleEducationEdit"
          :type="educationBtnType"
          :icon="educationBtnIcon"
          size="small">
        {{ educationBtnText }}
      </el-button>
    </div>
    <el-divider
        style="
              margin-top: 16px; margin-bottom: 16px"
    />
    <el-form label-width="auto">
      <el-popover
          title="不可更改❌"
          trigger="hover"
          width="320px"
          placement="top"
          content="学校一经注册，就不可再变了哦😣"
      >
        <template #reference>
          <el-form-item label="学校">
            <el-input disabled placeholder="尚未绑定学校" v-model="user.school"/>
          </el-form-item>
        </template>
      </el-popover>
      <el-popover
          title="不可更改❌"
          trigger="hover"
          width="320px"
          placement="top"
          content="学号一经注册，就不可再变了哦😣"
      >
        <template #reference>
          <el-form-item label="学号">
            <el-input disabled placeholder="尚未绑定学号" v-model="user.id"/>
          </el-form-item>
        </template>
      </el-popover>
      <div class="Space-Between-Flex" style="width: 100%">
        <el-form-item style="flex: 1" label="入学时间">
          <el-date-picker
              :disabled="!isEducationEditable"
              v-model="authenticationInfo.enrollment"
              type="date"
              placeholder="请选择入学年份，同学😊"
              style="width: 100%"
          />
        </el-form-item>
        <el-form-item label="学制" style="flex: 1">
          <el-select
              :disabled="!isEducationEditable"
              v-model="authenticationInfo.period"
              placeholder="还有学制奥"
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
            :disabled="!isEducationEditable"
            v-model="authenticationInfo.department"
            placeholder="嘿，这里是你的教学院部"
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
            :disabled="!isEducationEditable"
            v-model="authenticationInfo.major"
            placeholder="别忘了确认你的所属专业"
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
            :disabled="!isEducationEditable"
            v-model="authenticationInfo.s_class"
            placeholder="最后是你的所在的教学班"
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