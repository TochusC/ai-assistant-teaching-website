import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from "@/views/LoginPage.vue";
import MainPage from "@/views/MainPage.vue";
import CoursePage from "@/views/CoursePage.vue";
import MyAcademyPage from "@/views/MyAcademyPage.vue";
import Homework from "@/views/MyAcademy/Assignment/Homework.vue";
import Course from "@/views/MyAcademy/Assignment/Course.vue";
import Attendance from "@/views/MyAcademy/Assignment/Attendance.vue";
import MyCoursePage from "@/views/MyAcademy/MyCoursePage.vue";
import UserCenterPage from "@/views/UserCenterPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path:"/", component: MainPage},
    {path: "/login", component: LoginPage},
    {path:"/course/:id", component:CoursePage},
    {path:"/user/my-course/:id", component:MyCoursePage},
    {path:"/user/", component:UserCenterPage},
    {path:"/academy/", component:MyAcademyPage},
    {path:"/academy/homework/:id", component:Homework},
    {path:"/academy/course/:id", component:Course},
    {path:"/academy/attendance/:id", component:Attendance},
    {path:"/academy/my-course/:id", component:MyCoursePage},
  ]
})

export default router
