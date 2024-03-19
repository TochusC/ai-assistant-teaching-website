<script setup lang="ts">
import {useRoute} from "vue-router";
import {UploadFilled} from "@element-plus/icons-vue";
import BlankPage from "@/views/BlankPage.vue";
import {ref} from "vue";

const route = useRoute()

const homeworkId = route.params.id

const homework = {
  id: 1,
  name: "第一次课堂作业",
  description: "本次作业要求学生完成一个简单的网页设计，要求使用HTML和CSS完成。",
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
</script>

<template>
  <BlankPage>
    <template #default>
        <el-tabs type="border-card">
          <el-tab-pane label="作业详情">
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
            </div>
          </el-tab-pane>
          <el-tab-pane label="作业提交">

            <div style="margin:12px;">
              <div style="width: 100%; margin-bottom: 24px">
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
              <el-upload
                  class="upload-demo"
                  drag
                  action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                  multiple
              >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                  拖动文件或 <em>点击上传</em>
                </div>
                <template #tip>
                  <div style="margin: 8px">
                    <el-button type="primary" style="margin-right: 16px">点击上传</el-button>
                    <el-text type="primary">
                      只能上传jpg/png文件，且不超过500kb
                    </el-text>
                  </div>
                </template>
              </el-upload>
            </div>
          </el-tab-pane>
        </el-tabs>
    </template>
  </BlankPage>

</template>

<style scoped>

</style>