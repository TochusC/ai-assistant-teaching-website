<script setup>
import {ref, onMounted, inject, provide} from 'vue';
import TeachSideNavi from "@/components/TeachingActivity/utils/TeachSideNavi.vue";
import TeachHeadNavi from "@/components/TeachingActivity/utils/TeachHeadNavi.vue";
import HeadNavi from "@/components/utils/HeadNavi.vue";

const windowWidth = inject('windowWidth');
const rescaleElement = () => {
  if (windowWidth.value < 800) {
    showAside.value = false;
  }
  else{
    showAside.value = true;
  }
}

onMounted(() => {
  rescaleElement()

  window.addEventListener('resize', () => {
    rescaleElement()
  })
  window.addEventListener('showAssistant', () => {
    rescaleElement()
  })
})

const showAside = ref(true)

const workObject = ref(null)
const workRule = ref(null)
provide('workObject', workObject)
provide('workRule', workRule)
</script>

<template>
    <el-container id="parent-container">
      <el-header style="padding: 0">
        <HeadNavi/>
      </el-header>
      <el-container id="body-container">
        <el-aside style="height: 100%" v-show="showAside">
          <TeachSideNavi/>
        </el-aside>
        <el-main style="height: 100%">
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
</template>

<style scoped>
#parent-container{
  height: 100%;
  width: 100%;
}
#body-container{
  margin-top: 4px;
  height: 100%;
}
</style>