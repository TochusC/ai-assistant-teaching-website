<script setup>
import {useRoute} from "vue-router";
import {Delete, Flag, Help, HelpFilled, Promotion, StarFilled, UploadFilled} from "@element-plus/icons-vue";
import BlankPage from "@/views/BlankPage.vue";
import {onMounted, ref} from "vue";
import AITextLong from "@/components/utils/AITextLong.vue";
import AIEvaluatePanel from "@/components/utils/AIEvaluatePanel.vue";
import AISimilarQuestion from "@/components/utils/AISimilarQuestion.vue";
import axios from "axios";
import {backendUrl, llmApi} from "@/assets/static/js/severConfig.js";
import ProblemInspect from "@/components/MyAcademyPage/ProblemPage/ProblemInspect.vue";
import {ElMessage} from "element-plus";


const route = useRoute()
const userInput = ref("")
const showPromptByInput = ref(false)
const showAnswer=ref(false)
const showEvaluation = ref(false)

const evaluateUserInput = () =>{
  showEvaluation.value=true
}

const questionNum = ref([])

const problemId = route.params.id
const problem = ref({})
const answer = ref(null)
const isLoading = ref(true)
const fetchProblem = () => {
  axios.get(backendUrl + 'problem/' + problemId)
      .then((res) => {
        problem.value = res.data
        isLoading.value = false
        fetchAnalysis()
      })
      .catch((err) => {
        console.log(err)
        isLoading.value = false
      })
}

const analysis = ref([])
const isAnalysisLoading = ref(true)
const fetchAnalysis = () => {
  const analysisUrl = llmApi + 'question/' + 'analysis/';
  const formData = new FormData();
  formData.append('userText', problem.value.description);
  axios.post(analysisUrl, formData).then((response) => {
    analysis.value = response.data.split(';')
    console.log(analysis.value)
    isAnalysisLoading.value = false;
  }).catch((error) => {
    ElMessage(
        {
          message: '小慧好像暂时不在线哦。',
          type: 'warning'
        }
    )
    isAnalysisLoading.value = false;
  })
}


const keyConcepts = ref([])
const fetchKeyConcept = () => {
  axios.get(backendUrl + 'problem/' +  'key_concept/' + problemId)
      .then((res) => {
        keyConcepts.value = res.data
        for (let keyConcept of keyConcepts.value){
          keyConcept.difficulty = keyConcept.difficulty / 20
          keyConcept.importance = keyConcept.importance / 20
        }
        isLoading.value = false
      })
      .catch((err) => {
        console.log(err)
        isLoading.value = false
      })
}
onMounted(async() => {
  fetchProblem()
  fetchKeyConcept()
})
</script>

<template>
  <el-scrollbar>
  <BlankPage v-loading="isLoading">
    <template #default>
      <el-tabs type="border-card">
        <el-tab-pane label="作业详情" display-directive="show:lazy">
          <div>
            <h1 style="margin-bottom: 12px">{{ problem.title }}</h1>
            <el-text style="display: block">{{ problem.description}}</el-text>
            <el-divider/>
            <ProblemInspect
                :key-concepts="keyConcepts"
                :problem="problem"
                :statistics="analysis"
            />

            <el-divider/>
            <div style="
                width: 100%;
              ">
              <el-input
                  resize="none"
                  maxlength="2048"
                  type="textarea"
                  placeholder="请输入作业内容"
                  :show-word-limit="true"
                  v-model="userInput"
                  :autosize="{ minRows: 18, maxRows: 24 }"
              />
            </div>
            <div style="width:100%;
                  margin-top: 8px;
                  display: flex;
                  justify-content: flex-end;"
            >
              <el-button
                  type="primary"
                  :icon="StarFilled"
                  @click="showPromptByInput=true">
                让小慧给点提醒
              </el-button>
              <el-button type="info" :icon="Delete" @click="userInput=''">
                重置
              </el-button>
              <el-button type="success" :icon="Promotion" @click="evaluateUserInput">
                提交
              </el-button>
            </div>
            <AITextLong
                @closeText="showPromptByInput=false"
                style="margin-top: 24px" v-if="showPromptByInput"
                :prompt="'这是我在做的题目：' + problem.description + '\n下面是我的答案：' + userInput + '\n请你根据我的答案给我点提示。' "/>
            <div style="
        width: 100%;
      ">
              <AIEvaluatePanel style="margin-top: 24px" @closeText="showEvaluation=false"
                               v-if="showEvaluation" :prompt="'这是我在做的题目：'
                    + problem.description + '\n下面是我的答案：' + userInput +
            '请你根据我的答案给我总结点评，并以百分制形式给出得分，请在最后把得分用<>包裹输出，例如：得分<70>分' "/>
            </div>
          </div>
        </el-tab-pane>
        <el-tab-pane label="相似例题">
          <div>
            <h1>{{ problem.title }}</h1>
            <el-text style="display: block">{{ problem.description}}</el-text>
            <div >
              <el-button
                  @click="questionNum.push(1)"
                  :icon="StarFilled"
                  type="primary" style="margin-top: 8px">
                点击让小慧生成更多相似题目</el-button>
              <el-button
                  @click="questionNum=[]"
                  :icon="Delete"
                  type="info" style="margin-top: 8px">
                清空</el-button>
            </div>
            <div style="
                  width: 100%;
                ">
              <el-divider/>
              <div style="height: 640px">
                <el-empty v-if="questionNum.length === 0" description="暂无题目"/>
                <el-scrollbar style="width: 100%; border: 1px solid #8080ff66; border-radius: 8px" v-else>
                  <AISimilarQuestion
                      @generateComplete="console.log('what?')"
                      style=" margin-top: 24px; margin-left: 24px; margin-right: 24px"
                      @closeText="showEvaluation=false"
                      v-for="item in questionNum" :prompt="problem.description"/>
                </el-scrollbar>
              </div>
            </div>
          </div>
        </el-tab-pane>
      </el-tabs>
      <el-divider/>
    </template>
  </BlankPage>
  </el-scrollbar>
</template>

<style scoped>

</style>