#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import urllib
import sys
import requests
import re

if sys.version_info.major == 2:
    import urllib as ul
elif sys.version_info.major == 3:
    from urllib import parse as ul
else:
    raise RuntimeError('Unknown python version')

# 直接用浏览器打开问题
def open_wabpage(question):
    webbrowser.open('https://baidu.com/s?wd=' + ul.quote(question.encode(sys.stdout.encoding)))


# 根据问题搜索结果计算每个选项出现的次数
def words_count(question, answers):
    search_page = requests.get(url='http://www.baidu.com/s', params={'wd': question})
    return [search_page.text.count(answer) for answer in answers]


# 计算问题＋每个选项搜索的结果数
def search_count(question, answers):
    counts = []
    for answer in answers:
        search_page = requests.get(url='http://www.baidu.com/s', params={'wd': question + "%20" + answer})
        m = re.search(u'百度为您找到相关结果约((\d+,)*\d+)个', search_page.text)
        if m is not None:
            counts.append(int(m.groups()[0].replace(',', '')))
    return counts


# 找到最符合的
def find_max_index(counts):
    return counts.index(max(counts))


# 找到最不符合的
def find_min_index(counts):
    return counts.index(min(counts))


# 判断结果是否重复
def has_repeat(counts, num):
    return counts.count(counts[num])
