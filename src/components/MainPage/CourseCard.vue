<script setup lang="ts">

const props = defineProps({
  brief: {
    type: Object,
    required: true
  },
})

</script>

<template>
  <el-card shadow="hover" id="course-card" style="width: 240px;">
    <img
        style="width: 196px"
        :src="props.brief.image"
        class="image"
        alt="计算机网络原理"
    />
    <div id="info-container">
      <el-text style="display: block">
        {{props.brief.name}}
      </el-text>
      <el-text truncated>
        {{ props.brief.description }}
      </el-text>
    </div>
  </el-card>
</template>

<style scoped>
#course-card{
  cursor: pointer;
  margin-right: 36px;
}
#info-container{
  padding: 8px;
  width: 210px;
  padding-bottom: 0;
}
</style>