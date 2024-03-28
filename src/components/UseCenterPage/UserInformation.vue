<script setup lang="ts">
import HeadNavi from "@/components/utils/HeadNavi.vue";
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";
import {useAuth} from "@/assets/static/js/useAuth";
import {onMounted, ref} from "vue";
import {
  Check,
  Delete,
  Edit,
  Message,
  Search,
  Star,
} from '@element-plus/icons-vue'
const {user} = useAuth()
const radio = ref(3)
const phone = ref("19953111360")
onMounted(() => {
    
})
const handleFileUpload = () =>{

}
</script>

<template>
    <div id = "all-container">
        <div id="propaganda-container">
          <p>基本信息</p>
          <p>&nbsp;</p>
            <img src = '../../assets/static/img/boy.png' id = "custom-image"/>
            <el-button type="info" style="margin-left:30px;margin-top:20px">编辑图像</el-button>
        </div>
        <div id="login-container">
          <p>&nbsp;</p>
          <el-text id="textstyle">姓名:&nbsp&nbsp{{ user.name }}</el-text><br>
          <el-radio-group style = "margin-left:30px;margin-top:30px" v-model="radio">
            <el-radio :value="3">男</el-radio>
            <el-radio :value="6">女</el-radio>
          </el-radio-group>
          <p style = "margin:30px">联系方式</p>
          <el-form
            label-width="auto"
            style="max-width:300px;margin-left:30px;margin-top:30px"
          >
            <el-form-item label="邮箱">
              <el-input disabled placeholder="尚未绑定邮箱"/>
            </el-form-item>
            <el-form-item label="手机号">
              <el-input disabled placeholder="尚未绑定手机号" v-model = "phone"/>
            </el-form-item>
          </el-form>
        </div>
        <div id="infor" style = "border:1px solid #1a1a1a66;padding:10px;border-radius:8px">
            <el-text>认证信息</el-text>
            <el-divider />
            <el-text>身份&nbsp&nbsp学生</el-text><br><br>
            <el-text>学号&nbsp&nbsp{{ user.id }}</el-text><br><br>
            <el-text>学校&nbsp&nbspxxx大学</el-text><br><br>
            <el-text>学院&nbsp&nbsp计算机科学与技术学院</el-text><br><br>
            <el-text>入学年份&nbsp&nbsp2000</el-text><br><br>
        </div>
    </div>
</template>

<style scoped>
#custom-image {
  width: 150px;
  height: 150px;
}
#all-container{
  display: flex;
  height: 100%;
  width: 100%;
}
#propaganda-container{
  flex: 1;
  height: 50%;
  width: 50%;
  background-size: cover;
}
#login-container{
  flex: 4;
  height: 100%;
  width: 100%;
}
#infor{
  flex: 4;
  height: 100%;
  width: 100%;
}

#slogan{
  margin: 36px;
  font-weight: bold;
  color: #8080FF;
}
#textstyle{
  margin: 30px;
}
</style>