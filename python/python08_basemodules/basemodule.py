# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午5:28
#@Author: 手写
#@File : basemodule.py

# chr  ord


# ord： str ---》Unicode码
str = 'hello world'
# print(ord(str)) # TypeError: ord() expected a character, but string of length 11 found

print(ord('h')) # 104

print(ord('你')) # 20320

# chr: # Unicode码 ---》 str

print(chr(20320)) # 你

# print()  input()  list()  str()  set()  dict()  tuple()
# int()  chr() ord()  bin()  hex()  oct()  isinstance()