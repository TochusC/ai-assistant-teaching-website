import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from "@/views/LoginPage.vue";
import MainPage from "@/views/MainPage.vue";
import CoursePage from "@/views/CoursePage.vue";
import MyAcademyPage from "@/views/MyAcademy/MyAcademyPage.vue";
import Course from "@/views/MyAcademy/Assignment/Course.vue";
import Attendance from "@/views/MyAcademy/Assignment/Attendance.vue";
import MyCoursePage from "@/views/MyAcademy/MyCoursePage.vue";
import UserCenterPage from "@/views/UserCenterPage.vue";
import TeacherPortal from "@/views/TeachingPortal.vue";
import NotFoundPage from "@/views/InfoPage/NotFoundPage.vue";

import {useAuth} from "@/assets/static/js/useAuth"
import TeachOverview from "@/views/TeachingPortal/TeachOverview.vue";
import ProblemPage from "@/views/MyAcademy/ProblemPage.vue";
import CourseCreate from "@/views/TeachingPortal/CourseManagement/CourseCreate.vue";
import StudentOverview from "@/views/TeachingPortal/StudentManagement/StudentOverview.vue";
import StudentInfo from "@/views/TeachingPortal/StudentManagement/StudentInfo.vue";
import ParentPage from "@/views/ParentPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {path:"/", redirect: "/portal"},
    {path: "/login", component: LoginPage, meta: {requiresAuth: false}},
    {path:"/portal", component: MainPage, meta: {requiresAuth: false}},
    {path:"/course/:id", component:CoursePage, meta: {requiresAuth: false}},

    {path:"/404", component: NotFoundPage, meta: {requiresAuth: false}},

    {path:"/user/my-course/:id", component:MyCoursePage, meta: {requiresAuth: true, role: "student"}},
    {path:"/user/", component:UserCenterPage, meta: {requiresAuth: true, role: "student"}},
    {path:"/academy",
          component:MyAcademyPage,
          meta: {requiresAuth: true, role: "student"},
          children: [
                {
                    path: "course/:id",
                    component: Course,
                    meta: {requiresAuth: true, role: "student"},
                },
                {
                    path: "attendance/:id",
                    component: Attendance,
                    meta: {requiresAuth: true, role: "student"},
                },
                {
                    path: "my-course/:id",
                    component: MyCoursePage,
                    meta: {requiresAuth: true, role: "student"},
                }
            ]
      },
      {path:"/academy/problem/:id", component:ProblemPage, meta: {requiresAuth: true, role: "student"}},
    {path:"/teaching",
        component: TeacherPortal,
        meta: {requiresAuth: true, role: "teacher"},
        children: [
            {
                path: 'portal',
                component: TeachOverview,
                meta: {requiresAuth: true, role: "teacher"},
            },
            {
                path: 'course',
                meta: {requiresAuth: true, role: "teacher"},
                children:[
                    {
                        path: 'create',
                        component: CourseCreate,
                        meta: {requiresAuth: true, role: "teacher"},
                    }
                ]
            },
            {
                path: 'student',
                meta: {requiresAuth: true, role: "teacher"},
                children:[
                    {
                        path: 'overview',
                        component: StudentOverview,
                        meta: {requiresAuth: true, role: "teacher"},
                    },
                    {
                        path: 'info/:id',
                        component: StudentInfo,
                        meta: {requiresAuth: true, role: "teacher"},
                    }
                ]
            }
        ]
    },
      {path: "/parent", component: ParentPage, meta: {requiresAuth: true, role: "parent"}},
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
