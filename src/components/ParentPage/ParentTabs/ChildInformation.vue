<script setup>
import ChildBasicInfoCard from "@/components/ParentPage/ParentTabs/ChildInformation/ChildBasicInfoCard.vue";
import ChildSchoolAuthentication
  from "@/components/ParentPage/ParentTabs/ChildInformation/ChildSchoolAuthentication.vue";
</script>

<template>
    <div id = "all-container">
      <ChildBasicInfoCard/>
      <el-divider/>
      <ChildSchoolAuthentication/>
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