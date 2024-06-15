import base64
import hashlib
import hmac
import io
import os
import shutil
import zipfile
from datetime import datetime
from time import mktime
from urllib import parse
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import chardet

from sample.exception import FileNotFoundException


def get_file_bytes(fd):
    """
    根据文件路径（一般相对）获取二进制数据
    :param fd: 文件路径
    :return: 二进制数据，不存在时为 None供后续判断
    """
    if os.path.exists(fd):
        with open(fd, "rb") as f:
            wav_maker = f.read(4)
            if b'RIFF' == wav_maker:
                f.seek(44, 0)
            else:
                f.seek(0, 0)
            f_data = f.read()
        f.close()
    else:
        raise FileNotFoundException("{}：文件不存在".format(fd))
    return f_data


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


# 生成鉴权的url
def build_auth_request_url(request_url, method="POST", api_key="", api_secret=""):
    url_result = parse.urlparse(request_url)
    date = format_date_time(mktime(datetime.now().timetuple()))
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(url_result.hostname, date, method, url_result.path)
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    values = {
        "host": url_result.hostname,
        "date": date,
        "authorization": authorization
    }
    return request_url + "?" + urlencode(values)


# video ico编码
video_ico_encoding_read_len = 120
# video 其他编码
video_other_encoding_read_len = 122


# 构造流式请求数据
def build_stream_data(payload_data, send_ws, read_len=1280):
    """
     构造流式数据，[content, data_status, wav_length]
    :param payload_data: 多媒体二进制数据
    :param send_ws: 是否流式发送数据
    :param read_len: 每次读取长度
    :return: [[content, data_status, wav_length]]
    """
    stream_list = []
    if len(payload_data) == 0:
        data_status = 2
        stream_list.append([bytes(), data_status, 0])
        return stream_list
    wav_length = len(payload_data)
    input_length = 0
    if not send_ws:
        content = payload_data[input_length:]
        data_status = 2
        stream_list.append([content, data_status, wav_length - input_length])
    else:
        if read_len > wav_length:
            read_len = wav_length
        num = 1
        while input_length + read_len <= wav_length:
            if num == 1:
                data_status = 0
            else:
                data_status = 1
            if input_length + read_len == wav_length:
                data_status = 2
            content = payload_data[input_length: input_length + read_len]
            stream_list.append([content, data_status, read_len])
            num = num + 1
            input_length = input_length + read_len
        if wav_length > input_length:
            content = payload_data[input_length:]
            data_status = 2
            stream_list.append([content, data_status, wav_length - input_length])
    return stream_list


# 构造流式文本请求数据(按行处理)
def build_stream_data_by_line_for_text(text_data):
    stream_list = []
    if len(text_data) == 0:
        data_status = 2
        stream_list.append([bytes(), data_status, 0])
        return stream_list
    charset = chardet.detect(text_data)
    data_str_list_tmp = text_data.decode(charset['encoding']).splitlines()
    data_str_list = [x for x in data_str_list_tmp if x.strip()]

    for index, line in enumerate(data_str_list):
        if index == len(data_str_list) - 1:
            data_status = 2
        elif index == 0:
            data_status = 0
        else:
            data_status = 1
        content = line.encode(charset['encoding'])
        stream_list.append([content, data_status, len(content)])
    return stream_list


# 构造流式图片请求数据
def build_stream_data_one_by_one_for_image(img_zip_data):
    stream_list = []
    if len(img_zip_data) == 0:
        data_status = 2
        stream_list.append([bytes(), data_status, 0])
        return stream_list
    fio = io.BytesIO(img_zip_data)
    img_zip = zipfile.ZipFile(file=fio)
    img_name_list = img_zip.namelist()
    img_name_list_no_dir = [i for i in img_name_list if not i.endswith('/')]
    img_num = len(img_name_list_no_dir)
    img_name_list_no_dir.sort(key=lambda x: x.split("/")[-1])

    for index in range(img_num):
        if index == img_num - 1:
            data_status = 2
        elif index == 0:
            data_status = 0
        else:
            data_status = 1
        content = img_zip.read(img_name_list_no_dir[index])
        stream_list.append([content, data_status, len(content)])
    return stream_list
