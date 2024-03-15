<script setup>

import { ref} from 'vue'
import {useRoute} from "vue-router";

const remoteServer = ref(0)

const props = defineProps({
  showAssistant: {
    type: Boolean,
    required: true
  },
  isCallBtnLoading: {
    type: Boolean,
    required: true
  },
})

const emit = defineEmits(['changeRemoteServer', 'summarizeWebsite'])

const route = useRoute()

const websiteDescription = {
  '/login': '网页内容：智能教学运营辅助平台的登录页面，在这里可以登录你的账号，或进行账号注册',
  '/':'网页内容：智能教学运营辅助平台的主页，在这里看到一些课程的推荐',
  '/course/1': '网页内容：计算机网络原理的课程页面，你可以在这里看到课程相关信息',
}


const handleSummarizeWebsite = () => {
  var path = route.path
  var description = websiteDescription[path]
  console.log(description)

  UnityIns.SendMessage('ChatManager',
      'chat', '请你帮我总结下面网页的内容，并向我介绍下如何使用该网页'
      + description);
}



</script>

<template>
  <div id="InteractionContainer"
       v-if="showAssistant">
    <div class="interaction—item">
      <el-button
          type="primary"
          @click="handleSummarizeWebsite"
          :loading="isCallBtnLoading">
        询问小慧有关当前页面的讯息...
      </el-button>
    </div>
    <div class="interaction—item">
      <el-select v-model="remoteServer"
                  @change="emit('changeRemoteServer', remoteServer)"
                 placeholder="请选择服务端">
         <el-option
             :key="0"
             :value="0"
             label="本地服务端"
         />
        <el-option
            :key="1"
            :value="1"
            label="云服务端"
        />
      </el-select>
    </div>
  </div>
</template>

<style scoped>
#InteractionContainer{
  position: absolute;
}

.interaction—item{
  margin: 8px;
}
</style>