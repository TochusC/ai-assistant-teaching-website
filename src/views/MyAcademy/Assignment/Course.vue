<script setup>

import BlankPage from "@/views/BlankPage.vue";
import {ref, onMounted, inject} from "vue";
import ResourceCard from "@/components/MyAcademyPage/ResourceCard.vue";
import axios from "axios";

let resources = null;
const videoResource = ref(null);
const pptResource = ref(null);
const docResource = ref(null);
const isLoading = ref(true);

const cdnServerUrl = inject('cdnServerUrl');

const course = {
  id: 589,
  name: "第一章课程",
  description: "请自行完成学习",
  startTime: "2024.03.16 21:23",
  endTime: "2024.04.15 00.00",
  announceTime: "2024.03.16 21:23",
  course: {
    id: 327,
    name: "计算机网络原理"
  },
}

let resourceRootUrl = null;

onMounted( async () => { 
  resourceRootUrl = cdnServerUrl.value + `course/` + course.course.id + `/`
      + course.id + `/`;

  const response = await axios.get(resourceRootUrl + 'description.json');
    
  resources = response.data;

  console.log(resources)

  for (let typeIndex in resources.type){
    if (resources.type[typeIndex] === "video"){
      videoResource.value = resources['video'];
    }
    else if (resources.type[typeIndex] === "ppt"){
      pptResource.value = resources['ppt'];
    }
    else if (resources.type[typeIndex] === "doc"){
      docResource.value = resources['doc'];
    }
  }
  isLoading.value = false;
})



</script>

<template>
  <BlankPage>
    <div style="padding-left: 36px; padding-right: 36px">
      <h1 style="margin-bottom: 24px">{{ course.name }}</h1>
      <el-tabs v-loading="isLoading" type="border-card">
        <el-tab-pane label="课程简介">
          <el-text>{{ course.description }}</el-text>
        </el-tab-pane>
        <el-tab-pane label="课程视频">
          <ResourceCard
              v-for="resource in videoResource"
              :resource_root="resourceRootUrl"
              resource_type="video"
              :resource="resource"
          />
          <el-empty description="空空如也" v-if="!videoResource"/>
        </el-tab-pane>
        <el-tab-pane label="课程PPT">
          <ResourceCard
              v-for="resource in pptResource"
              :resource_root="resourceRootUrl"
              resource_type="ppt"
              :resource="resource"
          />
          <el-empty description="空空如也" v-if="!videoResource"/>
        </el-tab-pane>
        <el-tab-pane label="课程文档">
          <ResourceCard
              v-for="resource in docResource"
              :resource_root="resourceRootUrl"
              resource_type="doc"
              :resource="resource"
          />
          <el-empty description="空空如也" v-if="!videoResource"/>
        </el-tab-pane>
      </el-tabs>

    </div>
  </BlankPage>
</template>

<style scoped>

</style>