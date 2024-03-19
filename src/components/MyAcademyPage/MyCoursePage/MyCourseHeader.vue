<script setup lang="ts">
import { StarFilled, User, MessageBox } from "@element-plus/icons-vue";
import {ref} from "vue";
import router from "@/router";

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
  <div class="Space-Between-Flex" style="align-items: normal">
    <div style="display: flex">
      <img
          style="width:240px; height: 135px; background-size: cover;"
          src="@/assets/static/img/course/1/course.jpg"
          id="course-image"/>
      <div style="display:flex; flex-direction: column;" >

        <div style="display: flex; justify-content: center">
          <span>
            <h2 style="white-space: nowrap;">{{ props.name }}</h2>
          </span>
          <span style="height: 100%; display: flex; align-items: center; margin-left: 16px">
            <el-link style="font-size: 16px" type="primary" @click="router.push(`/course/`+ props.courseId)">
              课程主页
            </el-link>
          </span>
        </div>

        <el-text style="white-space: nowrap; width: 100%">{{props.illustration}}</el-text>
      </div>
    </div>
    <div style="display: flex; height: 100%">
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