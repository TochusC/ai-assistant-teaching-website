<script setup>
import {ref, provide, inject, onMounted} from "vue";
import {Collection, Star, User} from "@element-plus/icons-vue";
import router from "@/router/index.js";

const activeTab = ref('navigation')

const workObject = inject('workObject')

</script>

<template>
    <el-card style="height: 100%">
      <el-tabs v-model="activeTab">
        <el-tab-pane label="导航" name="navigation">
          <el-menu
              :default-openeds="['2', '3']"
              default-active="1">
            <el-menu-item
                index="1"
                @click="router.push('/teaching/portal')"
            >
              <el-icon><Star/></el-icon>
              <template #title>教学总览</template>
            </el-menu-item>
            <el-sub-menu
                index="2"
            >
              <template #title>
                <el-icon><Collection/></el-icon>
                <span>课程管理</span>
              </template>
              <el-menu-item index="2-1"
                            @click="router.push('/teaching/course/create')"
              >新建课程</el-menu-item>
            </el-sub-menu>
            <el-sub-menu
                index="3"
            >
              <template #title>
                <el-icon><User/></el-icon>
                <span>学生管理</span>
              </template>
              <el-menu-item index="3-1"
                            @click="router.push('/teaching/student/overview')"
              >学生总览</el-menu-item>
            </el-sub-menu>
          </el-menu>
        </el-tab-pane>
        <el-tab-pane label="工作区" name="workspace">
          <el-tree
            :data="workObject"
            node-key="id"
            default-expand-all
          >
          </el-tree>

        </el-tab-pane>
      </el-tabs>
    </el-card>
</template>

<style scoped>

</style>