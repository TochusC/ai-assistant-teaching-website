<script setup>
import ParentTabs from "@/components/ParentPage/ParentTabs.vue";
import HeadNavi from "@/components/utils/HeadNavi.vue";
</script>

<template>
  <el-container>
    <el-header style="padding: 0; margin: 0">
      <HeadNavi/>
    </el-header>
    <el-main>
      <ParentTabs/>
    </el-main>
  </el-container>
</template>

<style scoped>

</style>