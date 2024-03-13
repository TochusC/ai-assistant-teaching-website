<script setup lang="ts">
import { StarFilled, User, MessageBox } from "@element-plus/icons-vue";
import {ref} from "vue";

const props = defineProps({
  introduction:{
    type: String,
    required: true
  },
  imageUrl:{
    type: String,
    required: true
  },
  statistics:{
    type: Object,
    required: true
  }
})

const showIntroduction = ref(false)
</script>

<template>
  <div class="Space-Between-Flex">
    <img
        src="@/assets/static/img/course/1/course.jpg"
        id="course-image"/>
    <div>
      <div class="Space-Between-Flex" style="margin-bottom: 12px">
        <h2 style="white-space: nowrap">课程介绍</h2>
        <div>
          <el-tag
              id="intelligent-tag"
              effect="plain"
              style="margin-right: 16px"
          >
            AI助学 | 智能课
          </el-tag>
          <el-tag
              id="featured-tag"
              effect="plain"
          >
            AI赋能 | 精选课
          </el-tag>
        </div>
      </div>

      <el-text
          line-clamp="3">
        {{props.introduction}}
      </el-text>
      <el-link
          @click="showIntroduction = true"
          style="float: right; color: #8080FF;">
        查看更多
      </el-link>
      <div class="Space-Between-Flex" style="margin-right: 96px; margin-top:18px">
        <div>
          <el-text style="white-space: nowrap">
            <el-icon
                size="large"
                color="var(--color-featured)">
              <StarFilled/>
            </el-icon>
            评分: {{props.statistics.rate}}
          </el-text>
        </div>

        <div>
          <el-text style="white-space: nowrap">
            <el-icon
                size="large">
              <User />
            </el-icon>
            学习人数: {{props.statistics.student}}
          </el-text>
        </div>

        <div>
          <el-text style="white-space: nowrap">
            <el-icon size="large">
              <MessageBox />
            </el-icon>
            课程资源数: {{props.statistics.resources}}
          </el-text>
        </div>
      </div>
    </div>
  </div>
  <el-dialog v-model="showIntroduction" title="课程介绍">
    <div style="margin-left: 24px; margin-right: 24px;margin-bottom: 18px">
      <el-text style="margin: 32px">
        {{props.introduction}}
      </el-text>
    </div>
  </el-dialog>
</template>

<style scoped>
#course-image{
  width: 290px;
  height: 174px;
  object-fit: cover;
  border: #8080FF 1px solid;
  border-radius: 8px;
  margin-right: 32px;
}

#featured-tag{
  padding: 12px;
  transition: 0.5s;
  border: var(--color-featured) 1px solid;
  color: var(--color-featured)
}

#featured-tag:hover{
  box-shadow: var(--color-featured) 0 0 8px;
}

#intelligent-tag{
  padding: 12px;
  transition: 0.5s;
  border: var(--color-intelligent) 1px solid;
  color: var(--color-intelligent)
}

#intelligent-tag:hover{
  box-shadow: var(--color-intelligent) 0 0 8px;
}
</style>