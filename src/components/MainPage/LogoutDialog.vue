<script setup lang="ts">
import { useAuth } from "@/assets/static/js/useAuth"
import router from "@/router/index.js";
import {onMounted} from "vue";
import * as events from "events";

const { isAuthenticated, user, logout } = useAuth()

const emit = defineEmits(['handleCancelLogout'])
const handleLogout = (event:events) => {
  logout()
  router.push('/login')
}

onMounted(() => {
  if (!isAuthenticated.value) {
    router.push('/login')
  }
})
</script>

<template>
  <el-dialog
      :show-close="false"
      title="退出登录"
      width="500"
      height="800"
      center>
    <div class="Center-Flex" style="flex-direction: column;">
        <el-text style="display: block; margin-bottom: 12px">
          当前登录用户为：{{ user.name }}
        </el-text>
        <el-text>
          你确定要退出登录吗？
        </el-text>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button
            type="danger"
            style="width: 240px"
            @click="handleLogout">
          安全退出
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<style scoped>

</style>