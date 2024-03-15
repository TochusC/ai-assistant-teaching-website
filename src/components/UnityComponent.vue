<script setup>

import {onMounted, ref} from "vue";
import router from "@/router";
import {useAuth} from "@/assets/static/js/useAuth.js";
const { isAuthenticated, login, logout } = useAuth();

const props = defineProps({
  initialUnityCanvasHeight: {
    type: Number,
    required: true
  },
  initialUnityCanvasWidth: {
    type: Number,
    required: true
  }
})

const unityCanvasHeight = ref(props.initialUnityCanvasHeight);
const unityCanvasWidth = ref(props.initialUnityCanvasWidth);

function unityShowBanner(msg, type) {
  function updateBannerVisibility() {
    warningBanner.style.display = warningBanner.children.length ? 'block' : 'none';
  }
  var div = document.createElement('div');
  div.innerHTML = msg;
  warningBanner.appendChild(div);
  if (type == 'error') div.style = 'background: red; padding: 10px;';
  else {
    if (type == 'warning') div.style = 'background: yellow; padding: 10px;';
    setTimeout(function() {
      warningBanner.removeChild(div);
      updateBannerVisibility();
    }, 5000);
  }
  updateBannerVisibility();
}

function initRecord(opt = {}) {
  let defaultOpt = {
    serviceCode: "asr_aword",
    audioFormat: "wav",
    sampleRate: 16000,
    sampleBit: 16,
    audioChannels: 1,
    bitRate: 96000,
    audioData: null,
    punctuation: "true",
    model: null,
    intermediateResult: null,
    maxStartSilence: null,
    maxEndSilence: null,
  };

  let options = Object.assign({}, defaultOpt, opt);

  let sampleRate = options.sampleRate || 8000;
  let bitRate = parseInt(options.bitRate / 1000) || 16;
  if (RecorderIns) {
    RecorderIns.close();
  }

  RecorderIns = Recorder({
    type: "wav",
    sampleRate: sampleRate,
    bitRate: bitRate,
    onProcess(buffers, powerLevel, bufferDuration, bufferSampleRate) {
      // 60秒时长限制
      const LEN = 59 * 1000;
      if (bufferDuration > LEN) {
        RecorderIns.recStop();
      }
    },
  });
  RecorderIns.open(
      () => {
        // 打开麦克风授权获得相关资源
        console.log("打开麦克风成功");
      },
      (msg, isUserNotAllow) => {
        // 用户拒绝未授权或不支持
        console.log((isUserNotAllow ? "UserNotAllow，" : "") + "无法录音:" + msg);
      }
  );
}

var container = null
var canvas = null
var loadingBar = null
var progressBarFull = null
var fullscreenButton = null
var warningBanner = null

var buildUrl = "/src/assets/static/Unity/Build";
var loaderUrl = buildUrl + "/WebGL_Build.loader.js";
var config = {
  dataUrl: buildUrl + "/WebGL_Build.data.br",
  frameworkUrl: buildUrl + "/WebGL_Build.framework.js.br",
  codeUrl: buildUrl + "/WebGL_Build.wasm.br",
  streamingAssetsUrl: "StreamingAssets",
  companyName: "DefaultCompany",
  productName: "AI-Asssistant(WebGL)",
  productVersion: "0.1.0",
  showBanner: unityShowBanner,
};
var script = null;

// Shows a temporary message banner/ribbon for a few seconds, or
// a permanent error message on top of the canvas if type=='error'.
// If type=='warning', a yellow highlight color is used.
// Modify or remove this function to customize the visually presented
// way that non-critical warnings and error messages are presented to the
// user.


// By default, Unity keeps WebGL canvas render target size matched with
// the DOM size of the canvas element (scaled by window.devicePixelRatio)
// Set this to false if you want to decouple this synchronization from
// happening inside the engine, and you would instead like to size up
// the canvas DOM size and WebGL render target sizes yourself.
// config.matchWebGLToCanvasSize = false;

onMounted(() =>{

  window.handleUnityTransmission = function(str) {
    var currentRoute = router.path;
    if(str === "打开注册表单" || str === "打开登录表单" || str === "退出登录"){
      if(currentRoute !== '/login'){
        logout();
      }

      if (str === "打开注册表单") {
        router.push({path: '/login', query: {form: 'register'}})
      }
      else if (str === "打开登录表单") {
        router.push({path: '/login', query: {form: 'login'}})
      }
      else{
        router.push({path: '/login'})
      }
    }
    if(str === "打开课程：计算机网络原理"){
      router.push({path: '/course/1'})
    }
  }

  container = document.querySelector("#unity-container");
  canvas = document.querySelector("#unity-canvas");
  loadingBar = document.querySelector("#unity-loading-bar");
  progressBarFull = document.querySelector("#unity-progress-bar-full");
  fullscreenButton = document.querySelector("#unity-fullscreen-button");
  warningBanner = document.querySelector("#unity-warning");

  loadingBar.style.display = "block";

  if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
    // Mobile device style: fill the whole browser client area with the game canvas:

    var meta = document.createElement('meta');
    meta.name = 'viewport';
    meta.content = 'width=device-width, height=device-height, initial-scale=1.0, user-scalable=no, shrink-to-fit=yes';
    document.getElementsByTagName('head')[0].appendChild(meta);
    container.className = "unity-mobile";
    canvas.className = "unity-mobile";
    // To lower canvas resolution on mobile devices to gain some
    // performance, uncomment the following line:
    // config.devicePixelRatio = 1;

  } else {
    // Desktop style: Render the game canvas in a
    // window that can be maximized to fullscreen:
    canvas.style.width = unityCanvasWidth.value + "px";
    canvas.style.height = unityCanvasHeight.value + "px";
  }

  script = document.createElement("script");
  script.src = loaderUrl;
  script.onload = () => {
    createUnityInstance(canvas, config, (progress) => {
      progressBarFull.style.width = 100 * progress + "%";
    }).then((unityInstance) => {
      loadingBar.style.display = "none";
      fullscreenButton.onclick = () => {
        unityInstance.SetFullscreen(1);
      };
      UnityIns = unityInstance;
      initRecord();
    }).catch((message) => {
      alert(message);
    });
  };
  document.body.appendChild(script);
})
</script>

<template>
  <div id="unity-container" class="unity-desktop">
    <canvas id="unity-canvas" tabindex="-1"></canvas>
    <div id="unity-loading-bar">
      <div id="unity-logo"></div>
      <div id="unity-progress-bar-empty">
        <div id="unity-progress-bar-full"></div>
      </div>
    </div>
    <div id="unity-warning"> </div>
    <div id="unity-footer">
      <div id="unity-webgl-logo"></div>
      <div id="unity-fullscreen-button"></div>
      <div id="unity-build-title">AI Asssistant</div>
    </div>
  </div>
</template>

<style scoped>

</style>