#!/usr/bin/python
# -*- coding: utf-8 -*-

import http_utils
import json
import time
import config

result_set = set([])

#判断题目是否进行过展示，使用set去重
def isInSet(value):
    return value in result_set

#展示题目和答案
def display(value):
    json_obj = json.loads(value)
    print json_obj['title']
    if len(json_obj['answers']) > 0:
        print "A." + json_obj['answers'][0] + "  B." + json_obj['answers'][1] + "  C."+json_obj['answers'][2]
        print "==================="
        print u"分析: " + json_obj['search_infos'][0]['summary']
        print "==================="
        print u"推荐答案：  " + json_obj['recommend']
        if config.OPEN_BROWSER:
            http_utils.open_webpage( json_obj['search_infos'][0]['url'])
    print ""
    # print value

#使用搜狗搜索（https://www.sogou.com/）的api自动解答
while(True):
    for value in http_utils.getAutoValue():
        if not isInSet(value):
            result_set.add(value)
            display(value)
    time.sleep(0.5)