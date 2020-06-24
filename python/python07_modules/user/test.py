# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午2:04
#@Author: 手写
#@File : test.py


class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{} is eating {}'.format(self.name, food.name))