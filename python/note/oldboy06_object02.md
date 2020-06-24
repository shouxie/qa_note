
### 面向对象

> 私有化: 如果想让类的内部属性不被外界直接访问，可以在这个属性的前面加两个下划线__ ,在Python中，如果一个属性的前面出现 __,就表示这个属性只能在当前类的方法中被直接访问，不能通过对象直接访问，这个变量就被称为私有变量
封装: 1. 私有化属性  2.定义公有set和get方法
__属性： 就是将属性私有化，访问范围仅仅限于类中

这种私有化方式相当于伪私有化，因为打印dir 查看对象的属性相当于被私有化的属性伪装成了别的名字，还是能访问到的！

好处：
1. 隐藏属性不被外界随意修改
2. 也可以修改：通过函数
   def setXXX(self,xxx):
3. 筛选赋值的内容
        if xxx是否符合条件
            赋值
        else:
            不赋值
3.如果想获取具体的某一个属性
  使用get函数
    def getXXX(self):
       return self.__xxx


```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/24 下午1:03
#@Author: 手写
#@File : index02.py

class Person:

    def __init__(self, age):
        self.__age = age

    __age = ''

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
```