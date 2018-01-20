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

# 是否使用Windows投屏窗口化截图
# 若使用，设为1，手动设置的截屏范围将被忽略
# 仅支持 Windows，其他平台请保持该值为0
PC_USE_WINDOW_CAPTURE = 0

# 是否使用兼容模式
PC_WINDOW_FALLBACK = 0
PC_WINDOW_CONFIG = 'window.ini'

# 默认是否打开浏览器
OPEN_BROWSER = 0

#搜狗搜索api
#冲顶大会
KEY_CHONGDING = 'cddh'
#西瓜视频
KEY_XIGUA = 'xigua'
#百万赢家
KEY_BAIWAN = 'huajiao'
#芝士超人
KEY_ZHISHI = 'zscr'

#设置自动的类型
AUTO_URL_KEY = KEY_CHONGDING

AUTO_URL = 'http://140.143.49.31/api/ans2?key='+AUTO_URL_KEY+'&wdcallback=jQuery321007193239172920585_1516186783454&_=1516186784191'
