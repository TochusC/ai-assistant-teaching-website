<script setup>
import HeadNavi from "@/components/utils/HeadNavi.vue";

const props = defineProps({
  maxWidth: {
    type: Number,
    default: 2048
  }
})
</script>

<template>
  <el-container >
    <el-header style="padding: 0">
      <HeadNavi/>
    </el-header>
    <el-main>
      <div class="Center-Flex">
        <div id="content" :style="{'max-width': maxWidth}">
            <el-backtop :right="100" :bottom="100" />
            <slot/>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<style scoped>
#content{
  padding: 32px;
  width: 100%;
  height: 100%;
  border: #8080FF 1px solid;
  border-radius: 8px;
  box-shadow: #8080FF 0 0 4px;
  background: var(--el-bg-color);
  min-width: 760px;
  display: flex;
  margin: 24px 128px 0px;
  flex-direction: column;
}
</style>