<script setup>
import {onMounted, ref, reactive} from "vue";
import {Lock, UserFilled, User, School} from "@element-plus/icons-vue";
import {useAuth} from "@/assets/static/js/useAuth"
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig";
import {schools} from "@/assets/static/js/resources.js";
import {ElMessage} from "element-plus";
import {useRouter} from "vue-router";
const active = ref('student'); 
const user = useAuth()
const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
let resource = null
const {login} = useAuth()
const loginForm = reactive({
  school: '',
  id: '',
  password: ''
})
const emit = defineEmits(['handleClose','showRegister'])
const activeTab = ref('student')
const helpDialVis = ref(false)
const router = useRouter()

const validForm = () => {
  if (loginForm.school === '' || loginForm.id === '' || loginForm.password === '') {
    ElMessage({
      message: '请先把信息填写完整哦',
      type: 'warning',
      duration: 2000
    })
    return false
  }
  return true
}

const handleLogin = async () => {
  if(!validForm()) return
  const formData = new URLSearchParams();
  formData.append('request', "login");
  formData.append('school', loginForm.school);
  formData.append('id', loginForm.id); // 确保是字符串
  formData.append('password', loginForm.password);
  let loginUrl = backendUrl + activeTab.value;
  try {
    const response = await axios.post(loginUrl, formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    if (response.status === 200) {
      const userData = {
        role: activeTab.value,
        name: response.data.message,
        school: loginForm.school,
        id: loginForm.id,
      }
      ElMessage({
        message: '登录成功😊',
        type: 'success',
        duration: 2000
      })
      login(userData);
      if(activeTab.value === 'student'){
        router.push('/portal')
      }
      else if(activeTab.value === 'teacher'){
        router.push('/teaching/portal')
      }
    }
  }
  catch (error) {
    if (error.response.data.message === 'pwd'){
      ElMessage({
        message: '密码错误❌，请检查您的密码哦',
        type: 'error',
        duration: 2000
      })
    }
    else if (error.response.data.message === 'acc'){
      ElMessage({
          message: '用户不存在❌，请检查您的输入哦',
          type: 'error',
          duration: 2000
      })
    }
    else ElMessage({
      message: 'Oops，服务器开小差了~',
      type: 'error',
      duration: 2000
    })
  }
};


onMounted(() => {
  window.addEventListener('resize', () => {
    rescaleElement()
  })
})
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
                    <el-select
                        :prefix-icon="School"
                        class="loginInput"
                        placeholder="请输入或选择你的学校"
                        filterable
                        v-model="loginForm.school"
                        size="large"
                    >
                      <el-option
                          v-for="item in schools"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value"
                      />
                    </el-select>
                  </el-form-item>
                  <el-form-item>
                    <el-input
                        :prefix-icon="User"
                        class="loginInput"
                        placeholder="这里是你的学号"
                        v-model="loginForm.id"
                        size="large">
                    </el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input
                        :prefix-icon="Lock"
                        class="loginInput"
                        placeholder="还有你的密码"
                        v-model="loginForm.password"
                        size="large"
                        show-password>
                    </el-input>
                  </el-form-item>
            </el-form>
          </div>
        </el-tab-pane>

        <el-tab-pane label="教师" name="teacher">
          <div class="Center-Flex" style="margin-top: 46px">
            <el-form :model="loginForm">
              <el-form-item>
                <el-select
                    :prefix-icon="School"
                    class="loginInput"
                    placeholder="请输入或选择您所在的学校（工作单位）"
                    filterable
                    v-model="loginForm.school"
                    size="large"
                >
                  <el-option
                 p     v-for="item in schools"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                  />
                </el-select>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="User"
                    class="loginInput"
                    placeholder="请在此输入您的教工号"
                    v-model="loginForm.id"
                    size="large">
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    :prefix-icon="Lock"
                    class="loginInput"
                    placeholder="请在此输入您的密码"
                    v-model="loginForm.password"
                    size="large"
                    show-password>
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
      <el-link type="primary" style="float: right; margin-right: 24px" @click = "emit('showRegister')"> 注册账号 </el-link>
      <el-divider content-position="center" style="margin-top: 72px; margin-bottom: 72px">做有感情、有温度的教育</el-divider>
    </div>
    <div class="Center-Flex" style="margin-top: 0; margin-bottom: 32px">
      <el-text>
        如登录、注册遇到问题，请
      </el-text>
      <el-link type="primary" @click="helpDialVis = true">
        联系客服
      </el-link>
      <el-text>
        。
      </el-text>
    </div>
    <el-dialog
        title="联系客服"
        v-model="helpDialVis"
        align-center
        width="500"
    >
      <span>联络方式：tochus@163.com(电子邮箱)</span>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="helpDialVis = false">关闭</el-button>
          <el-button type="primary" @click="helpDialVis = false">
            确定
          </el-button>
        </div>
      </template>
    </el-dialog>
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
  margin: 12px;
}
</style>