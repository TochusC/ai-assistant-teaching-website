import base64
from io import BytesIO

from PIL import Image, ImageDraw
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = ('https://aip.baidubce.com/'
        'oauth/2.0/token?grant_type=client_credentials&'
        'client_id=bHETBx4h5z0Na5UIrNZuAb37&'
        'client_secret=cPeXqNxUqFARWX0CQvwTImyXDkhdHkID')


def get_face_access_token():
    response = requests.get(host)
    return response.json().get('access_token')


def face_analysis(image, access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    imageBase64 = str(base64.b64encode(image.read()), 'utf-8')
    params = {
        "image": imageBase64,
        "image_type": "BASE64",
        "max_face_num": 120,
        "face_field": "age,beauty,"
                      "expression,face,"
                      "emotion,location,"
                      "rotation,angle,gender,"
                      "glasses,eye_status,landmark150,quality"
    }
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()


def draw_face_rect(draw, analysis):
    for face in analysis['result']['face_list']:
        # 标出人脸
        left = face['location']['left']
        top = face['location']['top']
        right = left + face['location']['width']
        bottom = top + face['location']['height']

        draw.rectangle((left, top, right, bottom), outline='red', width=3)


def draw_face_landmark(draw, analysis):
    for face in analysis['result']['face_list']:
        for key, value in face['landmark150'].items():
            x = value['x']
            y = value['y']
            size = 1
            draw.ellipse([x - size, y - size, x + size, y + size], fill='blue', outline=None)


def process_face_analysis(img, analysis):
    image = Image.open(img)
    draw = ImageDraw.Draw(image)
    draw_face_rect(draw, analysis)
    draw_face_landmark(draw, analysis)

    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_stream.seek(0)

    processed_image = byte_stream.getvalue()

    return processed_image
