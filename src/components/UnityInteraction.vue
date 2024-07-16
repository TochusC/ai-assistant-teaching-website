<script setup>
import {useAuth} from "@/assets/static/js/useAuth.js";

const { login, logout } = useAuth();
import {onMounted, ref} from 'vue'
import {useRoute} from "vue-router";
import {ChatLineSquare, Delete, Microphone, More, Promotion} from "@element-plus/icons-vue";
import router from "@/router/index.js";
import {ElMessage} from "element-plus";
import axios from "axios";
import {backendUrl, llmUrl} from "@/assets/static/js/severConfig.js";

const isChatting = ref(false)
const userChatText = ref('')


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

window.handleUnityTransmission = function(str) {
  const currentRoute = router.path;
  console.log(str);
  if(str.startsWith("<网站指令>")){
    let command = str.substring(6)

    ElMessage({
      message: '小慧正在帮你...' + command + "!",
      type: 'success',
      appendTo: interaction.value
    })

    if(command === "打开注册表单" || command === "打开登录表单" || command === "退出登录"){
      if(currentRoute !== '/login'){
        logout();
      }

      if (command === "打开注册表单") {
        router.push({path: '/login', query: {form: 'register'}})
      }
      else if (command === "打开登录表单") {
        router.push({path: '/login', query: {form: 'login'}})
      }
      else{
        router.push({path: '/login'})
      }
    }
    else if(command === "打开课程：计算机网络原理"){
      router.push({path: '/course/1'})
    }
    else if(command === "打开我的学堂"){
      router.push({path: '/academy'})
    }
  }
  else if(str.startsWith("<用户输入>")){
    ElMessage({
      message: '识别到用户语言:' + str.substring(6),
      type: 'success',
      appendTo: interaction.value
    })
  }
  else if(str.startsWith("<LLM回复>")){
    ElMessage({
      message: '小慧的回复已生成：' + str.substring(7),
      type: 'success',
      appendTo: interaction.value
    })
    ElMessage({
      message: '正在合成小慧的语音...',
      appendTo: interaction.value
    })
  }
  else if(str.startsWith("<聊天完成>")){
    isChatting.value=false;
    ElMessage({
      message: '希望你对小慧感到满意🌟',
      type: 'success',
      appendTo: interaction.value
    })
  }
  else if(str.startsWith("<请求失败>")){
    isChatting.value=false;
    ElMessage({
      message: '发生错误！' + str,
      type: 'error',
      appendTo: interaction.value
    })
  }
}

const isVoiceRecording = ref(false)

const emit = defineEmits(['changeRemoteServer', 'summarizeWebsite'])

const route = useRoute()

const websiteDescription = {
  '/login': '网页内容：智能教学运营辅助平台的登录页面，在这里可以登录你的账号，或进行账号注册',
  '/':'网页内容：智能教学运营辅助平台的主页，在这里看到一些课程的推荐',
  '/course/1': '网页内容：计算机网络原理的课程页面，你可以在这里看到课程相关信息',
}

const voiceChatBtn = ref(null)


const handleSummarizeWebsite = () => {
  var path = route.path
  var description = websiteDescription[path]
  console.log(description)

  UnityIns.SendMessage('ChatManager',
      'StartChat', '请你帮我总结下面网页的内容，并向我介绍下如何使用该网页'
      + description);
}


const startRecordingVoice = () => {
    isVoiceRecording.value = true;
    isChatting.value = true;
    UnityIns.SendMessage('ChatManager',
      'StartRecorderFunc');
}

const endRecordingVoice = () => {
  isVoiceRecording.value = false;
  UnityIns.SendMessage('ChatManager',
      'EndRecorderFunc');
  voiceOff();
}

const sendUserText = () => {
  isChatting.value = true
  UnityIns.SendMessage('ChatManager',
      'StartChat', userChatText.value);
  userChatText.value = ""
  textOff();
}

const interaction = ref(null);
const cameraVideo = ref(null)
const cameraPhoto = ref(null)
const imageDate = ref('')
const analysis = ref(null)
const mediaSteam = ref(null)
const rawImage = ref('')

const initMedia = () => {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert("浏览器不支持getUserMedia! 将无法进行语音交互");
  }
  else{
    navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true,
    }).then((stream) => {
      mediaSteam.value = stream
      let cv = document.getElementById('cameraVideo')
      let cp = document.getElementById('cameraPhoto')
      cameraVideo.value = cv
      cameraPhoto.value = cp
      cv.srcObject = stream
    }).catch((err) => {
      ElMessage({
        title: '打开麦克风、摄像头失败❌',
        type: 'error',
        message: '出现问题啦，我们无法看到你的小表情奥😣' + err,
        duration: 4000
      })
    })
  }
  const voiceOff = () => {
    const canvas = cameraPhoto.value.getContext('2d')
    canvas.drawImage(
        cameraVideo.value,
        0, 0,
        cameraPhoto.value.width,
        cameraPhoto.value.height)
    fetchFaceAnalysis(3)
  }

}

