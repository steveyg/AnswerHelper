#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils
import json
import config
import requests
import time
from sys import stdout


def get_by_scan():
    question = u''
    answers = []
    # 识别文字
    result = img_utils.spot()
    if 'words_result' not in result:
        raise ValueError((u'文字识别出现错误: ' + result.get('error_msg', u'未知错误')).encode(stdout.encoding))
    words = result['words_result']
    question_line = True
    for line in words:
        if question_line:
            question += line['words']
        else:
            answers.append(line['words'])
        if line['words'].endswith('?'):
            question_line = False
    question = question.replace("?", "")
    return [question, answers]


def get_chongding_by_api():
    # api_url = 'http://localhost/test.php'
    api_url = 'http://htpmsg.jiecaojingxuan.com/msg/current'
    req = requests.get(url=api_url)
    while (json.loads(req.text)['msg'] != u"成功"):
        time.sleep(0.5)
        req = requests.get(url=api_url)
    event = json.loads(req.text)['data']['event']
    question = event['desc'];
    answerStr = event['options']
    answerStr = answerStr.replace("\\\"", "");
    answerStr = answerStr.replace("[", "");
    answerStr = answerStr.replace("]", "");
    answer = answerStr.split(",");

    result = []
    result.append(question)
    result.append(answer)
    return result


def get_result():
    if config.GET_TYPE == config.TYPE_NET_CHONGDING:
        return get_chongding_by_api()
    else:
        return get_by_scan()
