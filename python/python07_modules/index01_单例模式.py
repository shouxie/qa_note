# -*- coding:utf-8 -*-
#@Time : 2020/4/26 下午4:31
#@Author: 手写
#@File : index01_单例模式.py

class Person:

    __addr = None

    def __new__(cls):

        if cls.__addr is None:
            cls.__addr = object.__new__(cls)
            return cls.__addr

        else:
            return cls.__addr

p = Person()
p1 = Person()
print(p, p1)  # 执行结果：<__main__.Person object at 0x109625190> <__main__.Person object at 0x109625190>