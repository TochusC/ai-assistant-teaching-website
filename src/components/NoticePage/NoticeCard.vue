<script setup>

import {Bell, Check} from "@element-plus/icons-vue";
import axios from "axios";
import {useAuth} from "@/assets/static/js/useAuth.js";
import {backendUrl} from "@/assets/static/js/severConfig.js";

const {user} = useAuth()

const props = defineProps({
  message: {
    type: Object,
    required: true
  },
})

const emit = defineEmits(['deleteMessage'])

const confirmMessage = () => {
  const formData = new URLSearchParams();
  axios.delete(backendUrl + user.value.role + '/message/confirm/' + props.message.id, formData).then(res => {
    console.log(res)
  }).catch(err => {
    console.log(err)
  })
  emit('deleteMessage', props.message.id)
}
</script>

<template>
  <el-card>
    <div class="Space-Between-Flex">
      <div style="display:flex; align-content: center; justify-content: center">
        <el-tag
            :type="props.message.type == '提醒'? 'warning' : props.message.type === '预警'? 'danger' : props.message.type === '通知'? 'primary' : 'success'"
            style="margin-right: 8px">
          <div style="display: flex; align-content: center">
            <el-icon style="margin-right: 2px"><Bell/></el-icon>
            {{props.message.type}}
          </div>
        </el-tag>
        <el-text
            style="
              font-weight: bold;"
        >{{props.message.tittle}}</el-text>
      </div>

      <div>
        <el-tag effect="plain" style="margin-right: 8px" type="info">
          <el-text
              style="
                font-size: 12px"
          >{{props.message.sender}}</el-text>
        </el-tag>
        <el-tag effect="plain" type="info" plain>
          <el-text
              style="
                font-size: 12px"
          >{{props.message.time}}</el-text>
        </el-tag>
      </div>
    </div>
    <el-divider
        style="
          margin-top: 16px; margin-bottom: 16px"
    />
    <div class="Space-Between-Flex">
    <el-text>{{props.message.message}}</el-text>
      <el-button @click="confirmMessage" :icon="Check" size="small" type="success">确认</el-button>
    </div>
  </el-card>
</template>

<style scoped>

</style>