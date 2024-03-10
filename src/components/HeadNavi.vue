<template>
  <el-menu
      :default-active="activeIndex"
      mode="horizontal"
  >
    <el-container>
      <el-popover
          placement="top-start"
          :width="200"
          trigger="hover"
      >
        <template #reference>
          <img
              class="icon"
              src="../../assets/static/img/turbine_icon.png" alt="" style="height:64px; width: auto"/>
        </template>
        <span>守得云开见月明</span>
        <span>
        <el-switch
            v-model="isDark"
            @change="$emit('changeTheme', isDark)"
            style="margin-left: 22px"
            inline-prompt
            :active-icon="MoonNight"
            :inactive-icon="Sunset"
        /></span>
      </el-popover>
      <el-container
          style="margin-left: 8px"
          v-if="!isCollapse"
      >
        <p
            class="proverb"
            ref="proverb"
        >云龙相得起，风电一时来。</p>
      </el-container>
    </el-container>
    <el-menu-item index="1" @click="$emit('changePage', '1')">预测系统</el-menu-item>
    <el-menu-item index="2" @click="$emit('changePage', '2')">使用指南</el-menu-item>
    <el-menu-item
        index="3"
        style="
        color: #5968f4;
        font-size: 16px;
        text-shadow: #fff 0 0 16px"
        @mouseenter="dynamicClass = 'is-loading'"
        @mouseleave="dynamicClass = ''"
        @click="$emit('changePage', '3')"
    >
      AI
      <el-icon
          :class="dynamicClass"
          size="14px"
      >
        <Star
            color="#5968f4"/>
      </el-icon>
    </el-menu-item>
    <el-menu-item index="4" @click="$emit('changePage', '4')">关于我们</el-menu-item>
  </el-menu>
</template>

<script setup>
import { ref, onMounted ,defineEmits } from 'vue'
const activeIndex = ref('1')
import { useDark } from '@vueuse/core'
import {MoonNight, Star, Sunset} from "@element-plus/icons-vue";

const proverb = ref(null)
const isDark = useDark()
const isCollapse = ref(true)
const dynamicClass = ref('')
const emits = defineEmits(['changePage', 'changeTheme'])

onMounted(() => {
  if(isDark.value) {
    isDark.value = false
  }
  if (window.innerWidth < 620) {
    if(proverb.value){
      proverb.value.style.fontSize = '0px'
    }
  }
  else {
    if(proverb.value) {
      proverb.value.style.fontSize = '18px'
    }
    isCollapse.value = false
  }
  emits('changeTheme', isDark.value)
  window.addEventListener('resize', () => {
    if (window.innerWidth < 620) {
      if(proverb.value){
        proverb.value.style.fontSize = '0px'
      }
    }
    else {
      if(proverb.value) {
        proverb.value.style.fontSize = '18px'
      }
      isCollapse.value = false
    }
  })
})

</script>

<style scoped>
p.proverb{
  text-align: center;
  font-size: 18px;
  text-shadow: 0 0 4px #fff;
  transition: all ease 0.3s;
}
p.proverb:hover{
  text-align: center;
  text-shadow: 0 0 12px #fff;
  transition: all ease 0.3s;
}

</style>