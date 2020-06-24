
### 函数
参数：



格式：
def 函数名(参数):
  函数体
```python
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
```
#### 可变参数
依照：拆包与解包
不可变参数需要放到可变参数前面
```python
def add(name, *a):
    print(name, a)
    sum = 0
    for i in a:
        sum += i
    print(sum)

add(1,2) # 1 (2,)
```

#### 关键字参数
```python
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


def test(a,b=1,c=2,*d,**e):
    print(a,b,c,d,e)
test(1,2,x=1) #  1 2 2 () {'x': 1}
test(1,2,a=1) # TypeError: test() got multiple values for argument 'a'   不能重复，第一个参数是a
test(1,c=10,b=2) # 1 2 10 () {}

test(1,*[12,13,14]) # ----> 1,12,13,14  print ---> 1 12 13 (14,) {}
```
总结：
```python
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
```

#### return 返回值

#### 函数嵌套

#### 全局变量 局部变量
global
全局变量如果是不可变，在函数中修改需要加global，如果是可变的，不需要加

```python
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
```

#### 内部函数
可以访问外部函数的变量
可以修改外部的可变变量
修改不可变变量需要在内部函数加nonlocal关键字
修改全局的不可变量需要在内部函数加global关键字
locals() # 查看内部函数的东西 字典形式输出
global() # 查看全局 字典形式输出
```python
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

```

#### 闭包
在函数中提供的概念

1. 外部函数中定义了内部函数
2. 外部函数有返回值
3. 返回值是内部函数名
4. 内部函数引用了外部函数的变量
```python
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
```

在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
并且把里面的函数返回，我们把这种情况叫闭包

修改外部函数的可变类型局部变量可不加nonlocal
修改外部函数的不可变类型局部变量要加 nonlocal

闭包有什么缺点呢？
闭包的缺点1，作用域没有那么直观
闭包的缺点2，因为变量不会被垃圾回收所以有一定的内存占用问题。

闭包作用：1.可以使用同级的作用域
闭包作用：2.读取其他元素的内部变量
闭包作用：3.延长作用域


闭包总结
1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成.
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存.
3.闭包的好处，使代码变得简洁，便于阅读代码。
4.闭包是理解装饰器的基础

#### 装饰器
函数A作为参数传递给另一个函数B
要有闭包的特点
```python
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








def func4(f):
    n = 100
    def inner_func():
        print(n)
        f()
    return inner_func

def test():
    print('test')
func4(test)() # 100 test

print('='*20)


def decorate(f):
    f()


@decorate
def house():
    print('house')
house()


import time

def test():
    time.sleep(2)
    print('test is running')

def deco(func):
    start = time.time()
    func()
    stop = time.time()
    print(stop-start)
deco(test)
# test is running
# 2.0023510456085205


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



# 装饰器带参数
'''
带参数的装饰器是三层的
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器的内容
'''


def outer(a):  # 第一层： 负责接收装饰器的参数
    print('------------1 start')

    def decorate(func):  # 第二层 ： 负责接收函数的
        print('------------2 start')

        def wrapper(*args, **kwargs):  # 第三层   负责接收函数的参数
            func(*args)
            print("---->铺地砖{}块".format(a))

        print('------------2 end')
        return wrapper  # 返出来的是：第三层

    print('------------1 end')
    return decorate  # 返出来的是：第二层


@outer(10)
def house(time):
    print('我{}日期拿到房子的钥匙,是毛坯房....'.format(time))


# @outer(100)
# def street():
#     print('新修街道名字是：黑泉路')


house('2019-6-12')

# street()

```


LEGB：
local 本地
enclosing 嵌套
global 全局
built-in 内置

#### 匿名函数
简化函数定义
格式： lambda 参数... : 函数体
```python
print('*'*20)
s = lambda a,b:a+b
print(s(1,2))
```
匿名函数作为参数
```python
def func(a,b,func):
    print(a,b,func)
    s = func(a,b)
    print(s)

func(1,2,lambda x,y:x+y)
# 1 2 <function <lambda> at 0x11010df70>
# 3
```
匿名函数与内置函数结合

- max
> 函数功能为取传入的多个参数中的最大值，或者传入的可迭代对象元素中的最大值
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
key---可做为一个函数，用来指定取最大值的方法。
default---用来指定最大值不存在时返回的默认值。
arg1---字符型参数/数值型参数，默认数值型
```python
print(max(1,2,3,4,5)) # 5
print(max([1,2,3,4,5])) # 5

persons = [{'name':'111','age':18},{'name':'222', 'age': 20}, {'name': '333', 'age': 21}]
print(max(persons, key=lambda obj: obj['age'])) # {'name': '333', 'age': 21}
```

- map
> map(function,iterable,...)
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list

```python
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

# 列表中奇数加1，偶数不变
myList = [1,2,3,4,5,6]
result = map(lambda item: item+1 if item % 2 else item, myList)
print(list(result)) # [2, 2, 4, 4, 6, 6]
```
- reduce
reduce(function,iterable,[,initializer])
> reduce函数与map函数有不一样地方，map操作是并行操作，reduce函数是把多个参数合并的操作，也就是从多个条件简化的结果，在计算机的算法里，大多数情况下，就是为了简单化。比如识别图像是否是一只猫，那么就是从众多的像素里提炼出来一个判断：是或否。可能是几百万个像素，就只出来一个结果。
在GOOGLE大规模集群里，就是利用这个思想，把前面并行处理的操作叫做map，并行处理之后的结果，就需要简化，归类，把这个简化和归类的过程就叫做reduce。
由于reduce只能在一台主机上操作，并不能分布式地处理，但是reduce处理的是map结果，那么意味着这些结果已经非常简单，数据量大大减小，处理起来就非常快。
因此可以把mapreduce过程叫做分析归纳的过程。

function: 函数，有两个参数
interable: 可迭代对象
initializer: 初始化值，可选
```python
# reduce
from functools import reduce
x = reduce(lambda item1, item2: item1+item2, myList)
print(x) # 21

tuple1 = (1,)
x = reduce(lambda x,y:x-y, tuple1, 10)
print(x) # 9
```

- filter
```python
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
```
- sorted
```python
persons = [
    {'name': '111', 'age': 10},
    {'name': '222', 'age': 11},
    {'name': '333', 'age': 12},
    {'name': '444', 'age': 13}
]
# sorted 
print(sorted(persons, key=lambda item : item['age'])) # [{'name': '111', 'age': 10}, {'name': '222', 'age': 11}, {'name': '333', 'age': 12}, {'name': '444', 'age': 13}]
```
#### 递归函数
> 自己调用自己，设终点
```python
def getSum(n):
    if n == 0:
        return 0
    else:
        return n + getSum(n-1)
print(getSum(10)) # 55
```
