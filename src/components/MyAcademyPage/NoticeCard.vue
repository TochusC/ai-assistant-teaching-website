<script setup>
import {Notebook } from "@element-plus/icons-vue";
import {onMounted, ref} from "vue";
import router from "@/router";

const props = defineProps(
    {
      notice:{
        data:Object,
        required:true,
      }
    }
)

const tagType = ref("primary")
const tagTextClass = ref('primary-text')

onMounted(()=>{
  if(props.notice){
    if(props.notice.type === "简答")
    {
      tagType.value = "primary"
      tagTextClass.value = "primary-text"
    }
    else if(props.notice.type === "考勤"){
      tagType.value = "success"
      tagTextClass.value = "success-text"
    }
    else{
      tagType.value = "warning"
      tagTextClass.value = "warning-text"
    }
  }
})

const handleCheckout = () => {
  if(props.notice.type === "简答"){
    router.push('/academy/homework/' + props.notice.id)
  }
  else if(props.notice.type === "考勤"){
    router.push('/academy/attendance/' + props.notice.id)
  }
  else{
    router.push('/academy/course/' + props.notice.id)
  }
}

</script>

<template>
  <el-card
      id = "info-card"
      shadow="never"
  >
  <template #header>
    <div class="Space-Between-Flex">
      <el-tag :type="tagType">
        <el-text ref="tagText" :class="tagTextClass">
          <el-icon><Notebook /></el-icon>
          {{ props.notice.type }}
        </el-text>
      </el-tag>
      <el-button
          type="primary"
          size="small"
          @click="handleCheckout"
      >查看</el-button>
    </div>
  </template>
    <el-text>
      {{ props.notice.course }}
    </el-text>
    <p style="margin-top: 4px">
      {{ props.notice.tittle }}
    </p>
    <el-tag effect="plain" type="info" style="margin-top: 12px">
      {{ props.notice.startTime }} - {{ props.notice.endTime }}
    </el-tag>

  </el-card>
</template>

<style scoped>
.primary-text{
  color: var(--el-color-primary);
}
.success-text{
  color: var(--el-color-success);
}
.warning-text{
  color: var(--el-color-warning);
}

#info-card{
  min-width: 256px;
  margin: 12px;
  transition: 0.2s;
  box-shadow: 0 0 1px #1a1a1a;
}

#info-card:hover{
  transition: 0.2s;
  box-shadow: 0 0 4px #1a1a1a;
}

* {
  white-space: nowrap;
}
</style>