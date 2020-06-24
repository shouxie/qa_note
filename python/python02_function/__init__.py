# -*- coding:utf-8 -*-
#@Time : 2020/4/3 下午6:33
#@Author: 手写
#@File : __init__.py.py
import random


def random_fun(num):
    for i in range(num):
        ran = random.randint(1,10)
        print(ran)
random_fun(5)


def check_type(var1):
    print(isinstance(var1, int))
check_type(1)


# print(enumerate({1,2,3}))
for i, index in enumerate({1,2,3}):
    print(i, index)
# 0 1
# 1 2
# 2 3

def add(name, *a):
    print(name, a)
    sum = 0
    for i in a:
        sum += i
    print(sum)

add(1,2) # 1 (2,)

def add0(a=1,b=2):
    print(a,b)
add0(b=3) # 1 3
dict0 = {'01': 'python', '02': 'javascript', '03': 'java'}
def add1(**a):
    print(a)
add1() # {}
add1(a=1,b=2) # {'a': 1, 'b': 2}
# add1({'a':'1', 'b': '2'}) # TypeError: add1() takes 0 positional arguments but 1 was given
# 这种情况，相当于，先拆包把{'a':'1','b':'2'}变成a=1,b=2，再装包，把a=1,b=2 改成字典
add1(**{'a':'1','b':'2'}) # {'a': '1', 'b': '2'}

def func(a,b,*c,**d):
    print(a,b,c,d)
func(1,2) # 1 2 () {}
func(1,2,3,4) # 1 2 (3, 4) {}
func(1,2,[1,2]) # 1 2 ([1, 2],) {}
# list1 = [1,2,3]
def test(a,b=1,c=2,*d,**e):
    print(a,b,c,d,e)
test(1,2,x=1) #  1 2 2 () {'x': 1}
# test(1,2,a=1) # TypeError: test() got multiple values for argument 'a'   不能重复，第一个参数是a
test(1,c=10,b=2) # 1 2 10 () {}
test(1,*[12,13,14]) # ----> 1,12,13,14  print ---> 1 12 13 (14,) {}

# def参数：可变参数，关键字参数 原理：拆包和装包
# 列表和元组 *
# 字典和key=value **
def func1(*tuple1):
    if len(tuple1):
        for i in tuple1:
            print('{}:'.format(i))
    else:
        pass
func1(*[1,2,3])
# 1:
# 2:
# 3:
dict0 = {'01': 'python', '02': 'javascript', '03': 'java'}
def func2(**dict):
    values = dict.values()
    if (len(values)):
        for i in values:
            print('format print: %s' % i)
            print('format print:{}'.format(i))
# func2(**dict0)
# format print: python
# format print:python
# format print: javascript
# format print:javascript
# format print: java
# format print:java

def func2():
    return 'hello'
# print(func2())

#   案例

# def fun1():
#     return 'hello'

name = 'qpp'
def fun1():
    print(name)

fun1() # qpp
def fun2():
    name = 'qpp1' # 同名变量
    print(name)
fun2() # qpp1

def fun3():
    global name
    name = name + 'hello'
    print(name)
fun3() # qpphello
print(name) # qpphello

global_var = 1
def func1():
    n = 100
    list0 = [1,2,3]
    def func2():
        global global_var
        nonlocal n
        n += 100
        global_var += 100
        for index,item in enumerate(list0):
            list0[index] = list0[index] + n
    func2()
    print(list0, n, global_var) # [201, 202, 203] 200 101
    print(locals()) # {'func2': <function func1.<locals>.func2 at 0x1021400d0>, 'list0': [201, 202, 203], 'n': 200}
func1()
print(globals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10dfaf730>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python02_function/__init__.py', '__cached__': None, 'random': <module 'random' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/random.py'>, 'random_fun': <function random_fun at 0x10e027820>, 'check_type': <function check_type at 0x10e084d30>, 'i': 2, 'index': 3, 'add': <function add at 0x10e084dc0>, 'add0': <function add0 at 0x10e084e50>, 'dict0': {'01': 'python', '02': 'javascript', '03': 'java'}, 'add1': <function add1 at 0x10e084ee0>, 'func': <function func at 0x10e084f70>, 'test': <function test at 0x10e086040>, 'func1': <function func1 at 0x10e0863a0>, 'func2': <function func2 at 0x10e0861f0>, 'name': 'qpphello', 'fun1': <function fun1 at 0x10e086160>, 'fun2': <function fun2 at 0x10e086280>, 'fun3': <function fun3 at 0x10e086310>, 'global_var': 101}
print('*'*20)
def func3(a, b):
    c = 10
    def func_inner():
        return a + b + c
    print(locals())
    return func_inner
x = func3(1,2)
print(func3(1,2)) # {'func_inner': <function func3.<locals>.func_inner at 0x100e72430>, 'a': 1, 'b': 2, 'c': 10}
print(x,x()) # {'func_inner': <function func3.<locals>.func_inner at 0x108512430>, 'a': 1, 'b': 2, 'c': 10}  <function func3.<locals>.func_inner at 0x108512430> 13
'''
先声明一个函数，函数中声明一个内部函数，返回值是内部函数
x = func3(1,2) 相当于x = func_inner
print(x) 相当于print(func3(1,2)) 执行func3，会打印里面的print
print(x()) x相当于func_inner 即执行x相当于func_inner
'''




# print('func3',func3(1,2)())


print('*'*10)
def func3(number):
    n = 100
    def inner_func():
        nonlocal n
        for i in range(number):
            n += number
        print(n)
    return inner_func
func3(3)()


print('-'*12)

def func4(f):
    n = 100
    def inner_func():
        print(n)
        f()
    return inner_func

def test():
    print('test')
func4(test)() # 100 test
print('==='*12)


# def decorate(f):
#     f()
#     print('hello')
# @decorate
# def house():
#     print('house')
# # house()

def decorate(func):
    n = 100
    print('hello', n)
    def wrapper():
        func()
    return wrapper
    print('--'*6)
@decorate
def house():
    print('-house')
# house()
