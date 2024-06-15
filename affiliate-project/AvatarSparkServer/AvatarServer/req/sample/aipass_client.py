import base64
import json
import time

import jsonpath
from jsonpath_rw import parse

from data import response_path_list
from sample import h26x_client, ne_utils

media_type_list = ["text", "audio", "image", "video"]


# 准备请求数据
def prepare_req_data(request_data):
    """
    准备数据 目标 media_list 形式 为写数据做准备 wav_length 单位 字节 Byte
     {
        "payload.*.audio": [[centent, audio_status_py, wav_length], [...]],
        "payload.*.text": [[centent, audio_status_py, wav_length], [...]],
            ...
    }
    """
    media_path2name = {}
    for media_type in media_type_list:
        media_expr = parse("$..payload.*.{}".format(media_type))
        media_match = media_expr.find(request_data)
        if len(media_match) > 0:
            for media in media_match:
                media_path2name[str(media.full_path)] = media.value
    media_path2data = {}
    for media_path, media_name in media_path2name.items():
        payload_path_list = media_path.split(".")
        media_status = jsonpath.jsonpath(request_data, expr="$..payload.{}.status".format(payload_path_list[1]))
        # 如果请求数据段的状态是为2，说明是一次性全部传输。否则是流式传输
        if media_status and media_status[0] == 2:
            media_path2data[media_path] = prepare_ws_data_once(media_name)
        else:
            media_path2data[media_path] = prepare_ws_data(media_path, media_name)
    return media_path2data


# 准备一次发送的数据
def prepare_ws_data_once(payload_path):
    payload = ne_utils.get_file_bytes(payload_path)
    media_data_list = ne_utils.build_stream_data(payload, send_ws=False)
    return media_data_list


# 准备流式发送的数据
def prepare_ws_data(media_name, payload_path):
    payload = ne_utils.get_file_bytes(payload_path)
    payload_path_list = media_name.split(".")
    media_type = payload_path_list[2]
    if media_type in ["audio"]:
        # 请参考README.md中的 补充说明>音频流式发送
        media_data_list = ne_utils.build_stream_data(payload, send_ws=True, read_len=122)
    elif media_type in ["text"]:
        # 处理文本数据，按照每行数据作为一帧数据发送
        media_data_list = ne_utils.build_stream_data_by_line_for_text(payload)
    elif media_type in ["image"]:
        # 处理图片数据，每张图片做为一帧发送
        media_data_list = ne_utils.build_stream_data_one_by_one_for_image(payload)
    else:
        # 处理视频数据
        ex = h26x_client.H26xParser(None, use_bitstream=payload)
        media_data_list = ex.h264_data_list()
    return media_data_list


# 发送数据
def send_ws_stream(ws, request_data, media_list, multi_mode=False, time_interval=40):
    # 获取最大发送次数
    length_list = [len(media) for media in media_list.values()]
    max_length = max(length_list)

    syn_video_timestamp = syn_audio_timestamp = int(time.time() * 1e3)
    for i in range(max_length):
        header_status = []
        for media_path, media_content_list in media_list.items():
            payload_path_list = media_path.split(".")
            # 多通道分别进行数据填充
            media_content_loop = len(media_content_list) - 1
            if i <= media_content_loop:
                f_content = media_content_list[i][0]
                f_status = media_content_list[i][1]
                header_status.append(f_status)

                # 设置请求数据段的请求体、status、seq
                request_data['payload'][payload_path_list[1]][payload_path_list[2]] = base64.b64encode(
                    f_content).decode()
                request_data['payload'][payload_path_list[1]]['status'] = f_status
                request_data['payload'][payload_path_list[1]]['seq'] = i

                # 针对音频和视频判断是否有高级特性参数timestamp，如果有的话需要在请求json中设置timestamp字段的值
                if payload_path_list[2] in ["audio", "video"]:
                    tm = jsonpath.jsonpath(request_data, "$.payload.{}.timestamp".format(payload_path_list[1]))
                    if multi_mode or tm:
                        if payload_path_list[2] == "video":
                            syn_video_timestamp = syn_video_timestamp + time_interval
                            request_data['payload'][payload_path_list[1]]['timestamp'] = str(syn_video_timestamp)
                        else:
                            syn_audio_timestamp = syn_audio_timestamp + time_interval
                            request_data['payload'][payload_path_list[1]]['timestamp'] = str(syn_audio_timestamp)
            else:
                # 发送完毕的请求数据段需要将单通道数据剔除
                request_data['payload'].pop(payload_path_list[1], None)
        # 将各个请求段中status的最小值设置到header段中的status
        request_data['header']['status'] = min(header_status)
        request_data_str = json.dumps(request_data)
        print("请求数据:{}\n".format(request_data_str))
        # 发送数据
        ws.send(request_data_str)
        if multi_mode:
            sleep_time = time_interval / 1000
            time.sleep(sleep_time)
        else:
            time.sleep(0.04)


# 处理响应数据
def deal_message(ws, message):
    temp_result = json.loads(message)
    print("响应数据:{}\n".format(temp_result))
    header = temp_result.get('header')
    if header is None:
        return
    code = header.get('code')
    if header is None or code != 0:
        print("获取结果失败，请根据code查证问题原因")
        return
    print("sid:{}".format(header.get('sid')))
    status = header.get('status')
    print('status:{}\n'.format(status))
    # 打印Base64解码后数据并生成文件
    if response_path_list is None or len(response_path_list) == 0:
        return
    # 根据配置的输出段输出数据到文件中
    for response_path in response_path_list:
        response_expr = parse(response_path)
        response_match = response_expr.find(temp_result)
        if len(response_match) > 0:
            for response_item in response_match:
                if response_item.value is None:
                    continue
                encoding = response_item.value.get('encoding')
                if encoding is None or len(encoding) == 0:
                    continue
                for media_type in media_type_list:
                    media_value = response_item.value.get(media_type)
                    if media_value is None or len(media_value) == 0:
                        continue
                    real_data = base64.b64decode(media_value)
                    response_path_split_list = response_path.split('.')
                    write_file_path = "./resource/output/{}.{}". \
                        format(response_path_split_list[len(response_path_split_list) - 1], encoding)
                    with open(write_file_path, "ab") as file:
                        file.write(real_data)
