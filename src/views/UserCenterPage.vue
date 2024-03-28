<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";
import NoticeCard from "@/components/MyAcademyPage/NoticeCard.vue";
import MyCourseCard from "@/components/MyAcademyPage/MyCourseCard.vue";
import BlankPage from "@/views/BlankPage.vue";
import {useAuth} from "@/assets/static/js/useAuth";
import {onMounted, ref} from "vue";
import AccountManagement from "@/components/UseCenterPage/AccountManagement.vue";
import UserInformation from "@/components/UseCenterPage/UserInformation.vue";
onMounted(() => {
  const {user} = useAuth()
})

const ucflag = ref(false)

</script>

<template>
  <BlankPage>
    <template #default>
      <div id="course-div">
        <el-scrollbar>
            <el-menu  mode="horizontal">
                <el-menu-item @click = "ucflag = false">基本信息</el-menu-item>
                <el-menu-item @click = "ucflag = true" >账号管理</el-menu-item>
            </el-menu>
          <div id="course-container">
            <UserInformation v-if = "!ucflag"/>
            <AccountManagement v-else/>
          </div>
        </el-scrollbar>
      </div>
    </template>
  </BlankPage>
</template>

<style scoped>

#info-container{
  display: inline-flex;
  padding: 16px
}

#course-container{
  padding: 16px
}

#academy-info-container{
  display: flex;
  justify-content: center;
  align-items: center;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  flex-direction: column;
  padding: 32px;
  background: var(--el-bg-color);
  margin: 32px 256px 0;
}

#info-div{
  width: 100%;
}
#course-div{
  width: 100%;
}
</style>