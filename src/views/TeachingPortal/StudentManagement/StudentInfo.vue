<script setup>
import {onMounted, ref} from "vue";
import StudentInformation from "@/components/TeachingActivity/StudentInfo/StudentInformation.vue";
import StudentHomeSchoolAuthentication
  from "@/components/TeachingActivity/StudentInfo/StudentHomeSchoolAuthentication.vue";
import StudentEmotionRecord from "@/components/TeachingActivity/StudentInfo/StudentEmotionRecord.vue";
onMounted(() => {
})

const activeTab = ref('profile')
</script>

<template>
  <el-scrollbar>
    <div class="Center-Flex" >
      <div class="glowing-container" style="width: 100%; max-width: 1024px">
        <el-backtop :right="100" :bottom="100" />
        <div id="course-div">
          <el-scrollbar>
            <el-tabs v-model="activeTab">
              <el-tab-pane label="基本信息" name="profile">
                <StudentInformation/>
              </el-tab-pane>
              <el-tab-pane label="家校认证" name="homeSchool">
                <StudentHomeSchoolAuthentication/>
              </el-tab-pane>
              <el-tab-pane label="情绪记录" name="emotion">
                <StudentEmotionRecord/>
              </el-tab-pane>
            </el-tabs>
          </el-scrollbar>
        </div>
      </div>
    </div>
  </el-scrollbar>
</template>

<style scoped>
#course-div{
  width: 100%;
}
</style>