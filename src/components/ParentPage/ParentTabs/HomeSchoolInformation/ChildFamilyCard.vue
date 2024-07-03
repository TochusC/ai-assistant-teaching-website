<script setup>
import {onMounted, ref} from "vue";
import {region} from "@/assets/static/js/area.js";
import axios from "axios";
import {backendUrl} from "@/assets/static/js/severConfig.js";
import {useAuth} from "@/assets/static/js/useAuth.js";

const {user} = useAuth()
const sid = user.value.ident

const family = ref({ members: []})
const fetchFamily = () => {
  axios.get(backendUrl + 'student/info/family/' + sid).then(res => {
    family.value = res.data
  }).catch(err => {
    console.log(err)
  })
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
    </div>
    <el-divider
        style="margin-top: 16px; margin-bottom: 16px"
    />
    <el-form style="margin-left: 24px; margin-right: 24px">
      <span class="Center-Flex">
        <el-form-item label="家庭住址" style="width: 100%; margin-right: 24px">
          <el-cascader
              disabled
              v-model="family.address"
              :options="region"
              placeholder="您的孩子尚未选择家庭住址"
              :props="{value: 'name', label: 'name', children: 'children'}"
          />
        </el-form-item>
        <el-form-item label="详细地址" style="width: 100%; margin-right: 24px">
          <el-input
              disabled
              v-model="family.detailAddress"
              placeholder="您的孩子尚未输入详细地址"
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
              disabled
              v-model="family.members[scope.$index].name"
              placeholder="您的孩子尚未输入成员姓名"
          />
        </template>
      </el-table-column>
      <el-table-column label="关系">
        <template #default="scope">
          <el-input
              disabled
              v-model="family.members[scope.$index].relationship"
              placeholder="该孩子与成员的关系~"
          />
        </template>
      </el-table-column>

      <el-table-column prop="address" label="联系方式" >
        <template #default="scope">
          <el-input
              disabled
              v-model="family.members[scope.$index].phone"
              placeholder="（他/她/它）的联系方式"
          />
        </template>
      </el-table-column>
    </el-table>
    <n-result
        v-else
        status="info"
        title="暂无家庭成员信息"
        description="您的孩子暂未添加家庭成员信息"
    >
    </n-result>
    <el-divider content-position="right"/>
  </el-card>
</template>

<style scoped>

</style>