## 运行环境
python3.8
## 项目目录介绍
### requirements.txt
项目依赖包管理文件<br>
首次下载此项目后执行`pip3 install -r requirements.txt`即下载安装依赖包

### data.py
根据接口文档自动生成的相关配置（请根据接口文档配置所需的请求参数）
- 请求协议
- 请求地址
- 响应数据段，便于程序处理接口响应
- APPId、APIKey、APISecret信息

### main.py
程序的执行入口，使用websocket建立连接

### resource目录
此目录提供平台内置的请求文件以及后续保存程序执行响应文件

### sample目录
程序核心执行逻辑步骤

#### exception.py
自定义异常

#### ne_utils.py
工具文件 
- 读取问题获取文件内容
- 清空目录
- 生成鉴权的url
- 解析url获取对应的host、path、schema
- 构造流式请求数据
- 构造流式文本请求数据
- 构造流式图片请求数据

#### aipaas_client.py
核心程序执行
- 数据准备 prepare_req_data
- 发送数据 send_ws_stream
- 处理响应数据 deal_message

#### h26x_client.py nalutypes.py
处理视频编码的工具类

## 补充说明
### 音频流式发送
#### 使用的speex音频区分开源和讯飞定制两种：
开源的speex-wb要传frame_size，值一般是60，按120一段发送；<br>
讯飞定制的speex-wb 不需要frame_size，一般按122一段发送；<br> 
请注意 **内置的文件是讯飞定制的格式** 在使用时需要按照实际情况修改
#### 音频格式参照表
![avatar](./resource/input/image/音频格式对照表.png)
