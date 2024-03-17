<script setup lang="ts">
import {onMounted, ref, reactive} from "vue";
import {Lock, OfficeBuilding, User} from "@element-plus/icons-vue";
import {useAuth} from "@/assets/static/js/useAuth"
import router from "@/router";

const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
// dialog中v-model绑定内容
interface LoginForm{
  university:String
  userName:String
  password:String
}
const loginForm = reactive <LoginForm> ({
  university:'',
  userName:'',
  password:''
})

const {login} = useAuth()
const handleLogin = () => {
  login({name:"Guest", role:"user"})
  router.push('/')
}

onMounted(() => {
  window.addEventListener('resize', () => {
    rescaleElement()
  })
})

const emit = defineEmits(['handleClose'])

const activeTab = ref('student')
</script>

<template>
  <el-dialog
      align-center
      width="500"
      :before-close="emit('handleClose')"
  >
    <div id="login-tab-container">
      <el-tabs v-model="activeTab" style="margin-top: 72px">
        <el-tab-pane label="学生" name="student">
          <div class="Center-Flex" style="margin-top: 46px">
            <el-form :model="loginForm">
                  <el-form-item>
                    <el-input
                        class="loginInput"
                        placeholder="输入你的学校"
                        v-model="loginForm.university"
                        size="large">
                      <template #prepend>
                        <el-button :icon="OfficeBuilding" />
                      </template>
                    </el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input
                        class="loginInput"
                        placeholder="你的学号"
                        v-model="loginForm.userName"
                        size="large">
                      <template #prepend>
                        <el-button :icon="User" />
                      </template>
                    </el-input>
                  </el-form-item>

                  <el-form-item>
                    <el-input
                        class="loginInput"
                        placeholder="请输入密码"
                        v-model="loginForm.password"
                        size="large"
                        show-password>
                      <template #prepend>
                        <el-button :icon="Lock" />
                      </template>
                    </el-input>
                  </el-form-item>
            </el-form>
          </div>
        </el-tab-pane>

        <el-tab-pane label="教师" name="teacher">
          <div class="Center-Flex" style="margin-top: 46px">
            <el-form :model="loginForm">
              <el-form-item>
                <el-input
                    class="loginInput"
                    placeholder="输入你的学校"
                    v-model="loginForm.university"
                    size="large">
                  <template #prepend>
                    <el-button :icon="OfficeBuilding" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="loginInput"
                    placeholder="你的教工号"
                    v-model="loginForm.userName"
                    size="large">
                  <template #prepend>
                    <el-button :icon="User" />
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    class="loginInput"
                    placeholder="请输入密码"
                    v-model="loginForm.password"
                    size="large"
                    show-password>
                  <template #prepend>
                    <el-button :icon="Lock" />
                  </template>
                </el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-tab-pane>
      </el-tabs>

      <div class="Center-Flex">
        <el-button
            type="primary"
            class="loginButton"
            @click="handleLogin"
            size="large">
          登录</el-button>
      </div>

      <el-link type="primary" style="float: right; margin-right: 16px"> 忘记密码 </el-link>
      <el-link type="primary" style="float: right; margin-right: 24px"> 注册账号 </el-link>
      <el-divider content-position="center" style="margin-top: 72px; margin-bottom: 48px">其他登录方式</el-divider>

      <div class="Center-Flex">
        <img
            style="width: 56px; margin-right: 64px"
            src="@/assets/static/img/logo/qq_icon.png">
        <img
            style="width: 56px; margin-right: 64px"
            src="@/assets/static/img/logo/wechat_icon.png">
        <img
            style="width: 50px; margin-right: 16px"
            src="@/assets/static/img/logo/github_icon.png">
      </div>
    </div>

    <div class="Center-Flex" style="margin-top: 96px; margin-bottom: 32px">
      <el-text>
        如登录、注册遇到问题，请
      </el-text>
      <el-link type="primary">
        联系客服
      </el-link>
      <el-text>
        。
      </el-text>
    </div>
  </el-dialog>
</template>

<style scoped>
.loginInput {
  width: 400px;
  margin-bottom: 16px;
}
.loginButton {
  width: 400px;
  margin-top: 16px;
  margin-bottom: 18px;
}
#login-tab-container {
  margin: 26px;
}
</style>