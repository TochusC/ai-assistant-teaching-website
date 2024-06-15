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
import TeacherPortal from "@/views/TeachingActivity/TeachingPortal.vue";
import NotFoundPage from "@/views/InfoPage/NotFoundPage.vue";

import {useAuth} from "@/assets/static/js/useAuth"
import {ElMessage} from "element-plus";
import TeachOverview from "@/views/TeachingActivity/TeachOverview.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: "/login", component: LoginPage, meta: {requiresAuth: false}},
    {path:"/portal", component: MainPage, meta: {requiresAuth: false}},
    {path:"/course/:id", component:CoursePage, meta: {requiresAuth: false}},

    {path:"/404", component: NotFoundPage, meta: {requiresAuth: false}},

    {path:"/user/my-course/:id", component:MyCoursePage, meta: {requiresAuth: true, role: "student"}},
    {path:"/user/", component:UserCenterPage, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy/", component:MyAcademyPage, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy/homework/:id", component:Homework, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy/course/:id", component:Course, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy/attendance/:id", component:Attendance, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy/my-course/:id", component:MyCoursePage, meta: {requiresAuth: true, role: "student"}},

    {path:"/teaching",
        component: TeacherPortal,
        meta: {requiresAuth: true, role: "teacher"},
        children: [
            {
                path: 'portal',
                component: TeachOverview,
                meta: {requiresAuth: true, role: "teacher"},
            },
        ]
    },
  ]
})

// 路由守卫
router.beforeEach((to, from, next) => {
    if (to.matched.length === 0) {
        next('/404'); // 重定向到404页面的路径
    }
    else{
        if (to.meta.requiresAuth) {
            const {isAuthenticated, user} = useAuth()
            if (!isAuthenticated) {
                next({path: "/login"})
            } else {
                if (to.meta.role === "student" && user.value.role !== "student") {
                    next({path: "/teaching/portal"})
                } else if (to.meta.role === "teacher" && user.value.role !== "teacher") {
                    next({path: "/portal"})
                } else {
                    next()
                }
            }
        } else {
            next()
        }
    }
})

export default router
