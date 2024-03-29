<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import axios from "axios";
import { backendUrl} from "@/assets/static/js/severConfig.js";
import {ElNotification} from "element-plus";

const router = useRouter()
const isLoadingCourse = ref(true)

const dynamicCarouselHeight = ref('480px')
const rescaleElement = ref('')

const handleClickCourse = (id) => {
  router.push(`/course/${id}`)
}




const course_brief = ref(null)

const fetchCourseBrief = () => {
  isLoadingCourse.value = true
  axios.get(backendUrl+'api/course')
      .then((res) => {
        course_brief.value = res.data
        isLoadingCourse.value = false
      })
      .catch((err) => {
        ElNotification({
          title: '错误',
          message: '获取课程信息失败' + err,
          type: 'error',
          offset: 64,
          duration: 2000
        })
        isLoadingCourse.value = false
      })
}

onMounted(() => {
  fetchCourseBrief()
})


</script>

<template>
  <el-scrollbar>
    <el-container>
      <el-header style="padding: 0">
        <HeadNavi/>
      </el-header>
      <el-main>
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
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster1.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster2.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster3.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster4.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster5.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
            </el-carousel>

            <AIOpinion :prompt="'你好小慧，给大家说一句激起未来希望的话！'"/>

            <div id="primary-container">
              <el-divider content-position="left">
                <h1>精选好课</h1>
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
                  <course-card
                      style="display: inline-flex"
                      v-else
                      v-for="course in course_brief"
                      :key="course.Course_id"
                      :brief="course"
                      @click = "handleClickCourse(course.Course_id)"
                  />
                </el-scrollbar>
              </div>
            </div>
          </div>
      </el-main>
    </el-container>
  </el-scrollbar>
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