<script setup lang="ts">
import router from "@/router";
import HeadNavi from "@/components/utils/HeadNavi.vue";
import InfoTabs from "@/components/CoursePage/InfoTabs.vue";
import CourseHeader from "@/components/CoursePage/CourseHeader.vue";
import axios from "axios";
import {inject, onMounted, ref} from "vue";

const route = router.currentRoute.value
const courseId = route.params.id
const Course = ref([])

// const course = {
//   id: 1,
//   name: "计算机网络原理",
//   description: "深入剖析数字世界的联通之道",
//   illustration: "国家级 | 工学 (08)/计算机类 (0809)",
//   introduction: "Internet作为最伟大的技术发明之一，将人类引入到了信息时代。电子邮件、万维网、电子商务、微信、支付宝等的普及应用，使得人与人之间交流更加迅捷、距离大大缩短，世界真正变成了地球村。计算机网络已不再只是一门技术，而是成为一种无处不在的生活方式，更是一种文化。作为一门通识课程，本课程将带领大家走进网络技术的殿堂，内容准确新颖，理论操作结合，开放问题探究，深入浅出地介绍计算机网络基本原理，直接接地气地揭开网络居民常见的技术应用困惑。",
//   image: "@/assets/static/img/course/1/course.jpg",

//   design:{
//     background: "网络技术深刻改变着人类社会的方方面面，已成为信息时代公民的基本素养和生活方式。计算机网络是一门面向社会公众，以生活息息相关的网络技术和网络应用为讲授内容的通识教育课程，实用、通俗、准确、学以致用，是帮助开启网络生活之门的钥匙。",
//     target: "本课程旨在使学生了解计算机网络的基本概念、基本原理、基本技术和基本应用，掌握计算机网络的基本知识和基本技能，具备计算机网络的基本素养，能够熟练地使用计算机网络进行信息检索、资源共享、通信交流、网上学习、网上工作和网上娱乐等活动。",
//     principle: "本课程的教学原则是：以学生为中心，以问题为导向，以实践为基础，以创新为动力，以合作为手段，以评价为支撑。"
//   },

//   catalog:[
//     {
//       label: "第一章 计算机网络概述",
//       children: [
//         {
//           label: "1.1 计算机网络的概念和发展",
//         },
//         {
//           label: "1.2 计算机网络的分类",
//         },
//         {
//           label: "1.3 计算机网络的性能",
//         },
//         {
//           label: "1.4 计算机网络的体系结构",
//         },
//         {
//           label: "1.5 计算机网络的标准化",
//         },
//       ]
//     },
//     {
//       label: "第二章 物理层",
//       children: [
//         {
//           label: "2.1 传输媒体",
//         },
//         {
//           label: "2.2 数据通信基础",
//         },
//         {
//           label: "2.3 数据通信技术",
//         },
//         {
//           label: "2.4 传输调制技术",
//         },
//         {
//           label: "2.5 传输交换技术",
//         },
//       ]
//     },
//     {
//       label: "第三章 数据链路层",
//       children: [
//         {
//           label: "3.1 数据链路层的基本概念",
//         },
//         {
//           label: "3.2 数据链路层的基本功能",
//         },
//         {
//           label: "3.3 数据链路层的基本协议",
//         },
//         {
//           label: "3.4 数据链路层的基本技术",
//         },
//         {
//           label: "3.5 数据链路层的基本设备",
//         },
//       ]
//     },
//     {
//       label: "第四章 网络层",
//       children: [
//         {
//           label: "4.1 网络层的基本概念",
//         },
//         {
//           label: "4.2 网络层的基本功能",
//         },
//         {
//           label: "4.3 网络层的基本协议",
//         },
//         {
//           label: "4.4 网络层的基本技术",
//         },
//       ]
//     }
//   ],

//   announcement: [
//     {
//       type: "警示公告",
//       content: "本课程已将近结课，请尽快完成学习任务。",
//       time: "2022-12-07 13:21"
//     },
//     {
//       type: "重要公告",
//       content: "本课程已正式开课！",
//       time: "2022-09-01 00:00"
//     },
//     {
//       type: "普通公告",
//       content: "本课程将于2022年9月1日开课，敬请期待！",
//       time: "2022-08-01 18:37"
//     }
//   ],

