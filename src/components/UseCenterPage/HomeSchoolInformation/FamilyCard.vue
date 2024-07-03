<script setup>
import {onMounted, ref} from "vue";
import {region} from "@/assets/static/js/area.js";
import {Delete, Edit, Plus, Promotion} from "@element-plus/icons-vue";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import axios from "axios";
import {useAuth} from "@/assets/static/js/useAuth.js";

const familyBtnText = ref('编辑信息')
const familyBtnType = ref('primary')
const familyBtnIcon = ref(Edit)

const isFamilyEditable = ref(false)
const handleFamilyEdit = () => {
  isFamilyEditable.value = !isFamilyEditable.value
  if (isFamilyEditable.value) {
    familyBtnText.value = '保存上传'
    familyBtnType.value = 'success'
    familyBtnIcon.value = Promotion
  } else {
    familyBtnText.value = '编辑信息'
    familyBtnType.value = 'primary'
    familyBtnIcon.value = Edit
  }
}
const {user} = useAuth()
const family = ref({ members: []})
const fetchFamily = () => {
  axios.get(backendUrl + 'student/info/family/' + user.value.ident).then(res => {
    family.value = res.data
  }).catch(err => {
    console.log(err)
  })
}

const provinceIndex = ref(0)
const fetchProvinceIndex = () => {
  for (let i = 0; i < region.length; i++) {
    if (region[i].value === family.province) {
      return i
    }
  }
  return -1
}
const cityIndex = ref(0)
const fetchCityIndex = () => {
  for (let i = 0; i < region[provinceIndex].children.length; i++) {
    if (region[provinceIndex].children[i].value === family.city) {
      return i
    }
  }
  return -1
}

const fetchAreaIndex = () => {
  for (let i = 0; i < region[provinceIndex].children[cityIndex].children.length; i++) {
    if (region[provinceIndex].children[cityIndex].children[i].value === family.area) {
      return i
    }
  }
  return -1
}

const handleAddFamilyMember = () => {
  family.value.members.push({})
}

onMounted(() => {
  fetchFamily()
})
</script>

<template>
  <el-card
      shadow="hover"
      style="margin-top: 24px"
  >
    <div class="Space-Between-Flex" style="margin-left: 12px; margin-right: 12px">
      <el-text
          style="
            font-weight: bold;
            font-size: 16px"
      >家庭信息</el-text>
      <el-button
          @click="handleFamilyEdit"
          :type="familyBtnType"
          :icon="familyBtnIcon"
          size="small">
        {{ familyBtnText }}
      </el-button>
    </div>
    <el-divider
        style="margin-top: 16px; margin-bottom: 16px"
    />
    <el-form>
      <span class="Center-Flex">
        <el-form-item label="家庭住址" style="width: 100%; margin-right: 24px">
          <el-cascader
              :disabled="!isFamilyEditable"
              v-model="family.address"
              :options="region"
              placeholder="请选择你的家庭住址"
              :props="{value: 'name', label: 'name', children: 'children'}"
              @change="fetchProvinceIndex"
          />
        </el-form-item>
        <el-form-item label="详细地址" style="width: 100%; margin-right: 24px">
          <el-input
              :disabled="!isFamilyEditable"
              v-model="family.detailAddress"
              placeholder="请输入你的详细地址"
          />
        </el-form-item>
      </span>
    </el-form>
    <el-divider content-position="left" style="margin-bottom: 32px">
      <span style="margin-right: 16px">
        家庭成员信息
      </span>
    </el-divider>
      <el-table
          v-if="family.members.length > 0"
          height="240px"
          :data="family.members" style="width: 100%">
        <el-table-column label="姓名">
          <template #default="scope">
            <el-input
                :disabled="!isFamilyEditable"
                v-model="family.members[scope.$index].name"
                placeholder="在这里输入成员姓名奥"
            />
          </template>
        </el-table-column>
        <el-table-column label="关系">
          <template #default="scope">
            <el-input
                :disabled="!isFamilyEditable"
                v-model="family.members[scope.$index].relationship"
                placeholder="输入你与成员的关系~"
            />
          </template>
        </el-table-column>

        <el-table-column prop="address" label="联系方式" >
          <template #default="scope">
            <el-input
                :disabled="!isFamilyEditable"
                v-model="family.members[scope.$index].phone"
                placeholder="（他/她/它）的联系方式"
            />
          </template>
        </el-table-column>

        <el-table-column prop="address" label="操作" width="100">
          <template #default="scope">
            <el-button
                :disabled="!isFamilyEditable"
                size="small"
                type="danger"
                :icon="Delete"
                @click="family.members.splice(scope.$index, 1)">
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    <n-result
        v-else
        status="info"
        title="暂无家庭成员信息"
        description="同学，请添加你的家庭成员信息哦😊"
    >
    </n-result>
    <el-divider content-position="right">
      <el-button
          :disabled="!isFamilyEditable"
          size="small" type="primary"
          :icon="Plus" @click="handleAddFamilyMember">
        新增家庭成员
      </el-button>
    </el-divider>
  </el-card>
</template>

<style scoped>

</style>