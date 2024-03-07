<script setup lang="ts">
import { ref } from 'vue'
import UnityComponent from "@/components/UnityComponent.vue";
const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<template>
  <div style="display: flex">
<!--    用来放置教学网站的容器-->
    <div id="WebsiteContainer">
      <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          :ellipsis="false"
          @select="handleSelect"
      >
        <el-menu-item index="0">
        </el-menu-item>
        <div class="flex-grow" />
        <el-menu-item index="1">AI赋能的智能教学辅助系统</el-menu-item>
        <el-sub-menu index="2">
          <template #title>Workspace</template>
          <el-menu-item index="2-1">item one</el-menu-item>
          <el-menu-item index="2-2">item two</el-menu-item>
          <el-menu-item index="2-3">item three</el-menu-item>
          <el-sub-menu index="2-4">
            <template #title>item four</template>
            <el-menu-item index="2-4-1">item one</el-menu-item>
            <el-menu-item index="2-4-2">item two</el-menu-item>
            <el-menu-item index="2-4-3">item three</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
      </el-menu>

    </div>
<!--    用来存放AI教学助理的容器-->
    <div id="AssistantContainer">
      <UnityComponent/>
    </div>
  </div>
</template>

<style scoped>
#WebsiteContainer {
  flex: 3;
  border: 1px solid #ccc;
  padding: 10px
}
#AssistantContainer {
  flex:1;
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
