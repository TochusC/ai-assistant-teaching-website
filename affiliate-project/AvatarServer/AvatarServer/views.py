from io import BytesIO

from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from pydub import AudioSegment

from AvatarServer import STT
from AvatarServer import TTS
from AvatarServer import LLM

voice_access_token = STT.get_voice_access_token()
LLM_access_token = LLM.get_LLM_access_token()


def chat_with_llm(user_text):
    response_llm = LLM.chat_with_LLM(user_text, LLM_access_token)
    llm_reply = response_llm.get("result")
    if "><" in llm_reply:
        expression, action, reply, command = llm_reply.split("><")[0:4]
        expression = expression[1:]
        command = command[:-1]
    else:
        reply = llm_reply
        expression = "无"
        action = "无"
        command = "无"

    reply.replace(" ", "")
    reply.replace("\n", "")

    print("大语言模型的回复: " + llm_reply + "\n")

    response_audio = TTS.get_audio_from_text(reply,
                                             voice_access_token)

    with open("out.wav", 'wb') as f:
        f.write(response_audio)

    response_audio = open("out.wav", 'rb').read()

    response = HttpResponse(content_type="audio/wav")
    response.write(response_audio)
    response["Command"] = command
    response["Expression"] = expression
    response["Action"] = action
    return response

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def text_chat(request):
    user_text = request.POST["userText"]

    print("用户输入的文本:", user_text)
    return chat_with_llm(user_text);


# 表单
# POST
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def voice_chat(request):
    audio_data = request.FILES.get("file")

    response_stt = STT.get_text_from_audio(audio_data, voice_access_token)

    user_text = response_stt.get("result")[0]

    print("用户语音的文本识别结果: " + user_text + "\n")

    return chat_with_llm(user_text)


def test(request):
    response_audio = open("out.wav", 'rb').read()

    respone = HttpResponse(content_type="audio/wav")
    respone.write(response_audio)
    return respone
