<script setup lang="ts">
import {onMounted, ref} from "vue";
import {Lock, OfficeBuilding, User} from "@element-plus/icons-vue";

const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
const rescaleElement = () => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}

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
            <el-form>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="输入你的学校"
                    size="large">
                  <template #prepend>
                    <el-button :icon="OfficeBuilding" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="你的学号"
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
                    size="large"
                    show-passwor>
                  <template #prepend>
                    <el-button :icon="Lock" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请重复输入密码"
                    size="large"
                    show-passwor>
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
            <el-form>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="输入你的学校"
                    size="large">
                  <template #prepend>
                    <el-button :icon="OfficeBuilding" />
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="你的教工号"
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
                    size="large"
                    show-passwor>
                  <template #prepend>
                    <el-button :icon="Lock" />
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item>
                <el-input
                    class="registryInput"
                    placeholder="请重复输入密码"
                    size="large"
                    show-passwor>
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