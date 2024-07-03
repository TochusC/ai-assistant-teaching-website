<script setup>
import {Camera, Star, StarFilled} from "@element-plus/icons-vue";
import {onMounted} from "vue";

const props = defineProps({
  emotionRecord: {
    type: Object,
    required: true
  }
})

const recordType = parseInt(props.emotionRecord.type)
console.log(recordType)
</script>

<template>
  <el-card>
    <template #header>
      <div class="Space-Between-Flex">
        <el-text> 情绪卡片
          <el-tag type="primary" round style="margin-right: 12px;margin-left: 12px">
            <el-text style="color: var(--el-color-primary)"><el-icon><Camera /></el-icon>
              图像</el-text></el-tag>
          <el-tag v-if="recordType === 1" type="primary" round style="margin-right: 12px">单模态数据Unimodal</el-tag>
          <el-tag v-else-if="recordType === 2" type="primary" round style="margin-right: 12px">双模态数据Bimodal</el-tag>
          <el-tag v-else-if="recordType === 3" type="primary" round style="margin-right: 12px">三模态数据Trimodal</el-tag>
          <el-tag type="primary" round>{{ emotionRecord.time }}</el-tag>
        </el-text>
        <el-tag
            v-if="recordType > 1"
            id="featured-tag"
            effect="plain"
        >
          <el-icon><Star/></el-icon>
          <el-text style="color: var(--color-featured)">
            多模态Multimodal
          </el-text>
        </el-tag>
      </div>
    </template>
    <div class="Space-Between-Flex">
      <img :src="emotionRecord.raw_image">
      <img :src="emotionRecord.processed_image">
      <div>
      <el-descriptions
          :column="2"
          style="background: #4ac1f7"
          border>
        <el-descriptions-item :span="2" label="记录时间">{{ emotionRecord.time }}</el-descriptions-item>
        <el-descriptions-item label="性别">{{ emotionRecord.gender }}</el-descriptions-item>
        <el-descriptions-item label="置信度"> {{ emotionRecord.gender_probability.toFixed(2) }}</el-descriptions-item>
        <el-descriptions-item label="情绪">{{ emotionRecord.emotion }}</el-descriptions-item>
        <el-descriptions-item label="置信度"> {{ emotionRecord.emotion_probability.toFixed(2) }}</el-descriptions-item>
        <el-descriptions-item label="左眼"> {{ emotionRecord.left_eye_open.toFixed(2) }}</el-descriptions-item>
        <el-descriptions-item label="右眼"> {{ emotionRecord.right_eye_open.toFixed(2) }}</el-descriptions-item>
      </el-descriptions>
      </div>

    </div>
  </el-card>

</template>

<style scoped>
#featured-tag{
  padding: 12px;
  transition: 0.5s;
  border: var(--color-featured) 1px solid;
  color: var(--color-featured)
}

#featured-tag:hover{
  box-shadow: var(--color-featured) 0 0 8px;
}
</style>