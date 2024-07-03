<script setup>

import {onMounted, ref} from "vue";
import {useAuth} from "@/assets/static/js/useAuth";
import {Edit, Promotion} from "@element-plus/icons-vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";

const {user} = useAuth()

const infoBtnText = ref('编辑信息')
const infoBtnType = ref('primary')
const infoBtnIcon = ref(Edit)

const isInfoEditable = ref(false)
const handleInfoEdit = () => {
  isInfoEditable.value = !isInfoEditable.value
  if(isInfoEditable.value){
    infoBtnText.value = '保存上传'
    infoBtnType.value = 'success'
    infoBtnIcon.value = Promotion
  }
  else{
    infoBtnText.value = '编辑信息'
    infoBtnType.value = 'primary'
    infoBtnIcon.value = Edit
  }
}

const basicInfo = ref({})
const fetchBasicInfo = () => {
  axios.get(backendUrl + 'student/info/basic/' + user.value.ident).then(res => {
    basicInfo.value = res.data
  }).catch(err => {
  console.log(err)
  })
}

const avatar = ref(null)
const refreshAvatar = () => {
  window.location.reload()
}

onMounted(() => {
  fetchBasicInfo()
})

const file = ref(null)
const upload = ref();
const disabled = ref(false)
const handleExceed = (files)=>{
  upload.value?.clearFiles()
  file.value = files[0]
  upload.value?.handleStart(file)
  upload.value?.submit()
  refreshAvatar()
}
</script>

<template>
  <div class="Space-Between-Flex">
    <div style="
          display:flex;
          align-content: center;
          justify-content: center;
          flex-direction: column; max-width: 300px">
      <div class="Center-Flex"
           style="flex-direction: column; ">
        <el-popover
            trigger="hover"
            placement="top"
            width="240px"
            title="感谢你的陪伴"
        >
          <template #default>
            你于{{user.enrollment}}加入了通慧智教的大家庭🏠
          </template>
          <template #reference>
            <el-tag type="primary" style="margin-bottom: 24px">
              {{user.enrollment}}
            </el-tag>
          </template>
        </el-popover>
        <el-image
            alt="用户头像"
            ref="avatar"
            style="width: 150px; height: 150px; border-radius: 150px"
            :src = 'basicInfo.avatar'
            id = "custom-image"/>
        <el-upload
            :limit="1"
            ref="upload"
            name="avatar"
            :action=
                "backendUrl +
                 'student/info/basic/avatar/'
                 + user.ident"
            :on-exceed="handleExceed"
            :auto-upload="true"
            :on-success="refreshAvatar"
        >
          <el-button type="primary"
                     style="
                       width: 164px;
                       margin-top: 24px;
                       margin-left: 48px;
                       margin-right: 48px">
            更换头像</el-button>
        </el-upload>
      </div>
    </div>
    <el-card style="width: 100%;" shadow="hover">

      <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
        <el-text
            style="
                font-weight: bold;
                font-size: 16px"
        >基本信息</el-text>
        <el-button
            :icon="infoBtnIcon"
            @click="handleInfoEdit"
            ref="infoBtn"
            :type="infoBtnType"
            size="small">
          {{infoBtnText}}
        </el-button>
      </div>
      <el-divider
          style="
              margin-top: 16px; margin-bottom: 16px"
      />
      <el-form label-width="auto">
        <el-form-item label="姓名">
          <el-popover
              title="不可更改❌"
              trigger="hover"
              width="320px"
              placement="right"
              content="姓名一经注册，就不可再变了哦😣"
          >
            <template #reference>
              <el-input disabled placeholder="尚未设置姓名" v-model="user.name"/>
            </template>
          </el-popover>
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group :disabled="!isInfoEditable" v-model="basicInfo.gender" >
            <el-radio value="男">男</el-radio>
            <el-radio value="女">女</el-radio>
            <el-radio value="保密">保密</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="生日">
            <el-date-picker
                :disabled="!isInfoEditable"
                v-model="basicInfo.birthday"
                type="date"
                placeholder="我们到时会庆祝你的生日🎉"
                style="width: 100%"
            />
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input
              :disabled="!isInfoEditable"
              placeholder="尚未绑定邮箱"
              v-model="user.email"
          />
        </el-form-item>
        <el-form-item label="手机号">
          <el-input
              :disabled="!isInfoEditable"
              placeholder="尚未绑定手机号"
              v-model="basicInfo.phone"
          />
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>

</style>