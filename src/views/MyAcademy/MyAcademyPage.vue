<script setup lang="ts">
import HeadNavi from "@/components/utils/HeadNavi.vue";
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";

const notice = [
  {
    id: 1,
    type: "作业",
    tittle: "第一次课堂作业",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 1,
    type: "考勤",
    tittle: "第一次课堂考勤",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
  {
    id: 1,
    type: "课程",
    tittle: "第一章课程",
    course: "计算机网络原理",
    startTime: "2024.03.16 21:23",
    endTime: "2024.04.15 00.00",
    announceTime: "2024.03.16 21:23",
  },
]

const course_brief = [
    {
    id: 327,
    name: "计算机网络原理",
    description: "深入剖析数字世界的联通之道",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course.jpg",
  }
]

</script>

<template>
  <BlankPage>
    <template #default>
      <div id="info-div">
        <el-scrollbar>
          <el-divider content-position="left">
            <el-text style="font-size: 22px">
              重要提醒
            </el-text>
          </el-divider>
          <div id="info-container">
            <NoticeCard  v-for="noticeSingleton in notice" :notice="noticeSingleton"/>
          </div>
        </el-scrollbar>
      </div>

      <div id="course-div">
        <el-scrollbar>
          <el-divider content-position="left">
            <el-text style="font-size: 22px">
              我的课程
            </el-text>
          </el-divider>
          <div id="course-container">
            <MyCourseCard
                v-for="brief in course_brief"
                :brief="brief"/>
          </div>
        </el-scrollbar>
      </div>
    </template>
  </BlankPage>
</template>

<style scoped>

#info-container{
  display: inline-flex;
  padding: 16px
}

#course-container{
  padding: 16px
}

#academy-info-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  flex-direction: column;
  padding: 32px;
  background: var(--el-bg-color);
  margin: 32px 256px 0;
}

#info-div{
  width: 100%;
}
#course-div{
  width: 100%;
}
</style>