<script setup lang="ts">
import {onMounted, ref, reactive} from "vue";
import {Lock, UserFilled, User} from "@element-plus/icons-vue";
import axios from "axios";

const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)

const emit = defineEmits(['closeregister'])
// dialog中v-model绑定内容
interface registerForm{
  name:String
  id:String
  password:String
  rePassword:String
}
const registerForm = reactive <registerForm> ({
  name:'',
  id:'',
  password:'',
  rePassword:''
})

const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}

const handleRegister = async () => {
  const formData = new URLSearchParams();
  let registerUrl = '';
  if(activeTab.value === 'student'){
    registerUrl = 'http://5o2007f873.imdo.co/api/zhuce/student';
    console.log("student111")
    formData.append('Student_name', registerForm.name);
    formData.append('Student_id', registerForm.id); // 确保是字符串
    formData.append('password', registerForm.password);
    formData.append('password_verify',registerForm.rePassword)
  }else if(activeTab.value === 'teacher'){
    registerUrl = 'http://5o2007f873.imdo.co/api/zhuce/teacher';
    console.log("teacher111")

    formData.append('Teacher_name', registerForm.name);
    formData.append('Teacher_id', registerForm.id); // 确保是字符串
    formData.append('password', registerForm.password);
    formData.append('password_verify',registerForm.rePassword);
  }
  try {
    const response = await axios.post(registerUrl, formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    const resource = response.data;
    if(resource.message === '学生创建成功。'){
      emit('closeregister')
      registerForm.name = ''
      registerForm.id = ''
      registerForm.password = ''
      registerForm.rePassword = ''
    }else if(resource.message === '老师创建成功。'){
      registerForm.name = ''
      registerForm.id = ''
      registerForm.password = ''
      registerForm.rePassword = ''
      emit('closeregister')
    }
  } catch (error) {
    console.error('登录失败:', error.response ? error.response.data : error);
    // 处理错误
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
                <el-input
                    class="registryInput"
                    placeholder="输入你的名字"
                    v-model="registerForm.name"
                    size="large">
                  <template #prepend>
                    <el-button :icon="UserFilled" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="你的学号"
                    v-model="registerForm.id"
                    size="large">
                  <template #prepend>
                    <el-button :icon="User" />
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请输入密码"
                    v-model="registerForm.password"
                    size="large"
                    show-password>
                  <template #prepend>
                    <el-button :icon="Lock" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请重复输入密码"
                    v-model="registerForm.rePassword"
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
            <el-form :model="registerForm">
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="输入你的姓名"
                    v-model="registerForm.name"
                    size="large">
                  <template #prepend>
                    <el-button :icon="UserFilled" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="你的教工号"
                    v-model="registerForm.id"
                    size="large">
                  <template #prepend>
                    <el-button :icon="User" />
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请输入密码"
                    v-model="registerForm.password"
                    size="large"
                    show-password>
                  <template #prepend>
                    <el-button :icon="Lock" />
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请重复输入密码"
                    v-model="registerForm.rePassword"
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
            @click="handleRegister"
            class="registryButton"
            size="large">
          注册</el-button>
      </div>

      <el-text style="float: right">。</el-text>
      <el-link type="primary" style="float: right"> 登录 </el-link>
      <el-text style="float: right">已有账号，前往</el-text>

      <el-divider content-position="center" style="margin-top: 72px; margin-bottom: 48px">其他登录方式</el-divider>
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
.registryInput {
  width: 400px;
  margin-bottom: 16px;
}
.registryButton {
  width: 400px;
  margin-top: 16px;
  margin-bottom: 16px;
}
#registry-tab-container {
  margin: 26px;
}
</style>