<script setup lang="ts">
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import { onMounted , ref } from "vue";
import axios from "axios";

const {user} = useAuth();

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
//根据学生的id找到学生的选课，然后根据学生的选课的信息取请求后端，后端对每一个id请求应该返回的是这个json对象
// const course_brief = [ 
//     {
//     id: 327,
//     name: "计算机网络原理",
//     lable:"判断课程的类型（AI赋能精选课等等）",
//     description: "深入剖析数字世界的联通之道",
//     illustration: "国家级 | 工学 (08)/计算机类 (0809)",
//     image: "@/assets/static/img/course/1/course.jpg",
//   }
// ]

const course_brief = ref([])

onMounted( //用户选课信息已经初始化了
  async() => {
    const formData = new URLSearchParams();
    let GetLessonUrl = 'http://127.0.0.1:8000/api/choose/' + user.value.id;
    const response = await axios.get(GetLessonUrl);
    const resource = response.data;
    for (let lesson of resource){
      //console.log(lesson.Lesson_id) //用户选课的id
      let GetClassUrl = 'http://127.0.0.1:8000/api/course/' + lesson.Lesson_id;
      const course = await axios.get(GetClassUrl)
      const CouseData = course.data
      console.log("brief数据",CouseData[0])
      course_brief.value.push(CouseData[0])
    }
}
)
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
  height: 100%;
}
#course-div{
  width: 100%;
}
</style>