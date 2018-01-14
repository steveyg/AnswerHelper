#!/usr/bin/python
# -*- coding: utf-8 -*-

import solve_utils
import problem_utils
import config
import time

time_start = time.time()

question, answers = problem_utils.get_result()

print(u"问题 ：" + question)
# 选项
for i in range(0, len(answers)):
    print(u"选项" + str(i + 1) + u" : " + answers[i])

if config.OPEN_BROWSER:
    solve_utils.open_wabpage(question)

# 判断否定
is_opposite = (question.find(u"不") != -1)

# 两种方式进行判断
words_count = solve_utils.words_count(question, answers)
search_count = solve_utils.search_count(question, answers)
print(u'%-15s' * 3 % (u'', u'词频', u'结果数'))
for answer, word_count, search_num in zip(answers, words_count, search_count):
    print(u'%-15s' * 3 % (answer, word_count, search_num))

# 根据两种方式的结果选出最佳答案
select1 = 0
select2 = 0
if is_opposite:
    print(u"注意否定")
    select1 = solve_utils.find_min_index(words_count)
    select2 = solve_utils.find_min_index(search_count)
else:
    select1 = solve_utils.find_max_index(words_count)
    select2 = solve_utils.find_max_index(search_count)

if select1 == select2:
    print(u"推荐答案为 " + answers[select1])
else:
    print(u'推荐答案：%s  参考答案：%s' % ((answers[select2], answers[select1])
          if solve_utils.has_repeat(words_count, select1) > 1 else (answers[select1], answers[select2])))
print(u'耗时：%s s' % (time.time() - time_start))
