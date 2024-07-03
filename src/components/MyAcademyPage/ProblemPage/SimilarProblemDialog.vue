<script setup>
import {CircleClose, Delete, Promotion, StarFilled} from "@element-plus/icons-vue";
import AIEvaluatePanel from "@/components/utils/AIEvaluatePanel.vue";
import AITextLong from "@/components/utils/AITextLong.vue";
import {ref, defineProps} from "vue";

const emit = defineEmits(['closeDial'])
const props = defineProps(['question'])
const userInput = ref("")
const showPrompt = ref(false)
const showPromptByInput = ref(false)
const showEvaluation = ref(false)

</script>
<template>
  <el-dialog>
    <h1 style="margin-bottom: 12px; margin-left: 8px">相似例题</h1>
    <el-text
        style="
        display: block;
        margin-left: 24px;
        margin-right: 24px;
"
    >{{ question }}</el-text>
    <el-divider content-position="left">智能解析</el-divider>
    <div class="Center-Flex">
      <el-button
          @click="showPrompt = !showPrompt"
          type="primary" style="margin-top: 8px"
          v-if="!showPrompt">点击让小慧给点建议吧？</el-button>
      <AITextLong v-else style="margin-top: 24px; width: 100%; margin-left: 24px; margin-right: 24px"
                  :prompt="'请用简要的一句话提示下我应该如何完成这个作业：' + props.question"/>
    </div>
    <el-divider/>
    <div class="Center-Flex">
      <el-input
          style="margin-left: 24px; margin-right: 24px"
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
                  margin-top:24px;

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
      <el-button
          style="margin-right: 24px"
          type="success"
          :icon="Promotion"
          @click="showEvaluation.value = true">
        提交
      </el-button>
    </div>
    <AITextLong
        @closeText="showPromptByInput=false"
        style="margin-top: 24px; margin-left: 24px; margin-right: 24px"
        v-if="showPromptByInput"
        :prompt="'这是我在做的题目：' + props.question + '\n下面是我的答案：' + userInput + '\n请你根据我的答案给我点提示。' "/>
    <div style="
        width: 100%;
      ">
      <AIEvaluatePanel style="margin-top: 24px"
                       @closeText="showEvaluation=false"
                       v-if="showEvaluation"
                       :prompt="'这是我在做的题目：'+ question +
                       '\n下面是我的答案：' + userInput +
                       '请你根据我的答案给我总结点评，并以百分制形式给出得分，请在最后把得分用<>包裹输出，例如：得分<70>分' "/>
    </div>

    <template #footer>
      <div class="dialog-footer">
        <el-button
            style="
            margin-right: 24px;
            margin-bottom: 16px;
            margin-top: 6px"
            type="primary"
            :icon="CircleClose"
            @click="emit('closeDial')">关闭</el-button>
      </div>
    </template>
  </el-dialog>
</template>

<style scoped>

</style>