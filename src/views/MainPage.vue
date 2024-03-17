<script setup lang="ts">
import HeadNavi from "@/components/utils/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";

const router = useRouter()

const { isAuthenticated, user } = useAuth();
const dynamicCarouselHeight = ref('480px')
const rescaleElement = ref('')

const handleClickCourse = (id : number) => {
  router.push(`/course/${id}`)
}

onMounted(() => {
  if(isAuthenticated.value != true){
    router.replace('/login')
  }
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
    id: 1,
    name: "计算机网络原理",
    description: "深入剖析数字世界的联通之道",
    illustration: "国家级 | 工学 (08)/计算机类 (0809)",
    image: "@/assets/static/img/course/1/course.jpg",
  }
]

</script>

<template>
  <el-container>

    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>

    <el-main id="content-container">
      <el-carousel
          motion-blur
          direction="horizontal"
          height="500px"
          indicator-position="outside"
      >
        <el-carousel-item v-for="item in 4" :key="item">
          <h1 text="2xl" justify="center">{{ item }}</h1>
        </el-carousel-item>
      </el-carousel>

      <div class="primary-container">
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

        <el-divider
            content-position="left"
            class="info-divider">
           <h1>我的课程</h1>
        </el-divider>

        <div class="course-container">
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<style scoped>
.el-carousel__item h1 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
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

.course-container {
  padding-left: 32px;
  padding-right: 32px;
  margin-top: 32px;
  margin-bottom: 32px;
}

#content-container {
  padding: 36px 64px 12px;
}
html.dark #content-container {
}


</style>