<script setup>
import {useRoute} from "vue-router";
import {Delete, Promotion, StarFilled, UploadFilled} from "@element-plus/icons-vue";
import BlankPage from "@/views/BlankPage.vue";
import {onMounted, ref} from "vue";
import AIOpinion from "@/components/utils/AIOpinion.vue";
import AITextLong from "@/components/utils/AITextLong.vue";
import VueMarkdown from 'vue-markdown-render'
import AIEvaluatePanel from "@/components/utils/AIEvaluatePanel.vue";
import AISimilarQuestion from "@/components/utils/AISimilarQuestion.vue";
const route = useRoute()

const homeworkId = route.params.id

const homework = {
  id: 1,
  name: "基础知识测验",
  description: "论述具有五层协议的网络体系结构的要点，包括各层的主要功能。",
  startTime: "2024.03.16 21:23",
  endTime: "2024.04.15 00.00",
  announceTime: "2024.03.16 21:23",
  course: {
    id: 1,
    name: "计算机网络原理"
  },
  allowDelay: true,
  allowRedo: true,
}
const userInput = ref("")
const showPrompt = ref(false)
const showPromptByInput = ref(false)
const showAnswer=ref(false)
const showEvaluation = ref(false)

const evaluateUserInput = () =>{
  showEvaluation.value=true
}
const questionNum = ref([])
const questionArray = ref([])
</script>

<template>
  <BlankPage>
    <template #default>
        <el-tabs type="border-card">
          <el-tab-pane label="作业详情" display-directive="show:lazy">
            <div>
              <h1>{{ homework.name }}</h1>
              <div>
                <el-tag effect="plain" type="info" style="margin: 12px 12px 12px 0">
                  {{ homework.startTime }} - {{ homework.endTime }}
                </el-tag>
                <el-tag v-if="homework.allowDelay" effect="plain" type="info" style="margin: 12px">
                  允许迟交
                </el-tag>
                <el-tag v-if="homework.allowRedo" effect="plain" type="info" style="margin: 12px">
                  允许重做
                </el-tag>
              </div>
              <el-text style="display: block">{{ homework.description}}</el-text>
              <el-button
                  @click="showPrompt = !showPrompt"
                  type="primary" style="margin-top: 8px" v-if="!showPrompt">点击让小慧给点建议吧？</el-button>
              <AITextLong v-else style="margin-top: 24px"
                         :prompt="'请用简要的一句话提示下我应该如何完成这个作业：' + homework.description"/>
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
                  :prompt="'这是我在做的题目：' + homework.description + '\n下面是我的答案：' + userInput + '\n请你根据我的答案给我点提示。' "/>
              <div style="
        width: 100%;
      ">
                <AIEvaluatePanel style="margin-top: 24px" @closeText="showEvaluation=false"
                                 v-if="showEvaluation" :prompt="'这是我在做的题目：'
                    + homework.description + '\n下面是我的答案：' + userInput +
            '请你根据我的答案给我总结点评，并以百分制形式给出得分，请在最后把得分用<>包裹输出，例如：得分<70>分' "/>
              </div>
            </div>
          </el-tab-pane>
          <el-tab-pane label="相似例题">
            <div>
              <h1>{{ homework.name }}</h1>
              <div>
                <el-tag effect="plain" type="info" style="margin: 12px 12px 12px 0">
                  {{ homework.startTime }} - {{ homework.endTime }}
                </el-tag>
                <el-tag v-if="homework.allowDelay" effect="plain" type="info" style="margin: 12px">
                  允许迟交
                </el-tag>
                <el-tag v-if="homework.allowRedo" effect="plain" type="info" style="margin: 12px">
                  允许重做
                </el-tag>
              </div>
              <el-text style="display: block">{{ homework.description}}</el-text>
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
                      style=" margin-top: 24px" @closeText="showEvaluation=false"
                                   v-for="item in questionNum" :prompt="'这是我在做的题目：'
                      + homework.description + questionArray.join('\n')  + '\n我希望你能帮我提出一个相似度为' + (100 - 10 * questionNum) + ' 的题目，但不要完全一样，' +
                      '并且在最后给出你所生成的题目与原题目的相似度，相似度要用<>包裹起来，例如：相似度<80>%，你不需要向我解释，单纯地给出题目并在最后加上相似度就好'"/>
                  </el-scrollbar>
                </div>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      <el-divider/>
    </template>
  </BlankPage>
</template>

<style scoped>

</style>