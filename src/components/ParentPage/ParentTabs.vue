<script setup>
import StudentInformation from "@/components/TeachingActivity/StudentInfo/StudentInformation.vue";
import StudentHomeSchoolAuthentication
  from "@/components/TeachingActivity/StudentInfo/StudentHomeSchoolAuthentication.vue";
import StudentEmotionRecord from "@/components/TeachingActivity/StudentInfo/StudentEmotionRecord.vue";
import {ref} from "vue";
import UserInformation from "@/components/UseCenterPage/UserInformation.vue";
import ChildInformation from "@/components/ParentPage/ParentTabs/ChildInformation.vue";
import ChildHomeSchoolInformation from "@/components/ParentPage/ParentTabs/ChildHomeSchoolInformation.vue";
import ChildEmotionRecord from "@/components/ParentPage/ParentTabs/ChildEmotionRecord.vue";

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
                <ChildInformation/>
              </el-tab-pane>
              <el-tab-pane label="家校认证" name="homeSchool">
                <ChildHomeSchoolInformation/>
              </el-tab-pane>
              <el-tab-pane label="情绪记录" name="emotion">
                <ChildEmotionRecord/>
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