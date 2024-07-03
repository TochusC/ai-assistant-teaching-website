<script setup>
import BasicInfoCard from "@/components/UseCenterPage/UserInformation/BasicInfoCard.vue";
import StudentAuthentication from "@/components/UseCenterPage/UserInformation/StudentAuthentication.vue";
</script>

<template>
    <div id = "all-container">
      <BasicInfoCard/>
      <el-divider/>
      <StudentAuthentication/>
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