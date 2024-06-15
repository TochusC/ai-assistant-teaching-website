from urllib.parse import urlencode

import requests
import json
from pydub import AudioSegment


api_key = "G0gaXSL56dHKQoHi1WWkldnb"
secret_key = "RGoQe3ZwD0xhGDtgHWxhBHgYBFdU0trB"

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = ("http://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&"
           "client_id=" + api_key + "&client_secret=" + secret_key)

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def get_audio_from_text(text, access_token, per=111):
    url = "https://tsn.baidu.com/text2audio"

    headers = {
        'Content-Type': 'audio/wav;'
    }

    parameter = {
        "tex":text,
        "lan":"zh",
        "ctp":"1",
        "cuid":"toch",
        "aue":"6",
        "per":per,
        "tok":access_token
    }

    payload = urlencode(parameter)

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.content

def spark_get_audio_from_text(text):
    url = "http://127.0.0.1:9880/?text=" + text + "&text_language=zh"

    payload = json.dumps(
        {
        "refer_wav_path": "zhou.wav",
        "prompt_text": "我刚刚还看到有人说，等着我开播就掉小珍",
        "prompt_language": "zh",
        "text": text,
        "text_language": "zh"
    }
    )

    response = requests.request("POST", url, data=payload)
    return response.content

def sovits_get_audio_from_text(text):
    url = "http://127.0.0.1:9880/?text=" + text + "&text_language=zh"

    payload = json.dumps(
        {
        "refer_wav_path": "zhou.wav",
        "prompt_text": "我刚刚还看到有人说，等着我开播就掉小珍",
        "prompt_language": "zh",
        "text": text,
        "text_language": "zh"
    }
    )

    response = requests.request("POST", url, data=payload)
    return response.content


def main():
    """
    替换下列示例中的创建服务时填写的API名称
    """
    tok = get_access_token()
    url = "https://tsn.baidu.com/text2audio"

    headers = {
        'Content-Type': 'audio/wav;'
    }

    parameter = {
        "tex":"哈喽，我听到你的请求啦，请等小慧思考一下",
        "lan":"zh",
        "ctp":"1",
        "cuid":"toch",
        "aue":"6",
        "tok":get_access_token()
    }

    payload = urlencode(parameter)

    response = requests.request("POST", url, headers=headers, data=payload)

    with open("out.wav", 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    # response_audio = get_audio_from_text("我听到你的请求啦，请等小慧思考一下", get_access_token())
    #
    # with open("out.wav", 'wb') as f:
    #     f.write(response_audio)
    print(get_access_token())