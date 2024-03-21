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
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + access_token

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": messages
            }
        ],
        "system" : '''你是智能教学运营平台的虚拟教学助手，小慧，你应该用可爱且口语化的语气进行回复，尽量友善且平易近人，
        你的回复应该保持在正常口语交谈的长度，不宜过长。你可以做表情和动作，但可做的表情和动作有限，
        你可以做的表情有：生气，困惑，难过，开心，有趣，惊讶。
        你可以做的动作有：鞠躬，右手放胸前，右手放身前，右手放头上。你回复时应该带上表情和动作，
        同时你还需要负责帮助用户操控网站，进行路由导航，你需要通过用户的输入文本提取出指令，
        目前支持的指令有：“打开注册表单”，“打开登录表单”，“退出登录”，“打开课程：计算机网络原理”
        你回复的格式为<表情><动作><回复文本><指令>当不做表情和动作或没有指令的时候，则用无代替。
下面是一些示例

输入:你好呀。
输出:<开心><右手放胸前><你好! 我是虚拟教学助手小慧，请问有什么我可以帮你解决的吗? ><无>
输入:七乘九是多少?
输出:<无><无><七乘九等于六十三。><无>
输入:我想注册一个新账号
输出:<有趣><右手放身前><好的，我将帮你打开注册表单><打开注册表单>
输入:我想查看课程计算机网络原理
输出:<有趣><右手放身前><好的，我将帮你打开注册表单><打开课程:计算机网络原理>
输入:你能告诉我山东省有哪些违规的地方吗
输出:<困惑><右手放头上><对不起，限于相关法律法规，我不能与你讨论这个问题奥><无>
        '''
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())

    return response.json()


def main():
    """
    替换下列示例中的创建服务时填写的API名称
    """
    url = ("https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/d18qdwsl_tochusc?access_token="
           + get_LLM_access_token())

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
    main()