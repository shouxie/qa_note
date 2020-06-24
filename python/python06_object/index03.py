# -*- coding:utf-8 -*-
#@Time : 2020/4/24 下午3:24
#@Author: 手写
#@File : index03.py

# book student computer
'''
 知识点：
 1. has  a
    一个类中使用了另外一种自定义的类型

    student使用computer  book
2. 类型：
    系统类型：
       str  int  float
       list  dict  tuple  set
    自定义类型：
        算是自定义的类，都可以将其当成一种类型
        s = Student()
        s是Student类型的对象
a = 12 # 是把int类型中的一个12这个对象赋给a
self.book = book # 是把自定义类型Book实例化出来的book对象赋给self.book
'''
class Book:
    def __init__(self, bName, num):
        self.name = bName
        self.number = num

    def __str__(self):
        return '{}本{}书'.format(self.number, self.name)

class Computer:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def __str__(self):
        return '电脑是{}，品牌是{}'.format(self.name, self.brand)

class Student:

    def __init__(self, name, book, computer):
        self.name = name
        self.book = book
        self.computer = computer

    def myHave(self):
        print('{}有{},{}'.format(self.name,self.computer,self.book))


book = Book('盗墓笔记', 10)
computer = Computer('MAC', 'mac pro')
s = Student('zhangsan', book, computer)
s.myHave() # zhangsan有电脑是MAC，品牌是mac pro,10本盗墓笔记书