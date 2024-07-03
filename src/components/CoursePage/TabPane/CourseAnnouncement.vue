<script setup>
import {onMounted} from "vue";
const props = defineProps({
  announcement:{
    type: Array,
    required: true
  }
})


</script>

<template>
  <div class="info-container">
    <el-divider content-position="left">
      <h1>课程公告</h1>
    </el-divider>
    <el-scrollbar :max-height="500">
      <div class="announcement-container"
           v-for = "item in props.announcement"
      >
        <el-card shadow="hover">
          <el-tag
              v-if="item.type === '普通公告'"
              type="primary">
            {{ item.type }}
          </el-tag>
          <el-tag
              v-else-if="item.type === '重要公告'"
              type="warning">
            {{ item.type }}
          </el-tag>
          <el-tag
              v-else-if="item.type === '警示公告'"
              type="danger">
            {{ item.type }}
          </el-tag>

          <el-text style="margin-left: 8px">
            {{ item.title }}
          </el-text>
          <el-tag
              style="float: right"
              type="info" effect="plain" >
            {{ item.time }}
          </el-tag>
        </el-card>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>

.info-container{
  margin-bottom: 64px;
}
.announcement-container{
  margin: 24px;
}
</style>