import base64
from io import BytesIO

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from AvatarServer import STT, face
from AvatarServer import TTS
from AvatarServer import LLM

VOICE_ACCESS_TOKEN = STT.get_voice_access_token()
LLM_ACCESS_TOKEN = LLM.get_LLM_access_token()
FACE_ACCESS_TOKEN = face.get_face_access_token()

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def chat_with_llm(request):
    user_text = request.POST["userText"]
    llm_reply = LLM.chat_with_LLM(user_text, LLM_ACCESS_TOKEN)

    print("LLM回复:", llm_reply)

    return HttpResponse(llm_reply)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def chat_with_basic_llm(request):
    user_text = request.POST["userText"]
    llm_reply = LLM.chat_with_basic_llm(user_text, LLM_ACCESS_TOKEN)

    print("LLM回复:", llm_reply)

    return HttpResponse(llm_reply)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def generate_question(request):
    user_text = request.POST["userText"]
    llm_reply = LLM.chat_with_question_generate_LLM(user_text)

    print("LLM回复:", llm_reply)

    return HttpResponse(llm_reply)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def analysis_question(request):
    user_text = request.POST["userText"]
    llm_reply = LLM.chat_with_question_analysis_LLM(user_text)

    print("LLM回复:", llm_reply)

    return HttpResponse(llm_reply)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def voice_recognize(request):
    audio_data = request.FILES.get("file")

    response_stt = STT.get_text_from_audio(audio_data, VOICE_ACCESS_TOKEN)

    user_text = response_stt.get("result")[0]
    print("用户输入的文本:", user_text)

    return HttpResponse(user_text)


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def voice_synthesize(request):
    llm_reply = request.POST["llmReply"]
    response_audio = TTS.get_audio_from_text(llm_reply,
                                             VOICE_ACCESS_TOKEN)

    response = HttpResponse(content_type="audio/wav")
    response.write(response_audio)
    return response

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def face_analysis(request):
    image_data = request.FILES.get("img")

    analysis = face.face_analysis(image_data, FACE_ACCESS_TOKEN)
    processed_image = face.process_face_analysis(image_data, analysis)

    img_base64 = base64.b64encode(processed_image).decode()
    response = {"img": img_base64, "analysis": analysis}
    return JsonResponse(response)



