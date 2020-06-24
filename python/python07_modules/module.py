# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午2:08
#@Author: 手写
#@File : module.py


class Person:
    def __init__(self, name):
        self.name = name

        print('----------> person init')


def func(*args):
    print('func',args, *args)

module = 1
print(__name__)
__all__ = ['Person', 'func']