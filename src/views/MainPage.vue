<script setup lang="ts">

import HeadNavi from "@/components/MainPage/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
</script>

<template>
  <el-container>

    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>

    <el-main style="padding-left: 36px;
padding-top: 12px; padding-bottom: 12px; padding-top: 36px">
      <el-carousel
          motion-blur
          direction="horizontal"
          height="360px"
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
        >
          <img
              style="width: 230px"
              src="@/assets/static/img/course/course1.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>

        <course-card
            course-name="计算机网络原理"
            course-description="深入剖析数字世界的联通之道"
        >
          <img
              style="width: 236px"
              src="@/assets/static/img/course/course1.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>

        <course-card
            course-name="计算机网络原理"
            course-description="深入剖析数字世界的联通之道"
        >
          <img
              style="width: 236px"
              src="@/assets/static/img/course/course1.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>
      </div>

      <el-divider content-position="left">
        <h1>我的课程</h1>
      </el-divider>

      <div class="course-container">
        <course-card
            course-name="计算机网络原理"
            course-description="深入剖析数字世界的联通之道"
        >
          <img
              style="width: 230px"
              src="@/assets/static/img/course/course1.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>

        <course-card
            course-name="计算机网络原理"
            course-description="深入剖析数字世界的联通之道"
        >
          <img
              style="width: 236px"
              src="@/assets/static/img/course/course1.jpg"
              class="image"
              alt="计算机网络原理"
          />
        </course-card>
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
</style>