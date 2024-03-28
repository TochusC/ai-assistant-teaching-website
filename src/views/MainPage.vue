<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import AIOpinion from "@/components/utils/AIOpinion.vue";

const router = useRouter()

const dynamicCarouselHeight = ref('480px')
const rescaleElement = ref('')

const handleClickCourse = (id) => {
  router.push(`/course/${id}`)
}

onMounted(() => {

})

const course_brief = [
  {
    id: 1,
    name: "计算机网络原理",
    description: "深入剖析数字世界的联通之道",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course.jpg",
  },
  {
    id: 2,
    name: "计算机组成原理",
    description: "深入探索计算机系统的核心构造",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course1.jpg",
  },
  {
    id: 3,
    name: "计算机操作系统",
    description: "深入理解现代操作系统的设计与实现",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course1.jpg",
  },
  {
    id: 4,
    name: "数据结构",
    description: "探索数据组织、管理和存储的高效方法",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course1.jpg",
  }
]

const propagandaImages = [
  {
    name: "AI Empowered",
    image: "../assets/static/img/propaganda/1.jpg"
  },
  {
    name: "AI Empowered",
    image: "@/assets/static/img/propaganda/2.jpg"
  },
  {
    name: "AI Empowered",
    image: "@/assets/static/img/propaganda/2.jpg"
  },
  {
    name: "AI Empowered",
    image: "@/assets/static/img/propaganda/2.jpg"
  },
  {
    name: "AI Empowered",
    image: "@/assets/static/img/propaganda/2.jpg"
  },
]
</script>

<template>
  <el-container>

    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>

    <el-main >
      <el-scrollbar>
        <div id="content-container">
          <el-carousel
              style="
              margin-bottom: 24px;
              background: var(--el-bg-color);
              box-shadow: 0 0 8px #8080FF;
              border-radius: 8px"
              motion-blur
              direction="horizontal"
              height="480px"
              indicator-position="outside"
          >
            <el-carousel-item
                v-for="item in 5"
                :key="item">
              <img src="@/assets/static/img/propaganda/poster.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
            </el-carousel-item>
          </el-carousel>

          <AIOpinion :prompt="'你好小慧，给大家说一句激起未来希望的话！'"/>


          <div id="primary-container">
            <el-divider content-position="left">
              <h1>精选好课</h1>
            </el-divider>

            <div class="course-container">
              <el-scrollbar>
                <course-card
                    style="display: inline-flex"
                    v-for="course in course_brief"
                    :key="course.id"
                    :brief="course"
                    @click = "handleClickCourse(course.id)"
                  />
              </el-scrollbar>
            </div>

            <!-- <el-divider
                content-position="left"
                class="info-divider">
               <h1>我的课程</h1>
            </el-divider> -->

            <div class="course-container">
            </div>
          </div>
        </div>
      </el-scrollbar>
    </el-main>
  </el-container>
</template>

<style scoped>
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
.info-divider{
  margin-top: 36px;
  margin-bottom: 36px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
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