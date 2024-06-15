<template>
  <div id="all-container">
    <div id="propaganda-container">
      <canvas style="width: 100%; height: 100%; z-index: 1; position: absolute" ref="canvas" />
      <h1 id="slogan">
        AI Empowered ·
      </h1>
      <SloganCarousel style="z-index: 2"/>
    </div>
    <div id="login-container">
      <WelcomeAside/>
    </div>
  </div>
</template>


<script setup>


import SloganCarousel from "@/components/LoginPage/SloganCarousel.vue";
import WelcomeAside from "@/components/LoginPage/WelcomeAside.vue";
import {useAuth} from "@/assets/static/js/useAuth"
import {inject, onMounted, reactive, ref} from "vue";
import router from "@/router/index.ts";
import {Application} from "@splinetool/runtime";


// template ref
const canvas = ref(null)

// spline state
const state = reactive({
  spline: {
    scene: "https://prod.spline.design/n2atriDKoCIrXiJx/scene.splinecode",
    app: null,
    isLoaded: false,
  },
});

const { isAuthenticated, user} = useAuth();

const windowHeight = inject('windowHeight')

const initSpline =   async () =>{
  const app = new Application(canvas.value);
  await app.load(state.spline.scene)
  state.spline.app = app;
  state.spline.isLoaded = true;
  setRefresh.value = false
}

const setRefresh = ref(true);
onMounted(() => {
  initSpline();
  if(isAuthenticated.value === true){
    router.replace('/portal')
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
  position: relative;
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