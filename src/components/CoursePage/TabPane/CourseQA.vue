<script setup>
import AIOpinion from "@/components/utils/AIOpinion.vue";

const props = defineProps({
  qa:{
    type: Array,
    required: true
  }
})
</script>

<template>
  <div class="info-container">
    <el-divider content-position="left">
      <h1>课程问答</h1>
    </el-divider>
    <el-scrollbar :max-height="500">
      
      <div class="qa-container"
           v-for = "item in props.qa"
      >
        <el-card shadow="hover">
          <template #header>
            <el-tag class="target-tag" type="primary">
               问题
            </el-tag>
            <el-text>
              {{ item.question }}
            </el-text>
          </template>
          <AIOpinion :prompt="'请帮我回答一下这个问题' + item.question"/>
        </el-card>
      </div>
      
    </el-scrollbar>
  </div>
</template>

<style scoped>
.target-tag{
  margin-right: 8px;
}
.qa-container{
  margin: 24px;
}
</style>