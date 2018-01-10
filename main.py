#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils
import json
import solve_utils
import config


#识别文字
words = img_utils.spot()['words_result'];
question = '';
answer = [];
flag = 1;

#问题
if len(words) == 4:
    question = words[0]['words'];
elif len(words) == 5:
    question = words[0]['words'] + words[1]['words'];
    flag = 2;
question = question.replace("?","")
print u"问题 ：" + question;

#选项
for i in range(flag,len(words)):
    answer.append(words[i]['words'])
    print u"选项" + str(i - flag + 1) + u" : " +answer[i - flag]

#判断否定
is_min = (question.find(u"不") != -1)

#两种方式进行判断
r1 = solve_utils.words_count(question,answer)
r2 = solve_utils.search_count(question,answer)

#根据两种方式的结果选出最佳答案
select1 = 0;
select2 = 0;
if is_min == False:
    select1 = solve_utils.find_max(r1)
    select2 = solve_utils.find_max(r2)
else:
    print u"注意否定"
    select1 = solve_utils.find_min(r1)
    select2 = solve_utils.find_min(r2)

if select1 == select2:
    print u"推荐答案为 " + answer[select1]
else:
    if solve_utils.has_repeat(r1,select1) > 1:
        temp = select1
        select1 = select2
        select2 = temp
    print u"推荐答案：" + answer[select1]
    print u"参考答案：" + answer[select2]
