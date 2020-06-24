# -*- coding:utf-8 -*-
#@Time : 2020/4/22 下午5:53
#@Author: 手写
#@File : methods.py

# 魔术方法

class Person:
    def __init__(self):
        print('---------> init')

    def __new__(cls):
        print('--------------> cls')

p = Person()

print(p)
# 打印结果
#  --------------> cls
#  None

'''
__new__ 是申请内存
'''

class Person:

    def __init__(self, name):
        self.name = name
        print('----------> init')

    def __new__(cls, *args):
        print('-------------> new')
        addr = object.__new__(cls)
        print('-------->', addr)
        return addr

    def __call__(self, args):
        print('---------> call', args)

p = Person('jack')
print(p)
print(p.name)
# 打印结果
# -------------> new
# --------> <__main__.Person object at 0x10b3699a0>
# ----------> init
# <__main__.Person object at 0x10b3699a0>
# jack


'''
创建对象：
先执行__new__ 方法，addr = object.__new__(cls) 是申请内存空间，返回这个地址，才能执行__init__方法，创建对象完成
'''


print('*'*30)

p('hello') # 如果没有__call__, TypeError: 'Person' object is not callable
# --------->  call hello

###   __del__
print('*'*30)

import sys

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('-----------> del')

p = Person('jack')
p1 = p
p2 = p
print('-------------> p1:name',p1.name)  # 打印结果:-------------> p1:name jack

print('-------------> p2:name', p2.name)  # 打印结果:-------------> p2:name jack

p1.name = 'tom'
print('----->p \'s name is {}, ----->p1 \'s name is {}, ----->p2 \'s name is {}'.format(p.name, p1.name,p2.name))
# 打印结果:----->p 's name is tom, ----->p1 's name is tom, ----->p2 's name is tom

print(sys.getrefcount(p))
# 打印结果:4    解释： 为啥是4呢，因为p,p1,p2 都引用了p的内存地址，最后还打印了一下

#  打印结果: -----------> del   解释： 为啥最后打印了del呢，因为python解释器在代码执行结束会回收内存

del p1

print(sys.getrefcount(p))

del p2
print(sys.getrefcount(p))



print('hello')

#  打印结果: 先打印的hello，再打印的del     解释： 为啥最后打印了del呢，因为python解释器在代码执行结束会回收内存
# 4
# 3
# 2
# hello
# -----------> del


del p
# print(sys.getrefcount(p))  # 报错,因为把p删掉了

print('hello-------->end')

#  打印结果: 先打印的del，再打印的hello     解释： del 打印的时机是引用的地址被回收的时候打印，这个时候删除了p，这个地址也没了，所以会触发del
# -----------> del
# hello-------->end





