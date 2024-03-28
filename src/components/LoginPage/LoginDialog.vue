<script setup lang="ts">
import {onMounted, ref, reactive} from "vue";
import {Lock, UserFilled, User} from "@element-plus/icons-vue";
import {useAuth} from "@/assets/static/js/useAuth"
import axios from "axios";
import router from "@/router";

const active = ref('student'); 
const user = useAuth()
const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
let loginUrl = null
let resource = null
// dialog中v-model绑定内容
interface LoginForm{
  active:String
  name:String
  id: String
  password:String
}
const loginForm = reactive <LoginForm> ({
  active:'student',
  name:'',
  id:'',
  password:''
})
let ifLogin:boolean = false
const {login} = useAuth()
//login({name:"Guest", role:"user"})
// const handleLogin = () => {
//   const loginUrl = 'http://127.0.0.1:8000/api/yanzheng/student';
//   const formData = new URLSearchParams();
//   formData.append('Student_name', loginForm.Student_name);
//   formData.append('Student_id', loginForm.Student_id.toString()); // 确保是字符串
//   formData.append('password', loginForm.password);

//   (async () => {
//     try {
//       const response = await axios.post(loginUrl, formData, {
//         headers: {
//           'Content-Type': 'application/x-www-form-urlencoded',
//         },
//       });
//       const resource = response.data;
//       console.log(resource.message)
//       if(resource.message === '学生信息在数据表中存在。'){
//         console.log("000")
//         login({
//           name:loginForm.Student_name,
//           role:"user"
//         })
//         console.log("111")
//         ifLogin = true
//       console.log(ifLogin)
//       }
//       // 根据需要做响应处理，比如页面跳转
//        // 修改为成功登录后应该跳转的路径
//     } catch (error) {
//       console.error('登录失败:', error.response.data);
//       // 处理错误
//     }
//   })();
//   if(ifLogin){
//     router.push('/')
//   }
  
//   // 注意：这里直接跳转到根路径可能不合适，因为请求是异步的
//   // 如果登录成功后需要跳转，应该在try块内跳转，而不是在这里
// };
const handleLogin = async () => {
  const formData = new URLSearchParams();
  let loginUrl = '';
  if(activeTab.value === 'student'){
    loginUrl = 'http://127.0.0.1:8000/api/yanzheng/student';
    formData.append('Student_name', loginForm.name);
    formData.append('Student_id', loginForm.id); // 确保是字符串
    formData.append('password', loginForm.password);
  }else if(activeTab.value === 'teacher'){
     loginUrl = 'http://5o2007f873.imdo.co/api/yanzheng/teacher';
    formData.append('Teacher_name', loginForm.name);
    formData.append('Teacher_id', loginForm.id); // 确保是字符串
    formData.append('password', loginForm.password);
  }
  try {
    const response = await axios.post(loginUrl, formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    const resource = response.data;
    if(resource.message === '学生信息在数据表中存在。'){
      login({
        id: loginForm.id,
        name: loginForm.name,
        role: "student"
      })

      // 设置登录标志
      ifLogin = true
      console.log(ifLogin)
      
      // 登录成功，跳转到根路径
      router.push('/');
    }else if(resource.message === '老师信息在数据表中存在。'){
      login({
        id: loginForm.id,
        name: loginForm.name,
        role: "teacher"
      })
      // 设置登录标志
      ifLogin = true
      console.log(ifLogin)
      
      // 登录成功，跳转到根路径
      router.push('/');
    }
    console.log("login Id: ",login.id)
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

const emit = defineEmits(['handleClose','showregister'])

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
                        placeholder="输入你的姓名"
                        v-model="loginForm.name"
                        size="large">
                      <template #prepend>
                        <el-button :icon="UserFilled" />
                      </template>
                    </el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input
                        class="loginInput"
                        placeholder="你的学号"
                        v-model="loginForm.id"
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
                    placeholder="输入你的姓名"
                    v-model="loginForm.name"
                    size="large">
                  <template #prepend>
                    <el-button :icon="UserFilled" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="loginInput"
                    placeholder="你的教工号"
                    v-model="loginForm.id"
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
      <el-link type="primary" style="float: right; margin-right: 24px" @click = "emit('showregister')"> 注册账号 </el-link>
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