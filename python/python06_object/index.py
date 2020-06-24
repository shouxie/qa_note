# -*- coding:utf-8 -*-
#@Time : 2020/4/21 下午4:19
#@Author: 手写
#@File : index.py

class Person:
    age = ''
    def func(self):
        print(self)
per = Person()
print(per.age)
per.age = 12
print(per.age) # 12
print(per) # <__main__.Person object at 0x10790ca30>
per.func() # <__main__.Person object at 0x109c44a30>
print('**'*30)

# 对象方法和类方法
class Person:
    def func(self):
        print(self)
        print('self name',self.name)

tom = Person()
tom.name = 'tom'
print(tom)
tom.func()
#<__main__.Person object at 0x102e380d0>
# <__main__.Person object at 0x102e380d0>
# self name tom

jack = Person()
#jack.name = 'jack'
#jack.func() # AttributeError: 'Person' object has no attribute 'name'

print('**'*30)

'''
创建对象，开辟一块内存空间，如果有__init__，执行__init__里面内容，把空间地址赋给对象，如果没有，直接把空间地址赋给对象
魔术方法：__init__ 
'''

class Person:
    def __init__(self):
        print(self)
        self.name = ''
    def eat(self):
        print('{} eating'.format(self.name))

jack = Person()  # <__main__.Person object at 0x104213640> 创建对象，有__init__，执行__init__里面的内容
jack.eat()  # eating
jack.name = 'jack'
jack.eat()  # jack eating

print('**'*30)

# __init__ 传参数，普通方法传参, 对象的普通方法可以掉对象的普通方法

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self, food):
        print('{} is eatting {}'.format(self.name, food))

    def run(self, food):
        self.eat(food)
        print('{} is running'.format(self.name))

jack = Person('jack', 18)
jack.run('apple')
# jack is eatting apple
# jack is running


# 类方法
'''
 特点:
  1. 定义需要依赖装饰器@classmethod
  2. 类方法中参数不是一个对象，而是类
     print(cls)  # <class '__main__.Dog'>
  3. 类方法中只可以使用类属性
  4. 类方法中可否使用普通方法？  不能

类方法作用:
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作(功能)

'''


class Dog:

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self   对象
        print('{}在院子里跑来跑去!'.format(self.nickname))

    def eat(self):
        print('吃饭。。。。。')
        self.run()  # 类中方法的调用，需要通过self.方法名()

    @classmethod
    def test(cls):  # cls  class
        print('----------')
        print(cls)  # <class '__main__.Dog'>
        # self.run()
        # print(cls.nickname)   报错
        # print(self.nickname)


Dog.test()

# d = Dog('大黄')
#
# d.run()  # 调用run
#
# d.test()
print('*'*30)

class Person:
    @classmethod
    def setName(cls):
        print(cls)
        # print(cls.name)  # AttributeError: type object 'Person' has no attribute 'name' cls 指的是类，类里面没有name属性

    def __init__(self):
        self.name = 'jack'

jack = Person()
print(jack.name)  # jack
jack.setName()    # <class '__main__.Person'>

Person.setName()  # <class '__main__.Person'>

print('*'*30)

class Person:
    __age = 18

    @classmethod
    def setAge(cls):
        cls.__age = 20

    @classmethod
    def showAge(cls):
        print(cls.__age)

p = Person()
# print(p.__age) # AttributeError: 'Person' object has no attribute '__age'
p.setAge()
p.showAge() # 20
