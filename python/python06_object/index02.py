# -*- coding:utf-8 -*-
#@Time : 2020/4/24 下午1:03
#@Author: 手写
#@File : index02.py

class Person:

    def __init__(self, age):
        self.__age = age

    # __age = ''

    def setAge(self):
        self.__age = 20

    def getAge(self):
        return self.__age

p = Person(19)
p.setAge()
print(p.getAge()) # 20

print(dir(Person)) # ['_Person__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getAge', 'setAge']

print(dir(p)) # ['_Person__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getAge', 'setAge']


print(p._Person__age) # 20
# print(p.__age) #  创建的对象访问不了类中的私有属性__age  AttributeError: 'Person' object has no attribute '__age'

# print(Person.__age)
print('*'*30)

class Person:
    def __init__(self, age):
        if (age > 10):
            self.__age = age
        else:
            self.__age = 10

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


p = Person(12)
print(p.age) # 12

p1 = Person(10)
print(p1.age) # 10

p2 = Person(100)
p2.age = 99
print(p2.age) # 99

print(Person.age) # <property object at 0x10e3e3b80>

Person.age = 20
print(Person.age) # 20
'''
要想对象直接修改属性：p2.age = 99 需要加set
'''