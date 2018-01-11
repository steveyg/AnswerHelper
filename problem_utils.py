#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils
import json
import solve_utils
import config
import requests

def get_by_scan():
	question = '';
	answer = [];
	#识别文字
	words = img_utils.spot()['words_result'];
	flag = 1;
	#问题
	if len(words) == 4:
	    question = words[0]['words'];
	elif len(words) == 5:
	    question = words[0]['words'] + words[1]['words'];
	    flag = 2;
	question = question.replace("?","")

	#选项
	for i in range(flag,len(words)):
	    answer.append(words[i]['words'])
	    print u"选项" + str(i - flag + 1) + u" : " +answer[i - flag]

	question = question.replace("?","")
	result = []
	result.append(question)
	result.append(answer)
	return result

def get_chongding_by_api():
	#api_url = 'http://localhost/test.php'
	api_url = 'http://htpmsg.jiecaojingxuan.com/msg/current'
	req = requests.get(url=api_url)
	while(json.loads(req.text)['msg']  != u"成功"):
		req = requests.get(url=api_url)
	event = json.loads(req.text)['data']['event']
	question = event['desc'];
	answerStr = event['options']
	answerStr = answerStr.replace("\\\"","");
	answerStr = answerStr.replace("[","");
	answerStr = answerStr.replace("]","");
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