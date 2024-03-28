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


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def chat_with_llm(request):
    user_text = request.POST["userText"]
    llm_reply = LLM.chat_with_LLM(user_text, LLM_access_token)

    print("LLM回复:", llm_reply)

    return HttpResponse(llm_reply)


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def voice_recognize(request):
    audio_data = request.FILES.get("file")

    response_stt = STT.get_text_from_audio(audio_data, voice_access_token)

    user_text = response_stt.get("result")[0]

    print("用户输入的文本:", user_text)

    return HttpResponse(user_text)


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def voice_synthesis(request):
    llm_reply = request.POST["llmReply"]
    response_audio = TTS.get_audio_from_text(llm_reply,
                                             voice_access_token)

    response = HttpResponse(content_type="audio/wav")
    response.write(response_audio)
    return response

# @csrf_exempt
# @require_http_methods(["GET", "OPTIONS"])
# def testField(request):
#     llm_reply = request.GET["llmReply"]
#     response_audio = TTS.get_audio_from_text(llm_reply,
#                                              voice_access_token)
#
#     # with open("out.wav", 'wb') as f:
#     #     f.write(response_audio)
#     #
#     # response_audio = open("out.wav", 'rb').read()
#
#     response = HttpResponse(content_type="audio/wav")
#     response.write(response_audio)
#     return response

@csrf_exempt
@require_http_methods(["GET", "OPTIONS"])
def testField(request):
    user_text = request.GET["userText"]
    print("用户输入的文本:", user_text)
    response_llm = LLM.chat_with_LLM(user_text, LLM_access_token)
    llm_reply = response_llm.get("result")
    print("LLM回复:", llm_reply)
    return HttpResponse(llm_reply)


