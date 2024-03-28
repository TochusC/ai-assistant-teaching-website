<template>
  <div id="all-container">
    <div id="propaganda-container">
      <h1 id="slogan">
        AI Empowered ·
      </h1>
      <SloganCarousel/>
    </div>
    <div id="login-container">
      <WelcomeAside/>
    </div>
  </div>
</template>


<script setup lang="ts">


import SloganCarousel from "@/components/LoginPage/SloganCarousel.vue";
import WelcomeAside from "@/components/LoginPage/WelcomeAside.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {inject, onMounted} from "vue";
import router from "@/router";

const { isAuthenticated} = useAuth();

const windowHeight = inject('windowHeight')

onMounted(() => {
  if(isAuthenticated.value == true){
    router.replace('/')
  }
})
</script>

<style scoped>
#all-container{
  display: flex;
  height: 100%;
  width: 100%;
}
#propaganda-container{
  flex: 4;
  height: 100%;
  width: 100%;
  background-image: url('@/assets/static/img/background.png');
  background-size: cover;
}
#login-container{
  flex: 1;
  box-shadow: inset 0 0 16px #8080FF;
  height: 100%;
  width: 100%;
  background: var(--el-bg-color);
}

#slogan{
  margin: 36px;
  font-weight: bold;
  color: #8080FF;
}

</style>