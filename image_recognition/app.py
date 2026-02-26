from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import json
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

# '''
# 認証
# 資格情報を検証し、クライアントを作成する。
# '''
try:
    VISION_ENDPOINT = st.secrets["VISION_ENDPOINT"]
    VISION_KEY = st.secrets["VISION_KEY"]
except (StreamlitSecretNotFoundError, KeyError, FileNotFoundError):
    secret_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret.json")
    with open(secret_path) as f:
        secret = json.load(f)
    VISION_ENDPOINT = secret["VISION_ENDPOINT"]
    VISION_KEY = secret["VISION_KEY"]

computervision_client = ComputerVisionClient(VISION_ENDPOINT, CognitiveServicesCredentials(VISION_KEY))

# '''
# ローカル画像の物体検出
# '''
def detect_objects(local_image):
    read_local_image = open(local_image, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(read_local_image)
    objects = detect_objects_results.objects
    return objects

# '''
# 画像のタグ付け
# '''
def get_tags(local_image):
    read_local_image = open(local_image, "rb")

    tags_result = computervision_client.tag_image_in_stream(read_local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

from PIL import ImageDraw
from PIL import ImageFont

st.title("物体検出アプリ")

uploaded_file = st.file_uploader("画像をアップロードしてください。", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'image_recognition/img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Helvetica 400.ttf")
        font = ImageFont.truetype(font=font_path, size=50)
        text_w, text_h = font.getbbox(caption)[2:4]

        draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=5)
        draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
        draw.text((x, y), caption, fill='white', font=font)

    st.image(img, caption="アップロードされた画像", use_container_width=True)

    st.markdown("**認識されたコンテンツタグ**")
    st.markdown(f'> {get_tags(img_path)}')
