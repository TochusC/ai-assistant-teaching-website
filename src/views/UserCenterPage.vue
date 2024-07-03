<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";
import {ref} from "vue";
import AccountManagement from "@/components/UseCenterPage/AccountManagement.vue";
import UserInformation from "@/components/UseCenterPage/UserInformation.vue";
import HomeSchoolInformation from "@/components/UseCenterPage/HomeSchoolInformation.vue";
import EmotionRecord from "@/components/UseCenterPage/EmotionRecord.vue";


const activeTab = ref('profile')
</script>

<template>
  <el-container >
    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>
    <el-main >
      <div class="Center-Flex" >
        <div id="content" style="max-width: 1024px">
          <el-backtop :right="100" :bottom="100" />
          <div id="course-div">
            <el-scrollbar>
              <el-tabs v-model="activeTab">
                <el-tab-pane label="基本信息" name="profile">
                  <UserInformation/>
                </el-tab-pane>
                <el-tab-pane label="家校认证" name="homeSchool">
                  <HomeSchoolInformation/>
                </el-tab-pane>
                <el-tab-pane label="情绪记录" name="emotion">
                  <EmotionRecord/>
                </el-tab-pane>
                <el-tab-pane label="账号管理" name="account">
                  <AccountManagement/>
                </el-tab-pane>
              </el-tabs>
            </el-scrollbar>
          </div>
        </div>
      </div>
    </el-main>
  </el-container>

</template>

<style scoped>
#content{
  padding: 32px;
  width: 100%;
  height: 100%;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  background: var(--el-bg-color);
  min-width: 760px;
  display: flex;
  margin: 24px 128px 0px;
  flex-direction: column;
}
#course-div{
  width: 100%;
}
</style>