//   qa:[
//     {
//       question: "如何学习本课程？",
//       answer: "本课程采用线上教学模式，学生可以在学堂平台上进行学习。"
//     },
//     {
//       question: "本课程的考核方式是什么？",
//       answer: "本课程的考核方式包括平时作业、期中考试、期末考试。"
//     },
//     {
//       question: "本课程的教学目标是什么？",
//       answer: "本课程旨在使学生了解计算机网络的基本概念、基本原理、基本技术和基本应用，掌握计算机网络的基本知识和基本技能，具备计算机网络的基本素养，能够熟练地使用计算机网络进行信息检索、资源共享、通信交流、网上学习、网上工作和网上娱乐等活动。"
//     }
//   ],

//   resources:[
//     {
//       type: "课件",
//       name: "第一章 计算机网络概述",
//       time: "2022-09-01 00:00",
//       size: "1.2M",
//       url: "http://www.baidu.com",
//     },
//     {
//       type: "视频",
//       name: "第二章 物理层",
//       time: "2022-09-01 00:00",
//       size: "1.2G",
//       url: "http://www.baidu.com",
//     },
//     {
//       type: "文档",
//       name: "第三章 数据链路层",
//       time: "2022-09-01 00:00",
//       size: "1.2M",
//       url: "http://www.baidu.com",
//     },
//   ],

//   homework:[
//     {
//       type: "作业",
//       name: "第一次作业",
//       start: "2022-09-01 00:00",
//       end: "2022-09-07 00:00",
//       id: 1
//     },
//     {
//       type: "测试",
//       name: "第一次测试",
//       start: "2022-09-01 00:00",
//       end: "2022-09-07 00:00",
//       id: 2
//     },
//   ],

//   statistics: {
//     student: 120,
//     rate: 9.8,
//     total_rate : 98,
//     rate_num : 100,
//     qa: 3,
//     resources: 3,
//     homework: 2,
//     announcement: 3,
//     chapter: 4
//   }
// }


const dynamicBannerPadding = ref(128)
const windowWidth = inject("windowWidth")
const updatePadding = () => {
  // 示例：根据窗口宽度动态调整padding值
  dynamicBannerPadding.value = windowWidth.value / 2000 * 164;
  if(windowWidth.value < 1024){
    dynamicBannerPadding.value = 16
  }
};
const rescaleElements = ()=>{
  updatePadding();
}

const tittle = ref(null)

onMounted(
  async() => {
    rescaleElements();
  setTimeout(() => {
    if(tittle.value){
      tittle.value.style.letterSpacing = '4px'
    }
  }, 500);

  window.addEventListener('resize',  rescaleElements);
    const courseUrl = 'http://127.0.0.1:8000/api/course-design/' + courseId
    const response = await axios.get(courseUrl)
    Course.value.push(response.data[0])
    console.log("response ",response.data[0])
  }
)

</script>

<template>
  <el-container>
    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>
    <el-main 
        :style="{ paddingLeft: dynamicBannerPadding + 'px',
         paddingRight: dynamicBannerPadding + 'px'}"
         v-for="course in Course"
         >
      <div id="banner">
        <div id="decorative-divider" >
          <h1 ref="tittle" id="tittle">{{ course.name }}</h1>
          <p id="illustration">
            {{ course.illustration }}
          </p>
        </div>
      </div>
      <div class="Center-Flex">
        <div id="course-info-container">
          <CourseHeader
              :image-url="course.image"
              :introduction="course.introduction"
              :statistics="course.statistics"
          />

          <el-divider id="add-course-divider">
            <el-button round style="width: 180px"  type="primary">加入课程</el-button>
          </el-divider>

          <InfoTabs :course="course"/>
        </div>
      </div>
    </el-main>
  </el-container>

</template>

<style scoped>
#add-course-divider{
  margin-top: 48px;
  margin-bottom: 48px;
}
#banner{
  margin-top: 16px;
  background: radial-gradient(circle,
  var(--el-color-primary),
  var(--el-color-primary-light-3));
  border-radius: 8px;
  box-shadow: #8080FF 0 0 16px;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 128px;
  padding-bottom: 24px;
  transition: 0.5s;
}
#tittle{
  color: var(--el-color-white);
  font-size: 32px;
  margin-bottom: 12px;
  letter-spacing: 0px;
  transition: 1s;
}
#illustration{
  color: var(--el-color-white);
  font-size: 14px;
}

#course-info-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 8px;
  margin: -24px 128px 0px;
  flex-direction: column;
  padding: 32px;
  background: var(--el-bg-color);
}

#decorative-divider{
  padding-left: 18px;
  padding-right: 18px;
  border-left: #efefefaa 1px solid;
  border-right: #efefefaa 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>