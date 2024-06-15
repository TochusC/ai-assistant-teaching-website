<script setup lang="ts">

import router from "@/router";
</script>

<template>
  <div class="Center-Flex" style="height: 64%; width: 100%">
    <el-card style="width: 64%; top: 12%">
      <el-result
          icon="error"
          title="404 Not Found!"
          sub-title="您查找的页面并不存在😣！"
      >
        <template #extra>
          <el-button type="primary" @click="router.push('/portal')">前往首页！</el-button>
        </template>
      </el-result>
    </el-card>
  </div>
</template>

<style scoped>

</style>