<script setup lang="ts">

</script>

<template>
  <el-drawer
      title="问题"
      size="36%"
      >
    <el-form>
      <el-form-item label="问题">
        <el-input></el-input>
      </el-form-item>
      <el-form-item label="小慧回答（精调AI）">
        <el-input></el-input>
      </el-form-item>
      <el-form-item label="问题回答">
        <el-input></el-input>
      </el-form-item>
      <el-form-item label="我来回答">
        <el-input type="textarea"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary">提交</el-button>
      </el-form-item>
    </el-form>
  </el-drawer>

</template>

<style scoped>

</style>