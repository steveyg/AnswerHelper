#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import requests

#直接用浏览器打开问题
def open_wabpage(question):
    webbrowser.open('https://baidu.com/s?wd=' + question)

#根据问题搜索结果计算每个选项出现的次数
def words_count(question,answers):
    print "根据词频:"
    req = requests.get(url='http://www.baidu.com/s', params={'wd': question})
    body = req.text
    counts = []
    for answer in answers:
        num = body.count(answer)
        counts.append(num)
        print answer + " ---> " + str(num)
    return counts;

#计算问题＋每个选项搜索的结果数
def search_count(question,answers):
    print "根据结果数量："
    counts = []
    for answer in answers:
        req = requests.get(url='http://www.baidu.com/s', params={'wd': question +"%20"+answer})
        body = req.text
        start = body.find(u'百度为您找到相关结果约') + 11
        body = body[start:]
        end = body.find(u"个")
        num = body[:end]
        num = num.replace(',', '')
        counts.append(num)
        print answer + " ---> " + str(num)
    return counts

#找到最符合的
def find_max(counts):
    flag = 0
    max = counts[flag]
    for i in range(0,len(counts)):
        if(int(counts[i]) >= int(max)):
            flag = i;
            max = counts[i]
    return flag;

#找到最不符合的
def find_min(counts):
    flag = 0
    min = counts[flag]
    for i in range(0,len(counts)):
        if(int(counts[i]) <= int(min)):
            flag = i;
            min = counts[i]
    return flag;

#判断结果是否重复
def has_repeat(counts,num):
    sum = 0;
    for count in counts:
        if count == counts[num] or count == 0:
            sum = sum + 1;
    return sum
