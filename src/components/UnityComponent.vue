<script setup>

import {onMounted} from "vue";

onMounted(() =>{
  var container = document.querySelector("#unity-container");
  var canvas = document.querySelector("#unity-canvas");
  var loadingBar = document.querySelector("#unity-loading-bar");
  var progressBarFull = document.querySelector("#unity-progress-bar-full");
  var fullscreenButton = document.querySelector("#unity-fullscreen-button");
  var warningBanner = document.querySelector("#unity-warning");

  // Shows a temporary message banner/ribbon for a few seconds, or
  // a permanent error message on top of the canvas if type=='error'.
  // If type=='warning', a yellow highlight color is used.
  // Modify or remove this function to customize the visually presented
  // way that non-critical warnings and error messages are presented to the
  // user.
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

  var buildUrl = "/src/assets/static/Unity/Build";
  var loaderUrl = buildUrl + "/what.loader.js";
  var config = {
    dataUrl: buildUrl + "/what.data.br",
    frameworkUrl: buildUrl + "/what.framework.js.br",
    codeUrl: buildUrl + "/what.wasm.br",
    streamingAssetsUrl: "StreamingAssets",
    companyName: "DefaultCompany",
    productName: "AI-Asssistant(WebGL)",
    productVersion: "0.1.0",
    showBanner: unityShowBanner,
  };

  // By default, Unity keeps WebGL canvas render target size matched with
  // the DOM size of the canvas element (scaled by window.devicePixelRatio)
  // Set this to false if you want to decouple this synchronization from
  // happening inside the engine, and you would instead like to size up
  // the canvas DOM size and WebGL render target sizes yourself.
  // config.matchWebGLToCanvasSize = false;

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
    // Desktop style: Render the game canvas in a window that can be maximized to fullscreen:

    canvas.style.width = "420px";
    canvas.style.height = "860px";
  }

  loadingBar.style.display = "block";

  var script = document.createElement("script");
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

  // 全局录音实例
  let RecorderIns = null;
  //全局Unity实例   （全局找 unityInstance , 然后等于它就行）
  let UnityIns = null;

  // 初始化 ，   记得调用
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

  // 开始
  function StartRecord() {
    RecorderIns.start();
  }
  // 结束
  function StopRecord() {
    RecorderIns.stop(
        (blob, duration) => {
          console.log(
              blob,
              window.URL.createObjectURL(blob),
              "时长:" + duration + "ms"
          );
          sendWavData(blob)
        },
        (msg) => {
          console.log("录音失败:" + msg);
        }
    );
  }

  // 切片像unity发送音频数据
  function sendWavData(blob) {
    var reader = new FileReader();
    reader.onload = function (e) {
      var _value = reader.result;
      var _partLength = 8192;
      var _length = parseInt(_value.length / _partLength);
      if (_length * _partLength < _value.length) _length += 1;
      var _head = "Head|" + _length.toString() + "|" + _value.length.toString() + "|end" ;
      // 发送数据头
      UnityIns.SendMessage("ChatManager", "GetAudioData", _head);
      for (var i = 0; i < _length; i++) {
        var _sendValue = "";
        if (i < _length - 1) {
          _sendValue = _value.substr(i * _partLength, _partLength);
        } else {
          _sendValue = _value.substr(
              i * _partLength,
              _value.length - i * _partLength
          );
        }
        _sendValue = "Part|" + i.toString() + "|" + _sendValue;
        // 发送分片数据
        UnityIns.SendMessage("ChatManager", "GetAudioData", _sendValue);
      }
      _value = null;
    };
    reader.readAsDataURL(blob);
  }
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