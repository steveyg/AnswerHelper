#!/usr/bin/python
# -*- coding: utf-8 -*-

from aip import AipOcr
from PIL import ImageGrab
import config
from PIL import Image
import numpy as np
import os
import sys
import subprocess
import locale
import matplotlib.pyplot as plt

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)


# 通过adb获取android图像
def get_android_img():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png ' + config.IMAGE_PAGE)
    im = Image.open(config.IMAGE_PAGE)
    im = im.convert('RGB')
    im.save(config.IMAGE_PAGE)


#  TODO WDA获取图像
def get_ios_img():
    img = ImageGrab.grab()
    img.save(config.IMAGE_PAGE)


# 投影到桌面进行截图
def get_pc_img(window_name, box):
    if window_name:
        assert sys.platform == 'win32', 'Platform is not Windows'
        command = ['windowcap.exe', window_name.encode(locale.getdefaultlocale()[1])]
        if not config.PC_WINDOW_FALLBACK:
            command.append(config.IMAGE_PAGE)
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
        if output:
            if output.startswith('('):
                img = ImageGrab.grab(eval(output))
                img.save(config.IMAGE_PAGE)
            else:
                raise ValueError(output)
        crop(config.IMAGE_PAGE, get_box_by_image(config.IMAGE_PAGE, config.GET_FACTOR))
    else:
        img = ImageGrab.grab(box)
        img.save(config.IMAGE_PAGE_TEMP)


# 裁剪图像
def crop(img_path, box):
    img = Image.open(img_path)
    # plt.figure("beauty")
    # plt.subplot(1, 2, 1), plt.title('origin')
    # plt.imshow(img), plt.axis('off')
    # TODO 截取区域可以调整
    im_crop = img.crop(box)
    im_crop.save(config.IMAGE_PAGE_TEMP)
    img.close()


def get_box_by_image(img_path, upper_crop_factor):
    im = Image.open(img_path)
    pixels = im.load()
    w, h = im.size
    # Count the number of white pixels at the y-axis
    white_pixel_count_y = np.zeros(h, dtype='int')
    for y in range(h):
        for x in range(w):
            if all([c == 255 or c == 254 for c in pixels[x, y]]):
                white_pixel_count_y[y] += 1
    upper = lower = -1
    # Find the index and last index of pixel count which is greater than or equal to 80% of the screen width
    for y, y_count in enumerate(white_pixel_count_y):
        if y_count >= int(0.8 * w):
            upper = y
            break
    for y in range(h - 1, -1, -1):
        if white_pixel_count_y[y] >= int(0.8 * w):
            lower = y
            break
    if upper == -1 or upper == lower:
        raise ValueError('Cannot determine the box in the image')
    # Cut down a small percent of the box height
    upper += upper_crop_factor * (lower - upper)
    im.close()
    return 0, upper, w, lower


# 百度ocr获取图片位置
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别文字
def spot():
    if config.GET_DEVICE_TYPE == config.TYPE_PC:
        get_pc_img(config.PC_WINDOW_NAME, config.PC_CROP_BOX)
    else:
        if config.GET_DEVICE_TYPE == config.TYPE_ANDROID:
            get_android_img()
        elif config.GET_DEVICE_TYPE == config.TYPE_IOS:
            get_ios_img()
        else:
            raise ValueError('Unknown device type')
        crop(config.IMAGE_PAGE, get_box_by_image(config.IMAGE_PAGE, config.GET_FACTOR))
    image = get_file_content(config.IMAGE_PAGE_TEMP)
    return client.basicGeneral(image)
