#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, urllib2

import requests

import config
import json
import webbrowser
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def getAutoValue():
    headers = {
        'Host': 'wdpush.sogoucdn.com',
        'Connection': 'keep-alive',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Sogousearch/Ios/5.9.7',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://assistant.sogoucdn.com/v5/cheat-sheet?channel=hj&icon=http%3A%2F%2Fapp.sastatic.sogoucdn.com%2Fdati%2Fhj.png&name=%E7%99%BE%E4%B8%87%E8%B5%A2%E5%AE%B6&appName=%E8%8A%B1%E6%A4%92%E7%9B%B4%E6%92%AD%2F%E5%BF%AB%E8%A7%86%E9%A2%91',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie':'APP-SGS-ID=e6ccf289bbd571f66fc55009dd13711c4e02924f5ddc'
    }
    r = requests.get(headers=headers,url=config.AUTO_URL, verify=False)
    # result = json.loads(r._content)
    # req = urllib2.Request(config.AUTO_URL, None, headers)
    # response = urllib2.urlopen(req)
    html = r._content
    html = html[html.find("(") + 1: len(html) - 1]
    return json.loads(base64.b64decode(json.loads(html)['result']))

def open_webpage(url):
    webbrowser.open(url)
