<script setup lang="ts">
import HeadNavi from "@/components/MainPage/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {onMounted, ref} from "vue";
import router from "@/router";

const { isAuthenticated, user } = useAuth();
const dynamicCarouselHeight = ref('480px')
const rescaleElement = ref('')

const handleClickCourse = (id : number) => {
  router.push('/course/' + id)
}

onMounted(() => {
  if(isAuthenticated.value != true){
    router.push('/login')
  }
})

</script>

<template>
  <el-container>

    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>

    <el-main id = content-container>
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

      <el-divider content-position="left">
        <h1>精选好课</h1>
      </el-divider>

      <div class="course-container">
        <course-card
          course-name="计算机网络原理"
          course-description="深入剖析数字世界的联通之道"
          @click = "handleClickCourse(1)"
        >
          <img
              style="width: 230px"
              src="../assets/static/img/course/1/course.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>

      </div>

      <el-divider content-position="left"
        style="margin-top: 36px; margin-bottom: 36px"
      >
        <h1>我的课程</h1>
      </el-divider>

      <div class="course-container">
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

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.course-container {
  display: flex;
  justify-content: left;
  align-items: center;
  margin-top: 32px;
  margin-bottom: 32px;
}

#content-container {
  padding: 36px 64px 12px;
}
</style>