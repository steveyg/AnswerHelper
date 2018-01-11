#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils
import json
import solve_utils
import config
import problem_utils

result = problem_utils.get_result()
question = result[0]
answer = result[1]

print u"问题 ：" + question;
#选项
for i in range(0,len(answer)):
    print u"选项" + str(i + 1) + u" : " +answer[i]

solve_utils.open_wabpage(question)

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
