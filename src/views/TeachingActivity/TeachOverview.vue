<script setup>
import CourseCard from "@/components/MainPage/CourseCard.vue";

import {useRouter} from "vue-router";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {Collection, Document, MessageBox, StarFilled, User} from "@element-plus/icons-vue";

const {user} = useAuth()
const router = useRouter()
</script>

<template>
  <div id="content-container">
    <div class="glowing-container" style="margin-bottom: 24px">
      <el-divider content-position="left">尊敬的{{user.name}}老师</el-divider>
      <div style="margin-left: 42px; margin-right: 42px">
        <div style="margin-bottom: 8px"><el-text>您在<el-text size="large" style="color: var(--el-color-primary)">通慧智教</el-text>中:</el-text></div>
        <el-text style="margin-left: 16px">
          开展了<el-text tag="b">{{0}}</el-text>门课程
          <el-icon size="large"><Collection/></el-icon>，

          上传了{{0}}项课程资源
          <el-icon size="large"><MessageBox /></el-icon>，

          布置了{{0}}条课程任务
          <el-icon size="large"><Document /></el-icon>，

          教育了共计<el-text tag="b">{{0}}</el-text>名学生
          <el-icon size="large"><User /></el-icon>，

          总计获得<el-text tag="b">{{0}}</el-text>个星星
          <el-icon size="large" color="var(--color-featured)"><StarFilled /></el-icon>。
          <div style="margin-top: 8px"><el-text>十分感谢您一直以来的辛勤奉献。 </el-text></div>
        </el-text>
      </div>
      <el-divider content-position="right">"桃李不言，下自成蹊。"</el-divider>
    </div>

    <AIOpinion :prompt="'你好小慧，给大家说一句激起未来希望的话！'"/>

    <div id="primary-container">
      <el-divider content-position="left">
        <h1>您所教授的课程：</h1>
      </el-divider>

      <div class="course-container" v-loading="isLoadingCourse">
        <el-scrollbar>
          <el-result
              v-if="course_brief === null"
              icon="error"
              title="获取课程失败"
              sub-title="请稍后再试一试吧？"
          >
            <template #extra>
              <el-button type="primary" @click="fetchCourseBrief">重试</el-button>
            </template>
          </el-result>
        </el-scrollbar>
      </div>
    </div>
  </div>
</template>

<style scoped>
#parent-container{
  height: 100%;
  width: 100%;
}
#body-container{
  margin-top: 4px;
  height: 100%;
}

.el-carousel__item h1 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  text-align: center;
}

#primary-container{
  margin-top: 24px;
  background: var(--el-bg-color);
  padding: 16px;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
}

.course-container {
  padding-left: 32px;
  padding-right: 32px;
  margin-top: 32px;
  margin-bottom: 32px;
}

#content-container {
  padding-left: 36px;
  padding-right: 36px;
  padding-top: 12px;
  width: 100%;
  height: 100%;
}

</style>