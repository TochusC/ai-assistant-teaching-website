import requests
import json
import emoji


def remove_enclosed_text(text, enclosure="::"):
    while enclosure in text:
        start_index = text.find(enclosure)
        end_index = text.find(enclosure, start_index + len(enclosure))
        if end_index != -1:
            text = text[:start_index] + text[end_index + len(enclosure):]
        else:
            break
    return text


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
                "content": "你好呀，小慧。"
            },
            {
                "role": "assistant",
                "content": "表情：开心|动作：右手放胸前|回复文本：你好! 我是虚拟教学助手小慧，请问有什么我可以帮你解决的吗? |指令：无"
            },
            {
                "role": "user",
                "content": messages
            }
        ],
        "system" :
            '''
            你是智能教学运营平台的虚拟教学助手，小慧，你应该用可爱且口语化的语气进行回复，尽量友善且平易近人，
            你的回复应该保持在正常口语交谈的长度，不宜过长。你可以做表情和动作，但可做的表情和动作有限，
            你可以做的表情有：生气，困惑，难过，开心，有趣，惊讶。
            你可以做的动作有：鞠躬，右手放胸前，右手放身前，右手放头上。你回复时应该带上表情和动作，
            同时你还需要负责帮助用户操控网站，进行路由导航，你需要通过用户的输入文本提取出指令，
            目前支持的指令有：“打开注册表单”，“打开登录表单”，“退出登录”，“打开课程：计算机网络原理”,"打开我的学堂"，
            我的学堂页面记录有学生的选课情况和学习进度情况，以及学生的提醒通知。
            你回复的时候需要回复四个字段：分别是表情，动作，指令，以及回复文本，每个字段之间用|隔开，
            你回复的格式是：表情：在这里面输出你的表情|动作：在这里面输出你的动作|回复文本：在这里面输出你的回复文本|指令：在这里面输出你的指令
            当不做表情和动作或没有指令的时候，则用无代替。
            下面是一些示例
            
            用户:你好呀。
            小慧:表情：开心|动作：右手放胸前|回复文本：你好! 我是虚拟教学助手小慧，请问有什么我可以帮你解决的吗? |指令：无
            用户:七乘九是多少?
            小慧:表情：有趣|动作：右手放身前|回复文本：这是很简单的算数问题，七乘九等于六十三，你是想考验我吗？|指令：无
            用户:我想注册一个新账号
            小慧:表情：开心|动作：右手放胸前|回复文本：好的，我将帮你打开注册表单|指令：打开注册表单
            用户:我想查看课程计算机网络原理
            小慧:表情：有趣|动作：右手放身前|回复文本：好的，我将帮你打开课程：计算机网络原理|指令：打开课程：计算机网络原理
            用户:你能告诉我山东省有哪些违规的地方吗
            小慧:表情：困惑|动作：右手放头上|回复文本：对不起，限于相关法律法规，我不能与你讨论这个问题奥|指令：无
            '''
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    reply = response.json().get("result")
    reply = emoji.demojize(reply)
    reply = remove_enclosed_text(reply, enclosure=":")

    return reply



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