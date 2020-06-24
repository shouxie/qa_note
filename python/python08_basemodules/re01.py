# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午6:31
#@Author: 手写
#@File : re01.py

import re
msg = 'hello world'

result = re.compile('world')
print(result.match(msg)) # None

result1 = re.compile('hello')
print(result1.match(msg)) # <re.Match object; span=(0, 5), match='hello'>


result = re.match('hello', msg)
print(result) # <re.Match object; span=(0, 5), match='hello'>
result = re.search('hello', msg)
print(result) # <re.Match object; span=(0, 5), match='hello'>
res = re.search('world', msg)
print(res) # <re.Match object; span=(6, 11), match='world'>

print(res.span()) # 返回位置 (6, 11)
print(res.group()) # 使用group提取到匹配的内容 world

print('*'*30)

print(re.search('[0-9][a-z]', '10a000000f')) # <re.Match object; span=(1, 3), match='0a'>

print(re.findall('[0-9][a-z]', '10a000000f')) # ['0a', '0f']

# a7a  a88a a7878a
msg = 'a7aopa88akjgka7878a'
print(re.findall('[a-z][0-9]+[a-z]',msg))  # ['a7a', 'a88a', 'a7878a']

# qq号码验证 5~11 开头不能是0
qq = '14944689962'
print(re.findall('^[1-9][0-9]{4,10}$', qq)) # ['14944689962']

# 用户名可以是字母或者数字_， 不能是数字开头，用户名长度必须6位以上 [0-9a-zA-Z]

rep = '[a-z]'