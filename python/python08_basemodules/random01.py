# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午4:28
#@Author: 手写
#@File : random01.py

import random

# 0~1之间的随机小数
print('0~1之间的随机小数', random.random())
# 随机范围 randrange(start, end, step) 不包含end
print('随机范围，randrange', random.randrange(2, 10, 2))
# randint 包含end
print('randint', random.randint(1, 10))


list0 = [1,2,3,4]
# 随机选择列表的内容
print('random.choice', random.choice(list0))
# 打乱顺序
l = random.shuffle(list0)
print('l:',l,'list0:', list0)