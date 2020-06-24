# -*- coding:utf-8 -*-
#@Time : 2020/4/10 下午7:22
#@Author: 手写
#@File : decorate.py

import time
#
# def test():
#     time.sleep(2)
#     print('test is running')

# def deco(func):
#     start = time.time()
#     func()
#     stop = time.time()
#     print(stop-start)
# deco(test)
# test is running
# 2.0023510456085205

# def deco(func):
#     return func
# t = deco(test)
# t()
# test()
def timer(func):
    def deco():
        start = time.time()
        func()
        stop = time.time()
        print(stop-start)
    return deco
@timer
def test():
    time.sleep(2)
    print('test is running')
# test = timer(test)
# test()