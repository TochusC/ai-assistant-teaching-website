<script setup>
const props = defineProps({
  background:{
    type: String,
    required: true
  },
  target:{
    type: String,
    required: true
  },
  principle:{
    type: String,
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
          {{props.background}}
        </el-text>
      </div>
    </div>

    <div class="info-container">
      <el-divider content-position="left">
        <h1>课程目标</h1>
      </el-divider>
      <div class="info-text-container">
        <el-text>
          {{props.target}}
        </el-text>
      </div>
    </div>

    <div class="info-container">
      <el-divider content-position="left">
        <h1>课程设计原则</h1>
      </el-divider>
      <div class="info-text-container">
        <el-text>
          {{props.principle}}
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