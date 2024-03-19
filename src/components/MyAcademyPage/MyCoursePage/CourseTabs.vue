<script setup lang="ts">

const props = defineProps({
  course: {
    type: Object,
    required: true
  }
})

</script>

<template>
  <el-tabs style="width: 100%">
    <el-tab-pane label="学习资源">
      <el-empty description="空空如也"/>
    </el-tab-pane>
    <el-tab-pane label="学习任务">
      <el-empty description="空空如也"/>
    </el-tab-pane>
    <el-tab-pane label="问答讨论">
      <el-empty description="空空如也"/>
    </el-tab-pane>
    <el-tab-pane label="作业考试">
      <el-empty description="空空如也"/>
    </el-tab-pane>
  </el-tabs>
</template>

<style scoped>

</style>