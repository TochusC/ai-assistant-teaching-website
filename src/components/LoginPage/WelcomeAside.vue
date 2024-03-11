<script setup lang="ts">

import {defineEmits, onMounted, ref} from 'vue'
import RegistryDialog from "@/components/LoginPage/RegistryDialog.vue";
import LoginDialog from "@/components/LoginPage/LoginDialog.vue";

const emit = defineEmits(['openLoginDialog', 'openRegisterDialog'])

const showLoginDialog = ref(false)
const showRegistryDialog = ref(false)

const websiteTittle = ref(null)
onMounted(() => {
  setTimeout(() => {
    websiteTittle.value.style.letterSpacing = '4px'
  }, 500)
})
</script>

<template>
  <div id="function-container">
    <div>
      <div class="Center-Flex">
        <h1 ref="websiteTittle" id="tittle">
          AI赋能 | 智能教学运营平台
        </h1>
      </div>

      <el-divider style="display: block; margin-top: 24px; margin-bottom: 64px"/>

      <div class="Center-Flex">
        <h1 style="color: #101010">
          开始使用
        </h1>
      </div>

      <div class="Center-Flex" style="margin-top: 81px">
        <el-button type="primary"
                   class="login-button"
                   style="margin-right: 24px"
                   @click="showLoginDialog = true"
                   size="large">
          登录
        </el-button>
        <el-button type="primary"
                   class="login-button"
                   style="margin-left: 24px"
                   @click="showRegistryDialog = true"
                   size="large">
          注册</el-button>
      </div>

      <div class="Center-Flex" style="margin-top: 108px">
        <h3 style="color: #101010;
         margin-right: 8px">
          Powered by</h3>
        <img
            style="width: 128px; margin-right: 6px"
            src="@/assets/static/img/logo/baidu_logo.png"/>
        <img
            style="width: 36px; margin-right: 6px"
            src="@/assets/static/img/logo/vue_logo.png"/>
        <img
            style="width: 86px; margin-right: 6px"
            src="@/assets/static/img/logo/unity_logo.png"/>

      </div>
    </div>
  </div>

  <LoginDialog v-model="showLoginDialog"/>
  <RegistryDialog v-model="showRegistryDialog"/>

</template>

<style scoped>

#function-container{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 420px;
}

#tittle{
  font-size: 24px;
  display: block;
  transition: 1s;
  letter-spacing: 0px;
}

#tittle:hover{
  font-size: 26px;
  letter-spacing: 4px;
  transition: 1s;
  text-shadow: 0 0 24px #8080FF;
}

.login-button{
  padding-left: 60px;
  padding-right: 60px;
}

</style>