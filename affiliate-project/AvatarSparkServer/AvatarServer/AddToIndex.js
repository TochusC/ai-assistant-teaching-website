    <script src="./recorder.wav.min.js"></script>

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
          UnityIns.SendMessage("SignalManager", "GetAudioData", _head);
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
            UnityIns.SendMessage("SignalManager", "GetAudioData", _sendValue);
          }
          _value = null;
        };
        reader.readAsDataURL(blob);
      }
