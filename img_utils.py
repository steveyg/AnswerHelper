#!/usr/bin/python
# -*- coding: utf-8 -*-

from aip import AipOcr
from PIL import ImageGrab
import config
import json
from PIL import Image
import matplotlib.pyplot as plt
import datetime

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)
import os


# 通过adb获取android图像
def get_android_img():
    os.system('adb shell screencap -p > ' + config.IMAGE_PAGE)
    im = Image.open(config.IMAGE_PAGE)
    im = im.convert('RGB')
    im.save(config.IMAGE_PAGE)


# 获取ios图像
def get_ios_img():
    img = ImageGrab.grab()
    img.save(config.IMAGE_PAGE)


# 裁剪图像
def crop(img_path, box):
    img = Image.open(img_path)
    # plt.figure("beauty")
    # plt.subplot(1, 2, 1), plt.title('origin')
    # plt.imshow(img), plt.axis('off')
    # TODO 截取区域可以调整
    im_crop = img.crop(box)
    im_crop.save(config.IMAGE_PAGE_TEMP)


# 百度ocr获取图片位置
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别文字
def spot():
    if config.GET_DEVICE_TYPE == config.TYPE_ANDROID:
        get_android_img()
        crop(config.IMAGE_PAGE, (0, 300, 760, 900))
    elif config.GET_DEVICE_TYPE == config.TYPE_IOS:
        get_ios_img()
        crop(config.IMAGE_PAGE, (0, 300, 750, 880))
    else:
        raise ValueError('Unknown device type')
    image = get_file_content(config.IMAGE_PAGE_TEMP)
    return client.basicGeneral(image)
