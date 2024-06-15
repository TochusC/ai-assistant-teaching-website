<script setup>
import {inject, onMounted, ref} from "vue";
import router from "@/router/index.ts";

const showTag = ref(true)
const props = defineProps({
  name:{
    type: String,
    required: true
  },
  illustration:{
    type: String,
    required: true
  },
  imageUrl:{
    type: String,
    required: true
  },
  courseId:{
    type: Number,
    required: true
  }
})
</script>

<template>
  <div style="display: flex">
    <div>
      <img
          style="width:240px; height: 135px; background-size: cover;"
          :src="imageUrl"
          id="course-image"/>
    </div>
    <div style="width: 100%">
      <div style="width: 100%" class="Space-Between-Flex">
        <div>
          <div style="display: flex; white-space: nowrap">
            <h2 style="white-space: nowrap;">{{ props.name }}</h2>
            <el-link style="font-size: 16px; margin-left: 16px" type="primary" @click="router.push(`/course/`+ props.courseId)">
              课程主页
            </el-link>
          </div>
          <el-text style="white-space: nowrap; width: 100%">{{props.illustration}}</el-text>
        </div>
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
      <div style="display:flex;">
        <el-text style="white-space: nowrap">
          课程进度：
        </el-text>
        <el-progress
            style="margin: 24px;
              width: 100%"
            :text-inside="true"
            :stroke-width="26"
            :percentage="70" />
      </div>
    </div>
  </div>

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