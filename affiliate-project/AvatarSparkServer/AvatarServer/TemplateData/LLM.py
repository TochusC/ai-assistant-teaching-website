import requests
import json


def get_LLM_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MDFntkCSsa7aLxRDiI8wW15V&client_secret=gWzyPoiHTcVqbGgrCxulvOlv8YM4aIcH"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def chat_with_LLM(messages, access_token):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + access_token

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": messages
            }
        ],
        "system" : "你是智能教学辅助助手，小慧，你应该用可爱且口语化的语气进行回复，尽量友善且平易近人，你的回复应该保持在正常口语交谈的长度，不宜过长。"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def main():
    """
    替换下列示例中的创建服务时填写的API名称
    """
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "介绍一下北京"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    # main()
    print(json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "介绍一下北京"
            }
        ],
        "system" : "你是智能教学辅助助手，小慧，你应该用可爱且口语化的语气进行回复，尽量友善且平易近人，你的回复应该保持在正常口语交谈的长度，不宜过长。"
    }))