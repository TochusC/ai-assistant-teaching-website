<script setup>

import {reactive, ref} from "vue";
import {Lock, School, User, UserFilled} from "@element-plus/icons-vue";
import {ElMessage} from "element-plus";
import {schools} from "@/assets/static/js/resources.js";
import {Message} from "@element-plus/icons-vue/global";

const showAlterAuthenticationDialog = ref(false)
const showAlterPasswordDialog = ref(false)
const showDeleteAccountDialog = ref(false)

const altPwdForm = ref({
  newPassword: '',
  confirmPassword: ''
})

const updatePwd = () => {
  if (altPwdForm.value.newPassword !== altPwdForm.value.confirmPassword) {
    ElMessage(
        {
          message: 'Oops~两次输入的密码不一致奥😣',
          type: 'error'
        }
    )
  }
  else{
    ElMessage(
        {
          message: '密码修改成功✨',
          type: 'success'
        }
    )
    showAlterPasswordDialog.value = false
  }
}

const altAuthForm = reactive({
  school: '',
  name: '',
  id: '',
  email: '',
})
const altAuth = () => {
  if(altAuthForm.school === '' || altAuthForm.name === '' || altAuthForm.id === '' || altAuthForm.email === ''){
    ElMessage(
        {
          message: '请先把信息填写完整哦😣',
          type: 'warning'
        }
    )
    return
  }
  ElMessage(
      {
        message: '认证修改申请已提交✨',
        type: 'success'
      }
  )
  showAlterAuthenticationDialog.value = false
  pendingAltAuthRequest.value = true
}

const pendingAltAuthRequest = ref(false)


const deleteAccount = () => {
  ElMessage(
      {
        message: '账号注销申请已提交✨',
        type: 'success'
      }
  )
  showDeleteAccountDialog.value = false
  pendingDeleteAccountRequest.value = true
}
const pendingDeleteAccountRequest = ref(false)

</script>

<template>
  <el-card shadow="hover">
    <div class="Space-Between-Flex">
      <div>
        <h3 style="margin-bottom: 8px">更改密码</h3>
        <el-text>定期更改密码，设置复杂密码能保护您的账号安全</el-text>
      </div>
      <div>
        <el-button
            @click="showAlterPasswordDialog = true"
            type="primary" >更改</el-button>
      </div>
    </div>
  </el-card>

  <el-divider/>

  <el-card shadow="hover">
    <div class="Space-Between-Flex">
      <div>
        <h3 style="margin-bottom: 8px">修改认证信息</h3>
        <el-text>认证信息与您的成绩相关，请谨慎修改，修改后需等待管理员审核才可生效</el-text>
      </div>
      <div>
        <el-button
            v-if="pendingAltAuthRequest===false"
            @click="showAlterAuthenticationDialog = true"
            type="warning" >修改</el-button>
        <el-button
            v-else
            type="warning" disabled>审核中...</el-button>
      </div>
    </div>
  </el-card>

  <el-divider/>

  <el-card shadow="hover">
    <div class="Space-Between-Flex">
      <div>
        <h3 style="margin-bottom: 8px">注销账号</h3>
        <el-text>账号注销操作不可撤回，提出注销申请后，管理员将会在一段时间后清除您的账号</el-text>
      </div>
      <div>
        <el-button
            v-if="pendingDeleteAccountRequest===false"
            @click="showDeleteAccountDialog = true"
            type="danger">注销</el-button>
        <el-button
            v-else
            type="danger" disabled>审核中...</el-button>
      </div>
    </div>
  </el-card>

  <el-dialog
      title="修改密码"
      v-model="showAlterPasswordDialog">
    <el-form
        style="margin-top: 12px"
        :model="altPwdForm" label-width="auto">
      <el-form-item label="新密码" prop="newPassword">
        <el-input
            clearable
            :prefix-icon="Lock"
            v-model="altPwdForm.newPassword" show-password/>
      </el-form-item>
      <el-form-item label="确认密码" prop="confirmPassword">
        <el-input
            clearable
            :prefix-icon="Lock"
            v-model="altPwdForm.confirmPassword" show-password/>
      </el-form-item>
    </el-form>

    <template #footer>
        <el-button
            @click="showAlterPasswordDialog = false">取 消</el-button>
        <el-button
            @click="updatePwd" type="primary">确 定</el-button>
    </template>
  </el-dialog>
  <el-dialog
      title="修改认证信息"
      v-model="showAlterAuthenticationDialog">
    <el-form
        label-width="auto"
        :model="altAuthForm">
      <el-form-item
          label="学校"
          prop="school"
      >
        <el-select
            placeholder="在这里选择你的学校"
            class="registryInput"
            v-model="altAuthForm.school"
            :prefix-icon="School"
            size="large"
            filterable
        >
          <el-option
              v-for="item in schools"
              :key="item.label"
              :label="item.label"
              :value="item.label"
          />
        </el-select>
      </el-form-item>
      <el-form-item
          label="姓名"
          prop="name"
      >
        <el-input
            :prefix-icon="UserFilled"
            class="registryInput"
            v-model="altAuthForm.name"
            placeholder="在这里输入你的姓名"
            size="large">
        </el-input>
      </el-form-item>
      <el-form-item
          label="学号"
          prop="id"
      >
        <el-input
            :prefix-icon="User"
            class="registryInput"
            v-model="altAuthForm.id"
            placeholder="这里是你的学号"
            size="large">
        </el-input>
      </el-form-item>
      <el-form-item
          label="电子邮箱"
          prop="email"
      >
        <el-input
            :prefix-icon="Message"
            class="registryInput"
            v-model="altAuthForm.email"
            placeholder="别忘了填写电子邮箱"
            size="large">
        </el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button
          @click="showAlterAuthenticationDialog = false">取 消</el-button>
      <el-button
          @click="altAuth" type="primary">提交申请</el-button>
    </template>
  </el-dialog>
  <el-dialog
      title="注销账号"
      v-model="showDeleteAccountDialog">
    <el-text>你确定要
    <el-text style="color: var(--el-color-danger)">
      注销账号
    </el-text>吗？
    </el-text>
    <template #footer>
      <el-button
          @click="showDeleteAccountDialog = false">取 消</el-button>
      <el-button
          @click="deleteAccount" type="danger">注 销</el-button>
    </template> 
  </el-dialog>
</template>

<style scoped>

</style>