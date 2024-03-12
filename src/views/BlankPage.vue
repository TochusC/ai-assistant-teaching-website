<script setup lang="ts">

</script>

<template>
  <div id="blank-container">
    <slot>
    </slot>
  </div>
</template>

<style scoped>

#blank-container{
  display: flex;
  background-image: url('@/assets/static/img/background.png');
  background-size: cover;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
</style>