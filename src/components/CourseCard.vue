<script setup lang="ts">

const props = defineProps({
  "courseName": {
    type: String,
    required: true
  },
  "courseDescription": {
    type: String,
    required: true
  },
  "courseImage": {
    type: String,
    required: true
  }
})

</script>

<template>
  <el-card shadow="hover"
           style="width: 280px;
           height: 250px;
           margin-right: 36px">
    <slot>
    </slot>
    <div style="padding: 14px;">
      <h4>{{props.courseName}}</h4>
      <p>
        {{ props.courseDescription }}</p>
    </div>
  </el-card>
</template>

<style scoped>

</style>