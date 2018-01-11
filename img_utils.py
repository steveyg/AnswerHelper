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

#通过adb获取android图像
def get_android_img():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')
    crop()

#获取ios图像
def get_ios_img():
    img = ImageGrab.grab()
    #TODO 截取区域可以调整
    box = (0, 300, 850, 1000)
    img = img.crop(box)
    img.save(config.IMAGE_PAGE_TEMP)

#裁剪图像
def crop():
    img = Image.open(config.IMAGE_PAGE)
    plt.figure("beauty")
    plt.subplot(1, 2, 1), plt.title('origin')
    plt.imshow(img), plt.axis('off')
    #TODO 截取区域可以调整
    box = (0, 300, 760, 900)
    roi = img.crop(box)
    roi.save(config.IMAGE_PAGE_TEMP);


#百度ocr获取图片位置
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#识别文字
def spot():
    # get_ios_img();
    crop();
    image = get_file_content(config.IMAGE_PAGE_TEMP);
    result = client.basicGeneral(image);
    return result
