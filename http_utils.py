#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, urllib2
import config
import json
import webbrowser

def getAutoValue():
    headers = {
        'Host': '140.143.49.31',
        'Connection': 'keep-alive',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 Sogousearch/Ios/5.9.7',
        'Accept-Language': 'zh-cn',
        'Referer': 'http://nb.sa.sogou.com/',
        'Accept-Encoding': 'gzip, deflate'
    }
    req = urllib2.Request(config.AUTO_URL, None, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    html = html[html.find("(") + 1: len(html) - 1]
    return json.loads(html)['result']

def open_webpage(url):
    webbrowser.open(url)
