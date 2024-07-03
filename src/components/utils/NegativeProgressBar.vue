<script setup>
const props = defineProps({
  value: {
    type: Number,
    required: true
  },
  height: {
    type: Number,
    default: 8
  },
  attribute : {
    type: String,
    default: 'default'
  },
})
</script>

<template>
  <n-progress
      type="line"
      :percentage="value"
      :height="height"
      :status="value >= 80 ? 'danger' :
               value >= 60 ? 'warning':
               value >= 40? 'success':
               value >= 20? 'info' : 'default'"
      border-radius="12px 12px 12px 12px"
      fill-border-radius="12px 12px 12px 12px"
  >
    {{ props.attribute }}
  </n-progress>
</template>

<style scoped>

</style>