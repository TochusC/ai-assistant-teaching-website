<script setup>

import {Check} from "@element-plus/icons-vue";
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
      <div style="display:flex; align-content: center">

        <el-tag type="primary" plain style="margin-right: 8px">
          <el-text
              style="
                font-size: 12px"
          >{{props.message.type}}</el-text>
        </el-tag>

        <el-text
            style="
              font-weight: bold;
              font-size: 16px"
        >{{props.message.tittle}}</el-text>
      </div>

      <div>
        <el-tag type="info" plain>
          <el-text
              style="
                font-size: 12px"
          >{{props.message.sender}}</el-text>
        </el-tag>
        <el-tag type="info" plain>
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