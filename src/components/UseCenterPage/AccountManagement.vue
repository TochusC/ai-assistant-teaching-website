<script setup lang="ts">
import HeadNavi from "@/components/utils/HeadNavi.vue";
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";
import {useAuth} from "@/assets/static/js/useAuth";
import {onMounted, ref} from "vue";
onMounted(() => {
    
})


</script>

<template>
    <div id = "all-container">
        <div id="propaganda-container">
            <p id = "title">修改密码</p>
            <p id = "text">设置复杂密码更能保护您的账号安全</p>
        </div>
        <div id="login-container">
            <el-button type="info" style="margin-left:100px;margin-top:20px">修改</el-button>
        </div>
    </div>
    <div class="divider"></div>
    <div id = "all-container">
        <div id="propaganda-container">
            <p id = "title">修改认证信息</p>
            <p id = "text">认证信息与您的成绩相关，请谨慎修改</p>
        </div>
        <div id="login-container">
            <el-button type="info" style="margin-left:100px;margin-top:20px">修改</el-button>
        </div>
    </div>
    <div class="divider"></div>
    <div id = "all-container">
        <div id="propaganda-container">
            <p id = "title">账号注销</p>
            <p id = "text">为保证您的账号安全，需要满足相应的条件，才能提交注销申请</p>
        </div>
        <div id="login-container">
            <el-button type="info" style="margin-left:100px;margin-top:20px">注销</el-button>
        </div>
    </div>
    <div class="divider"></div>
</template>

<style scoped>
#title{
    color:black;
    font-size:18px;
    margin-left:20px;
    margin-bottom: 15px;
}
#text{
    color:gray;
    font-size:14px;
    margin-left:20px;
}
#all-container{
  display: flex;
  height: 100%;
  width: 100%;
}
#propaganda-container{
  flex: 8;
  height: 50%;
  width: 50%;
  background-size: cover;
}
#login-container{
  flex: 4;
  height: 100%;
  width: 100%;
}
.divider {
  width: 85%;
  height: 1px;
  background-color: #ccc;
  margin: 20px;
  margin-bottom: 30px;
}
</style>