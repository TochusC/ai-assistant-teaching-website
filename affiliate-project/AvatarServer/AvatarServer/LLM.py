import requests
import json
import emoji
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
SPARKAI_APP_ID = '3d753ce2'
SPARKAI_API_SECRET = 'ODIyOTJjZDA5ZWQ5NWU5MjVlOGMyNjgx'
SPARKAI_API_KEY = '86a20fef1c407cc12d999c28af5c1be9'
SPARKAI_DOMAIN = 'generalv3.5'

SPARK = ChatSparkLLM(
            spark_api_url=SPARKAI_URL,
            spark_app_id=SPARKAI_APP_ID,
            spark_api_key=SPARKAI_API_KEY,
            spark_api_secret=SPARKAI_API_SECRET,
            spark_llm_domain=SPARKAI_DOMAIN,
            streaming=False,
        )
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


def chat_with_basic_llm(messages, access_token):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + access_token

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": messages
            }
        ]
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
        "system":
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

class Question_Generator:
    def __init__(self):
        self.messages = [
            ChatMessage(role="system", content="你是一个负责相似题目生成的智能助理，你需要根据用户所输入的题目，生成相似题目，并且在生成的题目开头用<>标出相似度，你不需要回答用户的问题。"
                                               "例如：用户输入“论述具有五层协议的网络体系结构的要点，包括各层的主要功能。”，你需要生成一道相似题目“<90%>论述OSI七层协议网络体系结构的关键要素及其各层的核心功能。”。")
        ]
    def generate_question(self, question):
        self.messages.append(ChatMessage(role="user", content=question))
        handler = ChunkPrintHandler()
        response = SPARK.generate([self.messages], callbacks=[handler])
        reply = response.generations[0][0].text
        return reply


class Question_Analyser:
    def __init__(self):
        self.messages = [
            ChatMessage(role="system", content="你是一个负责分析题目的智能助理，你需要根据用户所输入的题目，以百分制分析题目的难度、重要度、创新度、综合度，并在回复中给出。"
                                               "你的回复格式仅仅包含数字和分号，难度、重要度、创新度、综合度的分数之间用分号隔开，例如：90;80;70;60")
        ]

    def question_analysis(self, question):
        self.messages.append(ChatMessage(role="user", content=question))
        handler = ChunkPrintHandler()
        response = SPARK.generate([self.messages], callbacks=[handler])
        reply = response.generations[0][0].text
        return reply

def chat_with_question_generate_LLM(messages):
    agent = Question_Generator()
    return agent.generate_question(messages)

def chat_with_question_analysis_LLM(messages):
    agent = Question_Analyser()
    return agent.question_analysis(messages)

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
