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
クイックスタート用変数
以下の変数は複数のサンプルで共通して使用する。
'''
# サンプルで使用する画像：画像の説明、画像の分類、タグ付け、
# 顔検出、アダルトコンテンツ検出、色調検出、
# ドメイン固有コンテンツ検出、画像タイプ検出、物体検出
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
'''
クイックスタート用変数ここまで
'''


'''
画像のタグ付け（リモート）
この例では、画像内の各要素に対するタグ（キーワード）を返す。
'''
print("===== 画像のタグ付け - リモート =====")
# リモート画像で API を呼び出し
tags_result_remote = computervision_client.tag_image(remote_image_url )

# 信頼度スコア付きで結果を表示
print("リモート画像のタグ: ")
if (len(tags_result_remote.tags) == 0):
    print("タグは検出されませんでした。")
else:
    for tag in tags_result_remote.tags:
        print("'{}' 信頼度 {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
画像のタグ付け（リモート）ここまで
'''

'''
画像の説明（リモート）
この例では、画像の説明を返す。
'''
description_results = computervision_client.describe_image(remote_image_url)
print("リモート画像の説明: ")
if (len(description_results.captions) == 0):
    print("説明は検出されませんでした。")
else:
    for caption in description_results.captions:
        print("'{}' 信頼度 {:.2f}%".format(caption.text, caption.confidence * 100))
print()
'''
画像の説明（リモート）ここまで
'''

'''
画像の分類（リモート）
この例では、画像の分類を返す。
'''
categorize_results_remote = computervision_client.analyze_image(remote_image_url, ["categories"])
print("リモート画像の分類: ")
if (len(categorize_results_remote.categories) == 0):
    print("分類は検出されませんでした。")
else:
    for category in categorize_results_remote.categories:
        print("'{}' 信頼度 {:.2f}%".format(category.name, category.score * 100))
print()
'''
画像の分類（リモート）ここまで
'''

'''
物体検出（リモート）
この例では、画像内の物体を検出する。
'''
object_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"

detect_objects_results_remote = computervision_client.detect_objects(object_image_url)
print("リモート画像の物体検出: ")
if (len(detect_objects_results_remote.objects) == 0):
    print("物体は検出されませんでした。")
else:
    for object in detect_objects_results_remote.objects:
        print("物体: '{}' 信頼度 {:.2f}%".format(object.object_property, object.confidence * 100))
        print("物体の位置: '{}', '{}', '{}', '{}'".format(object.rectangle.x, object.rectangle.y, object.rectangle.w, object.rectangle.h))
print()
'''
物体検出（リモート）ここまで
'''

'''
ローカル画像の物体検出
この例では、ローカル画像内の物体を検出する。
'''