const textOff = () => {
  const canvas = cameraPhoto.value.getContext('2d')
  canvas.drawImage(
      cameraVideo.value,
      0, 0,
      cameraPhoto.value.width,
      cameraPhoto.value.height)
  fetchFaceAnalysis(2)
}

const fetchFaceAnalysis = (type) => {
  cameraPhoto.value.toBlob((blob) => {
    const formData = new FormData()
    formData.append('img', blob, 'face.png')
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    const reader = new FileReader()
    reader.onload = function(e) {
      rawImage.value = e.target.result;
    };
    reader.readAsDataURL(blob)
    axios.post(llmUrl+'face/analysis/', formData, config)
        .then((res) => {
          imageDate.value = 'data:image/png;base64,' + res.data['img']
          analysis.value = res.data['analysis']

          const formData = new FormData;
          formData.append('image',
              rawImage.value)
          formData.append('type', 1)
          formData.append('processed_image',
              imageDate.value)
          formData.append('age',
              analysis.value.result.face_list[0].age)
          formData.append('gender',
              analysis.value.result.face_list[0].gender.type)
          formData.append('gender_probability',
              analysis.value.result.face_list[0].gender.probability)
          formData.append('emotion',
              analysis.value.result.face_list[0].emotion.type)
          formData.append('emotion_probability',
              analysis.value.result.face_list[0].emotion.probability)
          formData.append('left_eye_open',
              analysis.value.result.face_list[0].eye_status.left_eye)
          formData.append('right_eye_open',
              analysis.value.result.face_list[0].eye_status.right_eye)
          formData.append('type', type);

          const {user} = useAuth()
          axios.post(backendUrl+'student/emotion/' + user.value.ident, formData)
              .then((res) => {
                ElMessage({
                  title: '情绪记录成功✔',
                  type: 'success',
                  message: '你的小情绪已经被记录啦😉，快去看看吧！',
                  duration: 4000
                })
              })
              .catch((err) => {
                ElMessage({
                  title: '拍照失败❌',
                  type: 'error',
                  message: '出现问题啦，我们无法看到你的小表情奥😣',
                  duration: 4000
                })
              })
        })
        .catch((err) => {
          console.log(err)
        })
  })
}

const {user} = useAuth();
initMedia()
</script>

<template>
  <div id="InteractionContainer"
       ref="i"
       v-if="showAssistant">
    <div class="interaction—item">
      <el-button
          type="primary"
          @click="handleSummarizeWebsite"
          :loading="isCallBtnLoading">
        询问小慧有关当前页面的讯息...
      </el-button>
    </div>
    <div id="chat-container">
        <el-button :icon="Microphone"
                   type="primary"
                   size="large"
                   ref="voiceChatBtn"
                   :loading="isChatting"
                   v-if="!isVoiceRecording"
                   style="margin-bottom: 24px"
                   @click="startRecordingVoice"
                   round>
          开始语音...
        </el-button>
        <el-button
                   type="danger"
                   size="large"
                   ref="voiceChatBtn"
                   v-else
                   style="margin-bottom: 24px"
                   @click="endRecordingVoice"
                   round>
          <el-icon class="is-loading" style="margin-right: 8px">
            <More />
          </el-icon>
          结束语音并发送...
        </el-button>
      <el-input
          size="large"
          style="max-width: 360px; background: var(--el-bg-color);"
          clearable
          placeholder="请输入你向对小慧说的话..."
          v-model="userChatText"
      >
        <template #prepend>
          <el-icon>
            <ChatLineSquare/>
          </el-icon>
        </template>
      </el-input>

      <div style="width:100%;
      margin-top: 8px;
      padding-right: 32px;
      display: flex;
      justify-content: flex-end;"
      >
        <el-button type="info" :icon="Delete" @click="userChatText=''" :loading="isChatting">
          重置
        </el-button>
        <el-button type="success" :icon="Promotion" @click="sendUserText" :loading="isChatting">
          诉说
        </el-button>
      </div>
    </div>
  </div>
</template>

<style scoped>
#InteractionContainer{
  height: 100%;
  width: 100%;
  position: absolute;
}

.interaction—item{
  margin: 8px;
}
#chat-container{
  position: absolute;
  top:65%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>