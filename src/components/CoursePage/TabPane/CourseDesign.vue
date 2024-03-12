<script setup lang="ts">

import {Edit} from "@element-plus/icons-vue";

const props = defineProps({
  design:{
    type: Object,
    required: true
  }
})

</script>

<template>
  <el-scrollbar :max-height="520">
    <div class="info-container">
      <el-divider content-position="left">
        <h1>课程背景</h1>
      </el-divider>
      <div class="info-text-container">
        <el-text>
          {{props.design.background}}
        </el-text>
      </div>
    </div>

    <div class="info-container">
      <el-divider content-position="left">
        <h1>课程目标</h1>
      </el-divider>
      <div class="info-text-container">
        <el-text>
          {{props.design.target}}
        </el-text>
      </div>
    </div>

    <div class="info-container">
      <el-divider content-position="left">
        <h1>课程设计原则</h1>
      </el-divider>
      <div class="info-text-container">
        <el-text>
          {{props.design.principle}}
        </el-text>
      </div>
    </div>
  </el-scrollbar>
</template>

<style scoped>
.info-container{
  margin-bottom: 64px;
}
.info-text-container{
  margin: 32px;
  height: 100%;
}
</style>