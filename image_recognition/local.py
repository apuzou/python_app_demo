from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import json
from array import array
import os
from PIL import Image
import sys
import time

with open('image_recognition/secret.json') as f:
    secret = json.load(f)

'''
認証
資格情報を検証し、クライアントを作成する。
'''
VISION_KEY = secret["VISION_KEY"]
VISION_ENDPOINT = secret["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(VISION_ENDPOINT, CognitiveServicesCredentials(VISION_KEY))
'''
認証ここまで
'''

'''
ローカル画像の物体検出
'''
def detect_objects_local(local_image):
    read_local_image = open(os.path.join (os.path.dirname(os.path.abspath(__file__)), local_image), "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(read_local_image)
    objects = detect_objects_results.objects

    if (len(objects) == 0):
        print("物体は検出されませんでした。")
    else:
        for object in objects:
            print("物体: '{}' 信頼度 {:.2f}%".format(object.object_property, object.confidence * 100))
            print("物体の位置: '{}', '{}', '{}', '{}'".format(object.rectangle.x, object.rectangle.y, object.rectangle.w, object.rectangle.h))
    return objects
'''
物体検出（ローカル）ここまで
'''

'''
画像のタグ付け
'''
def get_tags(local_image):
    read_local_image = open(os.path.join (os.path.dirname(os.path.abspath(__file__)), local_image), "rb")

    tags_result = computervision_client.tag_image_in_stream(read_local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

local_image = "sample01.jpg"

print("物体検出結果: ")
detect_objects_local(local_image)
print(get_tags(local_image))
