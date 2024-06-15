<script setup>
import {ref} from "vue";
import {Collection, Star} from "@element-plus/icons-vue";

const activeTab = ref('navigation')
</script>

<template>
    <el-card style="height: 100%">
      <el-tabs v-model="activeTab">
        <el-tab-pane label="导航" name="navigation">
          <el-menu :default-openeds="['2']" default-active="1">
            <el-menu-item index="1">
              <el-icon><Star/></el-icon>
              <template #title>教学总览</template>
            </el-menu-item>
            <el-sub-menu index="2">
              <template #title>
                <el-icon><Collection/></el-icon>
                <span>课程管理</span>
              </template>
              <el-menu-item index="2-1">新建课程</el-menu-item>
            </el-sub-menu>
          </el-menu>
        </el-tab-pane>
        <el-tab-pane label="工作区" name="workspace">User</el-tab-pane>
      </el-tabs>
    </el-card>
</template>

<style scoped>

</style>