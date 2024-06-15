<script setup>
import {onMounted, ref, reactive} from "vue";
import {Lock, UserFilled, User, School} from "@element-plus/icons-vue";
import axios from "axios";
import {schools} from "@/assets/static/js/resources.js";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import {ElMessage} from "element-plus";
import {Message} from "@element-plus/icons-vue/global";

const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)

const emit = defineEmits(['showLogin'])
// dialog中v-model绑定内容
const helpDialVis = ref(false)
const registerForm = reactive({
  school: '',
  name: '',
  id: '',
  email: '',
  password: ''
})

const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}

const validForm = () => {
  if (registerForm.school === '' || registerForm.name === '' || registerForm.id === '' || registerForm.email === '' || registerForm.password === '') {
    ElMessage({
      message: '请先把信息填写完整哦',
      type: 'warning',
      duration: 2000
    })
    return false
  }
  if(registerForm.password !== registerForm.rePassword){
    ELMessage({
      message: 'Oops，两次输入的密码不一致哦。',
      type: 'error',
      duration: 2000
    })
    return false
  }
  return true
}

const handleRegister = async () => {
  if(!validForm()) return;
  const formData = new URLSearchParams();
  formData.append('request', "register");
  formData.append('name', registerForm.name);
  formData.append('id', registerForm.id); // 确保是字符串
  formData.append('school', registerForm.school);
  formData.append('password', registerForm.password);
  formData.append('email', registerForm.email);
  let registerUrl = backendUrl + activeTab.value;
  try {
    const response = await axios.post(registerUrl, formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    if(response.status === 201){
      ElMessage({
        message: '账号注册成功😊，欢迎加入通慧智教的大家庭，快去登录吧？',
        type: 'success',
        duration: 2000
      })
      emit('showLogin');
    }
    else{
      ElMessage({
        message: '注册失败❌，请检查您的输入哦',
        type: 'error',
        duration: 2000
      })
    }
  } catch (error) {
    if(error.response.status === 405){
      ElMessage({
        message: '该账号已经注册过了❌，请前往登录😣。',
        type: 'error',
        duration: 2000
      })
    }
    else{
      ElMessage({
        message: 'Oops，服务器开小差了~',
        type: 'error',
        duration: 2000
      })
    }
  }
};

onMounted(() => {
  window.addEventListener('resize', () => {
    rescaleElement()
  })
})

const activeTab = ref('student')
</script>

<template>
  <el-dialog
      align-center
      width="500"
  >
    <div id="registry-tab-container">
      <el-tabs v-model="activeTab" style="margin-top: 72px">
        <el-tab-pane label="学生" name="student">
          <div class="Center-Flex" style="margin-top: 46px">
            <el-form :model="registerForm">
              <el-form-item>
                <el-select
                    placeholder="在这里输入你的学校"
                    class="registryInput"
                    v-model="registerForm.school"
                    :prefix-icon="School"
                    size="large"
                    filterable
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
                    :prefix-icon="UserFilled"
                    class="registryInput"
                    v-model="registerForm.name"
                    placeholder="在这里输入你的姓名"
                    size="large">
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="User"
                    class="registryInput"
                    v-model="registerForm.id"
                    placeholder="这里是你的学号"
                    size="large">
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Lock"
                    class="registryInput"
                    v-model="registerForm.password"
                    placeholder="还有你的密码"
                    size="large"
                    show-password>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Lock"
                    class="registryInput"
                    v-model="registerForm.rePassword"
                    placeholder="请重复输入密码"
                    size="large"
                    show-password>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Message"
                    class="registryInput"
                    v-model="registerForm.email"
                    placeholder="别忘了填写电子邮箱"
                    size="large">
                </el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-tab-pane>

        <el-tab-pane label="教师" name="teacher">
          <div class="Center-Flex" style="margin-top: 46px">
            <el-form :model="registerForm">
              <el-form-item>
                <el-select
                    placeholder="请输入或选择您所在的学校（工作单位）"
                    class="registryInput"
                    v-model="registerForm.school"
                    :prefix-icon="School"
                    size="large"
                    filterable
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
                    :prefix-icon="UserFilled"
                    class="registryInput"
                    v-model="registerForm.name"
                    placeholder="请输入您的姓名"
                    size="large">
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    :prefix-icon="User"
                    class="registryInput"
                    v-model="registerForm.id"
                    placeholder="请在此输入您的教工号"
                    size="large">
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Lock"
                    class="registryInput"
                    v-model="registerForm.password"
                    placeholder="请在此输入您的密码"
                    size="large"
                    show-password>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Lock"
                    class="registryInput"
                    v-model="registerForm.rePassword"
                    placeholder="请重复输入您的密码"
                    size="large"
                    show-password>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    :prefix-icon="Message"
                    class="registryInput"
                    v-model="registerForm.email"
                    placeholder="请输入您的电子邮箱"
                    size="large">
                </el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-tab-pane>
      </el-tabs>


      <div class="Center-Flex">
        <el-button
            type="primary"
            @click="handleRegister"
            class="registryButton"
            size="large">
          注册</el-button>
      </div>

      <el-text style="float: right">。</el-text>
      <el-link type="primary" style="float: right" @click="emit('showLogin')"> 登录 </el-link>
      <el-text style="float: right">已有账号，前往</el-text>

      <el-divider content-position="center" style="margin-top: 64px; margin-bottom: 48px">做有感情、有温度的教育</el-divider>
    </div>

    <div class="Center-Flex" style="margin-top: 36px; margin-bottom: 32px">
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
.registryInput {
  width: 400px;
  margin-bottom: 16px;
}
.registryButton {
  width: 400px;
  margin-bottom: 16px;
}
#registry-tab-container {
  margin: 12px;
}
</style>