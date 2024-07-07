<script setup>
import {useAuth} from "@/assets/static/js/useAuth.js";

const {user} = useAuth()
import BlankPage from "@/views/BlankPage.vue";
import {onMounted, ref} from "vue";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import NoticeCard from "@/components/NoticePage/NoticeCard.vue";
import {Check, CircleCheck, Close, Promotion} from "@element-plus/icons-vue";
import {ElMessage} from "element-plus";

const notice = ref([])
const fetchNotice = () => {
  axios.get(backendUrl + user.value.role + '/message/' + user.value.ident).then(res => {
    notice.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

const deleteMessage = (id) => {
  notice.value = notice.value.filter(item => item.id !== id)
}

const showSendingMessageDialog = ref(false)

const messageForm = ref({})
const sendMessage = () => {
  if(messageForm.value.role === undefined ||
      messageForm.value.ident === undefined ||
      messageForm.value.title === undefined ||
      messageForm.value.content === undefined){
    ElMessage({
      message: '请填写完整的消息信息哦😣',
      type: 'error'
    })
    return
  }

  ElMessage({
    message: '消息发送成功✅',
    type: 'success'
  })
  showSendingMessageDialog.value = false
}

onMounted(() => {
  fetchNotice()
})
</script>

<template>
  <BlankPage>
    <template #default>
      <el-card
          shadow="hover"
      >
        <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
          <el-text
              style="
            font-weight: bold;
            font-size: 16px"
          >未读消息: {{notice.length}}条</el-text>
          <el-button
              size="small"
              type="primary"
              @click="showSendingMessageDialog=true"
              :icon="Promotion"
          >
            发送消息
          </el-button>
        </div>
        <el-divider
            style="
          margin-top: 16px; margin-bottom: 16px"
        />
        <el-scrollbar style="height: 512px">
        <n-result
            v-if="notice.length === 0"
            status="info"
            title="暂无消息"
            description="您暂时没有未读消息与通知哦😊"
        />
        <NoticeCard
            style="margin: 18px"
            v-for="message in notice" :message="message" :deleteMessage="deleteMessage"/>
        </el-scrollbar>
        <el-divider
            content-position="right"
            style="margin-top: 8px">
          <el-button
              :icon="CircleCheck"
              style="width: 128px"
              type="primary"
              size="small">
            全部已读
          </el-button>
        </el-divider>
      </el-card>
    </template>
  </BlankPage>

  <el-dialog
      title="✉️新建消息"
      style="padding: 32px"
      v-model="showSendingMessageDialog">
    <el-form label-width="auto">

      <el-divider
          style="margin-top: 32px; margin-bottom: 32px"
          content-position="left" >
        📥接收方信息
      </el-divider>

      <el-form-item label="对方身份">
        <el-select
            placeholder="请选择对方的用户身份"
            v-model="messageForm.role">
          <el-option value="teacher" label="教师"/>
          <el-option value="student" label="学生"/>
          <el-option value="parent" label="家长"/>
        </el-select>
      </el-form-item>
      <el-form-item label="学号/工号">
        <el-input v-model="messageForm.ident"
                  placeholder="请输入对方的学号/工号"/>
      </el-form-item>

      <el-divider
          style="margin-top: 32px; margin-bottom: 32px"
          content-position="left" >
        📩消息信息
      </el-divider>

      <el-form-item label="消息标题">
        <el-input
            v-model="messageForm.title"
            placeholder="请输入消息标题"
        />
      </el-form-item>
      <el-form-item label="消息内容">
        <el-input
            type="textarea"
            v-model="messageForm.content"
            placeholder="请输入消息内容"
        />
      </el-form-item>
      <el-divider
          style="margin-top: 32px; margin-bottom: 32px"
          content-position="right">
        <div style="display: flex; flex-direction: row; align-content: space-between">
          <el-button
              size="small"
              :icon="Close"
              @click="showSendingMessageDialog=false"
          >
            取消
          </el-button>
          <el-button
              size="small"
              type="success"
              :icon="Promotion"
              @click="sendMessage"
          >
            发送
          </el-button>
        </div>
      </el-divider>
    </el-form>
  </el-dialog>
</template>
<style scoped>
el-form-item{
  margin-left: 32px;
  margin-right: 32px;
}
</style>