<script setup>
import StudentBasicInfoCard
  from "@/components/TeachingActivity/StudentInfo/StudentInformation/StudentBasicInfoCard.vue";
import StudentSchoolAuthentication
  from "@/components/TeachingActivity/StudentInfo/StudentInformation/StudentSchoolAuthentication.vue";
</script>

<template>
  <div id = "all-container">
    <StudentBasicInfoCard/>
    <el-divider/>
    <StudentSchoolAuthentication/>
  </div>
</template>

<style scoped>
#all-container{
  display: flex;
  height: 100%;
  flex-direction: column;
  width: 100%;
}
</style>