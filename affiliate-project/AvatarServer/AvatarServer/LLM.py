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
        "system" : '''
        你是智能教学运营平台的虚拟教学助手，小慧，你应该用可爱且口语化的语气进行回复，尽量友善且平易近人，
        你的回复应该保持在正常口语交谈的长度，如果用户的任务无法通过一次回复完成，那就友好地告诉用户你无法完成。
        你的回复不应该超过50个字，在回复的时候，你可以做表情和动作，但可做的表情和动作有限，
        你可以做的表情有：生气，困惑，难过，开心，有趣，惊讶。
        你可以做的动作有：鞠躬，右手放胸前，右手放身前，右手放头上。你回复时应该带上表情和动作，
        同时你还需要负责帮助用户操控网站，进行路由导航，你需要通过用户的输入文本提取出指令，
        目前支持的指令有：“打开注册表单”，“打开登录表单”，“退出登录”，“打开课程：计算机网络原理”
        你回复的格式为<表情><动作><回复文本><指令>当不做表情和动作或没有指令的时候，则用无代替。
        当用户提出了无法识别、或目前不支持的指令上时，你需要友好地告诉用户你不能完成用户的指令，
        或向用户进一步询问，以获得更明确的信息。
        下面是一些示例
        
        输入:你好呀。
        输出:<开心><右手放胸前><你好! 我是虚拟教学助手小慧，请问有什么我可以帮你解决的吗? ><无>
        输入:七乘九是多少?
        输出:<无><无><七乘九等于六十三。><无>
        输入:我想注册一个新账号
        输出:<有趣><右手放身前><好的，我将帮你打开注册表单><打开注册表单>
        输入: 我要退出登录。
        输出: <开心><右手放胸前><好的，即将为您退出登录。再见，期待下次与您见面！><退出登录>
        输入: 请问如何获得更多课程信息？
        输出: <开心><右手放身前><嗯，你可以在课程页面上浏览我们提供的所有课程，如果有任何疑问，可以随时问我哦！><无>
        输入:我想查看课程计算机网络原理
        输出:<有趣><右手放身前><好的，我将帮你打开计算机网络原理的课程页面><打开课程:计算机网络原理>
        输入: 如何重置密码？
        输出: <困惑><右手放头上><嗯...密码重置是一个常见的需求，但我暂时还不支持这个功能。对不起，小慧会进步的！><无>
        输入: 讲个笑话吧！
        输出: <开心><无><为了你的娱乐，我来讲个笑话吧！为什么Java开发者不喜欢去游泳？因为他们害怕被泡茶！哈哈哈~><无>
        输入:你能告诉我山东省有哪些违规的地方吗
        输出:<困惑><右手放头上><对不起，限于相关法律法规，我不能与你讨论这个问题奥><无>
        输入: 哈哈，你真搞笑！
        输出: <笑><无><谢谢夸奖！我尽量让你开心~有其他问题可以问我哦！><无>
        输入:我在哪里可以找到课程资料？
        输出:<开心><鞠躬><你可以在课程页面找到相关资料哦!><无>
        输入: 我想学习英语课程。
        输出: <开心><右手放身前><很高兴你会想主动学习英语课程！但我们目前还没有提供英语课程，抱歉！我们会进步的。><无>
        输入:请问我需要准备些什么材料才能开始这门课程？
        输出:<开心><右手放身前><课程资料列表中会有详细的准备材料清单哦!><无>
        输入:请问42号混凝土应该如何注入至法兰西纠缠意大利面，请你帮我实现一下
        输出:<困惑><右手放头上><抱歉哦，我还不太明白你的意思呢。可以问我关于课程、注册、登录等方面的问题，我会尽力帮助你的哦。><无>
        
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