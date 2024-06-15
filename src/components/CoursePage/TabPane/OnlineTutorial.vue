<script setup lang="ts">

const props = defineProps({
  chapters:{
    type: Array,
    required: true
  }
})

</script>

<template>
  <div class="info-container">
    <el-divider content-position="left">
      <h1>在线教程</h1>
    </el-divider>
    <div class="info-text-container">
      <el-scrollbar :max-height="500">
        <el-tree
            :default-expand-all="true"
            style="max-width: 600px"
            :data="props.chapters"
        />
      </el-scrollbar>
    </div>
  </div>
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