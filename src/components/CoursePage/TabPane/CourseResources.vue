<script setup lang="ts">
import {VideoPlay, DataLine, Document} from "@element-plus/icons-vue";

const props = defineProps({
  resources:{
    type: Array,
    required: true
  }
})

</script>

<template>
  <div class="info-container">
    <el-divider content-position="left">
      <h1>课程资源</h1>
    </el-divider>
    <el-scrollbar :max-height="500">
      <div class="resource-container"
           v-for = "item in props.resources"
      >
        <el-card shadow="hover">
          <div class="Space-Between-Flex">

            <div>
              <el-tag
                  style="margin-right: 8px"
                  type="primary">
                <el-icon v-if="item.type=='视频'"><VideoPlay /></el-icon>
                <el-icon v-if="item.type=='课件'"><DataLine /></el-icon>
                <el-icon v-if="item.type=='文档'"><Document /></el-icon>
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
                {{ item.size }}
              </el-tag>
              <el-tag
                  style="margin-right: 8px"
                  type="info" effect="plain" >
                {{ item.time }}
              </el-tag>
              <el-button type="success" size="small">
                下载
              </el-button>
            </div>
          </div>
        </el-card>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>
.resource-container{
  margin: 24px;
}
</style>