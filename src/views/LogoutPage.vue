<script setup lang="ts">
// 暂未使用

import BlankPage from "@/views/BlankPage.vue";

</script>

<template>
<BlankPage>
  <template #default>
    <div id = "radius-container">
      <el-button type="danger">
        安全退出
      </el-button>
    </div>
  </template>
</BlankPage>
</template>

<style scoped>
#radius-container{
  border: 2px solid var(--el-color-primary);
  height: 640px;
  width: 320px;
  background: var(--el-alert-border-radius-base);
  padding: 32px;
  border-radius: 4px;
}
</style>