<script setup lang="ts">

import {DataLine, Document, VideoPlay} from "@element-plus/icons-vue";
import {defineProps} from "vue";

const props = defineProps({
  homework:{
    type: Array,
    required: true
  }
})
</script>

<template>
  <div class="info-container">
    <el-divider content-position="left">
      <h1>作业测试</h1>
    </el-divider>
    <el-scrollbar :max-height="500">
      <div class="homework-container"
           v-for = "item in props.homework"
      >
        <el-card shadow="hover">
          <div class="Space-Between-Flex">

            <div>
              <el-tag
                  style="margin-right: 8px"
                  type="primary">
                <el-icon v-if="item.type=='测试'"><DataLine /></el-icon>
                <el-icon v-if="item.type=='作业'"><Document /></el-icon>
                {{ item.type }}
              </el-tag>
              <el-text style="margin-left: 8px">
                {{ item.name }}
              </el-text>
            </div>
            <div>
              <el-tag
                  style="margin-right: 8px"
                  type="info" effect="plain" >
                开始时间：{{ item.start }}
              </el-tag>
              <el-tag
                  style="margin-right: 8px"
                  type="info" effect="plain" >
                截止时间：{{ item.end }}
              </el-tag>
              <el-button type="primary" size="small">
                查看
              </el-button>
            </div>
          </div>
        </el-card>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>
.homework-container{
  margin: 24px;
}
</style>