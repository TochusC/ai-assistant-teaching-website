<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";
import CourseCard from "@/components/MainPage/CourseCard.vue";
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import axios from "axios";
import {backendUrl, llmUrl} from "@/assets/static/js/severConfig.js";
import {ElMessage, ElNotification} from "element-plus";
import {Camera} from "@element-plus/icons-vue";
import {useAuth} from "@/assets/static/js/useAuth.js";

const router = useRouter()
const isLoadingCourse = ref(true)

const handleClickCourse = (id) => {
  router.push(`/course/${id}`)
}

const course = ref(null)
const fetchCourseBrief = () => {
  isLoadingCourse.value = true
  axios.get(backendUrl+'/course')
      .then((res) => {
        course.value = res.data
        isLoadingCourse.value = false
      })
      .catch((err) => {
        ElNotification({
          title: '错误',
          message: '获取课程信息失败' + err,
          type: 'error',
          offset: 64,
          duration: 2000
        })
        isLoadingCourse.value = false
      })
}

const cameraVideo = ref('')
const cameraPhoto = ref('')
const imageDate = ref('')
const analysis = ref(null)
const mediaSteam = ref(null)
const rawImage = ref('')

const initMedia = () => {
  navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true,
  }).then((stream) => {
    mediaSteam.value = stream
    cameraVideo.value.srcObject = stream
  }).catch((err) => {
    ElMessage({
      title: '打开麦克风、摄像头失败❌',
      type: 'error',
      message: '出现问题啦，我们无法看到你的小表情奥😣',
      duration: 4000
    })
  })
}
const handleCamera = () => {
  const canvas = cameraPhoto.value.getContext('2d')
  canvas.drawImage(
      cameraVideo.value,
      0, 0,
      cameraPhoto.value.width,
      cameraPhoto.value.height)
  fetchFaceAnalysis()
}
const fetchFaceAnalysis = () => {
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

          console.log(analysis.value)

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
          formData.append('type', 1);

          const {user} = useAuth()
          console.log(user)
          axios.post(backendUrl+'student/emotion/' + user.value.ident, formData)
              .then((res) => {
                ElMessage({
                  title: '拍照成功✔',
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
const emotionStatus = ref(0)
const fetchEmotionStatus = () => {
  const {user} = useAuth()
  axios.get(backendUrl + 'student/emotion/status/' + user.value.ident)
      .then((res) => {
        emotionStatus.value = parseFloat(res.data.message)
      })
      .catch((err) => {
        ElMessage({
          title: '获取活力状态失败❌',
          type: 'error',
          message: '出现问题啦，我们无法获取到你的活力状态😣',
          duration: 4000
        })
      })
}

onMounted(() => {
  fetchCourseBrief()
  fetchEmotionStatus()
  initMedia()
})
</script>

<template>
  <el-scrollbar>
    <el-container>
      <el-header style="padding: 0;">
        <HeadNavi/>
      </el-header>
      <el-main>
          <div id="content-container">
            <el-carousel
                style="
                margin-bottom: 24px;
                background: var(--el-bg-color);
                box-shadow: 0 0 8px #8080FF;
                border-radius: 8px"
                motion-blur
                direction="horizontal"
                height="480px"
                indicator-position="outside"
            >
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster1.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster2.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster3.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster4.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
              <el-carousel-item>
                <img src="@/assets/static/img/propaganda/poster5.png" style="width: 100%; height: 100%; object-fit: cover; " alt=""/>
              </el-carousel-item>
            </el-carousel>

            <AIOpinion :prompt="'你好小慧，给大家说一句激起未来希望的话！'"/>

            <div class="glowing-container"
                 style="
                 display: flex;
                 margin-top: 24px;
                 align-content: center;
                 flex-direction: column;
                 justify-content: center">
              <el-divider content-position="left">
                <h3>你好，{{user.name}}同学👋</h3>
              </el-divider>
              <div class="Center-Flex"
                   style="flex-direction: column"
              >
                <div class="Space-Between-Flex" style="margin-top:12px; width: 100%; padding-left: 24px; padding-right: 24px">
                  <el-divider content-position="left" style="max-width: 420px ">活力状态</el-divider>
                  <el-divider content-position="left">学习建议</el-divider>
                </div>
                <div style="margin-top:8px; width: 100%; padding-left: 24px; padding-right: 24px" class="Space-Between-Flex">
                  <div class="Center-Flex" style="flex-direction: column;width: 100%;max-width: 420px; margin-left: 12px">
                    <div style="width: 100%;margin-bottom: 36px;">
                      <el-text style="white-space: nowrap">
                        根据测量的小情绪，你的活跃值为：
                      </el-text>
                    </div>
                    <n-progress
                        type="line"
                        :percentage="emotionStatus.toFixed(2)"
                        :status="emotionStatus >= 80 ? 'success' :
                                   emotionStatus >= 60 ? 'info':
                                   emotionStatus >= 40 ? 'default':
                                   emotionStatus >= 20 ? 'warning' : 'danger'"
                        :height="32"
                        :indicator-placement="'inside'"
                        processing
                    />
                  </div>
                  <el-divider direction="vertical" style="height: 160px"/>
                  <div class="Center-Flex">
                    <div v-if="emotionStatus <= 20">
                      <p style="margin-bottom: 24px">学习路上，每个人都会有低谷时刻，重要的是不放弃。记住，每一步都算数，即使进步微小，也是向前的力量。给自己一些时间和空间，慢慢找回学习的节奏。</p>
                      <el-text style="margin-bottom: 24px">尝试通过设定小目标来激励自己，例如每天学习10分钟。选择自己感兴趣的 topic，让学习变得更有趣味。同时，与同学或老师交流，寻求支持和鼓励。</el-text>
                      <p style="margin-top: 24px">不要沮丧，我们会一直陪伴着你的✨</p>
                    </div>
                    <div v-else-if="emotionStatus <= 40">
                      <p style="margin-bottom: 24px">学习是一场马拉松，不是百米冲刺。保持耐心，相信自己的潜力。每个人都有自己的节奏，重要的是找到适合自己的步伐，不断前进。</p>
                      <el-text >分解学习任务，将其拆分成小块，一步一步完成。尝试多样化的学习方法，如观看教学视频、参与小组讨论等，以增加学习的趣味性。同时，记得给自己设定奖励，每完成一个任务就给自己一些奖励，以提高学习的积极性。</el-text>
                      <p style="margin-top: 24px">坚持下去，你会发现自己的进步✨</p>
                    </div>
                    <div v-else-if="emotionStatus <= 60">
                      <p style="margin-bottom: 24px">你已经取得了一定的进步，继续保持！学习是一场旅程，享受过程，不断探索和挑战自己。坚持下去，你会收获意想不到的成果。</p>
                      <el-text >制定合理的学习计划，平衡学习与休息时间。利用学习工具和资源，如在线教育平台、图书等，提高学习效率。同时，定期回顾和总结所学内容，巩固知识。</el-text>
                      <p style="margin-top: 24px">总有一天，你所坚持的会跑过来拥抱你✨</p>
                    </div>
                    <div v-else-if="emotionStatus <= 80">
                      <p style="margin-bottom: 24px">你的努力和进步值得赞赏！继续保持这份热情和动力，你会在学习的道路上走得更远。相信自己的能力，勇敢面对挑战，不断超越自我。</p>
                      <el-text >尝试拓展学习领域，探索新的知识和技能。与同学或老师进行深入讨论，提出问题，解决问题。同时，参加学习小组或寻找学习伙伴，互相激励，共同进步。</el-text>
                      <p style="margin-top: 24px">你的努力会得到回报，继续前行✨</p>
                    </div>
                    <div v-else>
                      <p style="margin-bottom: 24px">你的学习状态非常棒！继续保持这份热情和动力，你会在学习的道路上走得更远。相信自己的能力，勇敢面对挑战，不断超越自我。</p>
                      <el-text >设定更高的学习目标，挑战自己，不断突破舒适区。利用学习资源，如学术论文、专业书籍等，深入研究所学领域。同时，分享自己的知识和经验，帮助他人，成为学习的榜样。</el-text>
                      <p style="margin-top: 24px">追风逐浪✨</p>
                    </div>
                  </div>
                </div>
                <el-divider style="margin-top: 46px">
                  <el-button
                      type="primary"
                      @click="handleCamera"
                      style="width: 120px;"
                      :icon="Camera"> 茄子🍆！
                  </el-button>
                </el-divider>
                <el-text >拍张照片记录一下你当前的心情吧？</el-text>
              </div>
              <video style="
                      background: #4ac1f7;
                      display: none"
                     ref="cameraVideo"
              />
              <canvas style="
                      background: #1f69c0;
                      display: none"
                      ref="cameraPhoto"
              />
            </div>

            <div id="primary-container">
              <el-divider content-position="left">
                <h1>精选好课</h1>
              </el-divider>

              <div class="course-container" v-loading="isLoadingCourse">
                <el-scrollbar>

                  <el-result
                      v-if="course === null"
                      icon="error"
                      title="获取课程失败"
                      sub-title="请稍后再试一试吧？"
                  >
                    <template #extra>
                      <el-button type="primary" @click="fetchCourseBrief">重试</el-button>
                    </template>
                  </el-result>
                  <course-card
                      style="display: inline-flex"
                      v-else
                      v-for="course in course"
                      :key="course.id"
                      :brief="course"
                      @click = "handleClickCourse(course.id)"
                  />
                </el-scrollbar>
              </div>
            </div>
          </div>
      </el-main>
    </el-container>
  </el-scrollbar>
</template>

<style scoped>
.el-carousel__item h1 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  text-align: center;
}
.info-divider{
  margin-top: 36px;
  margin-bottom: 36px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

#primary-container{
  margin-top: 24px;
  background: var(--el-bg-color);
  padding: 16px;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
}

.course-container {
  padding-left: 32px;
  padding-right: 32px;
  margin-top: 32px;
  margin-bottom: 32px;
}

#content-container {
  padding-left: 36px;
  padding-right: 36px;
  padding-top: 12px;
  width: 100%;
  height: 100%;
}



</style>