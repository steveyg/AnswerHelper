#!/usr/bin/python
# -*- coding: utf-8 -*-

# 百度ocr app_id
APP_ID = ''
# 百度ocr api_key
API_KEY = ''
# 百度ocr secret_key
SECRET_KEY = ''

# 图片默认路径
IMAGE_PAGE = "img.jpg"
IMAGE_PAGE_TEMP = "temp.jpg"

# 获取题目方式
TYPE_IMG = 0
TYPE_NET_CHONGDING = 1

# 设备
TYPE_ANDROID = 10
TYPE_IOS = 11
TYPE_PC = 12

# 裁剪区域因子
FACTOR_CHONGDING = 0.24
FACTOR_BAIWAN = 0.13

# 默认题目获取方式、设备类型和裁剪因子
GET_TYPE = TYPE_IMG
GET_DEVICE_TYPE = TYPE_PC
GET_FACTOR = FACTOR_CHONGDING

# 投屏参数配置
# 投屏到桌面的截屏范围，(左，上，右，下)
PC_CROP_BOX = (0, 300, 850, 1000)

# 投屏到桌面的窗口标题
# 若设置此参数，手动设置的截屏范围(PC_CROP_BOX)将被忽略
# 仅支持 Windows，其他平台请勿设置
PC_WINDOW_NAME = ''
# 截图出现空白、黑屏可将其设为1
PC_WINDOW_FALLBACK = 1

# 默认是否打开浏览器
OPEN_BROWSER = 0
