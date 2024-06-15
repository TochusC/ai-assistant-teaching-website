#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import ssl
import _thread as thread

import jsonpath
import websocket

from sample import ne_utils, aipass_client
from data import *


# 收到websocket连接建立的处理
def on_open(ws):
    def run():
        # 清除文件
        ne_utils.del_file('./resource/output')
        # 判断是否是多模请求
        exist_audio = jsonpath.jsonpath(request_data, "$.payload.*.audio")
        exist_video = jsonpath.jsonpath(request_data, "$.payload.*.video")
        multi_mode = True if exist_audio and exist_video else False

        # 获取frame，用于设置发送数据的频率
        frame_rate = None
        if jsonpath.jsonpath(request_data, "$.payload.*.frame_rate"):
            frame_rate = jsonpath.jsonpath(request_data, "$.payload.*.frame_rate")[0]
        time_interval = 40
        if frame_rate:
            time_interval = round((1 / frame_rate) * 1000)

        # 获取待发送的数据
        media_path2data = aipass_client.prepare_req_data(request_data)
        # 发送数据
        aipass_client.send_ws_stream(ws, request_data, media_path2data, multi_mode, time_interval)

    thread.start_new_thread(run, ())


# 收到websocket消息的处理
def on_message(ws, message):
    aipass_client.deal_message(ws, message)


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### 执行结束，连接自动关闭 ###")


if __name__ == '__main__':
    # 程序启动的时候设置APPID
    request_data['header']['app_id'] = APPId
    auth_request_url = ne_utils.build_auth_request_url(request_url, "GET", APIKey, APISecret)
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(auth_request_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
