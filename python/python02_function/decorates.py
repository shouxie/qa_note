# -*- coding:utf-8 -*-
#@Time : 2020/4/11 上午9:24
#@Author: 手写
#@File : decorates.py

import time
def valiteArgs(f):
    print('-'*20)
    print('校验参数starting...')
    # time.sleep(2)
    def inner_valite(*args,**kwargs):
        f(*args,**kwargs)
        print('验证完成...')
        print('-' * 20)
    return inner_valite

@valiteArgs
def render_num(number):
    print('要验证的参数',number)
render_num(5)

@valiteArgs
def render_str(*str):
    print('要验证的参数',list(str))
    for i in str:
        print(i)
render_str('hello wolrd', 'hello python')
@valiteArgs
def render_extra(str='hello world'):
    print('要验证的参数', str)
render_extra(str='hello python')

# 多层装饰器
def decorate1(func):
    print('-'*10,'start1')
    def wrapper():
        func()
        print('decorate1')
    print('-'*10, 'end1')
    return wrapper
def decorate2(func):
    print('-'*10,'start2')
    def wrapper():
        func()
        print('decorate2')
    print('-'*10, 'end2')
    return wrapper
@decorate2
@decorate1
def house():
    print('hello world')
house()
# --------------------
# ---------- start1
# ---------- end1
# ---------- start2
# ---------- end2
# hello world
# decorate1
# decorate2
print('*'*20)
s = lambda a,b:a+b
print(s(1,2))

def func(a,b,func):
    print(a,b,func)
    s = func(a,b)
    print(s)

func(1,2,lambda x,y:x+y)
# 1 2 <function <lambda> at 0x11010df70>
# 3
print('*'*20)
print(max(1,2,3,4,5)) # 5
print(max([1,2,3,4,5])) # 5

persons = [{'name':'111','age':18},{'name':'222', 'age': 20}, {'name': '333', 'age': 21}]
print(max(persons, key=lambda obj: obj['age'])) # {'name': '333', 'age': 21}


# map
list1 = [1,2,3,4,5,6]
s = map(lambda l:l+2, list1)
print(s) # <map object at 0x10e625c40>
print(list(s)) # [3, 4, 5, 6, 7, 8]
list2 = [1,2,3,4,5,6]
s = map(lambda item: item+1, list2)
print(list(s))  # [2, 3, 4, 5, 6, 7]
s = map(lambda x,y:x+y, list1, list2)
print(list(s)) # [2, 4, 6, 8, 10, 12]

s = map(None,[2,4,6],[3,2,1])
print(s)

s = map(int, '1234')
print(list(s))


func = lambda x: x if x % 2 else x + 1
print(func(1)) # 1
print(func(2)) # 3

print('-'*20)
# 列表中奇数加1，偶数不变
myList = [1,2,3,4,5,6]
result = map(lambda item: item+1 if item % 2 else item, myList)
print(list(result)) # [2, 2, 4, 4, 6, 6]

# reduce
from functools import reduce
x = reduce(lambda item1, item2: item1+item2, myList)
print(x) # 21
x = reduce(lambda x,y:x-y,myList)
print(x) # -19
tuple1 = (1,)
x = reduce(lambda x,y:x-y, tuple1, 10)
print(x) # 9

# filter
print(list(filter(lambda x: x> 2, [1,2,3,4]))) # [3, 4]

# 所有年龄大于12的学生
persons = [
    {'name': '111', 'age': 10},
    {'name': '222', 'age': 11},
    {'name': '333', 'age': 12},
    {'name': '444', 'age': 13}
]
l = filter(lambda obj : obj['age']>12, persons)
print(list(l)) # [{'name': '444', 'age': 13}]
# sorted
print(sorted(persons, key=lambda item : item['age'])) # [{'name': '111', 'age': 10}, {'name': '222', 'age': 11}, {'name': '333', 'age': 12}, {'name': '444', 'age': 13}]

print('-'* 20)

def getSum(n):
    if n == 0:
        return 0
    else:
        return n + getSum(n-1)
print(getSum(10)) # 55

open