# -*- coding:utf-8 -*-
#@Time : 2020/4/26 上午10:28
#@Author: 手写
#@File : index04extends.py

'''
继承：
  Student，Employee  ---》 都属于人类
  相同代码 ---》 代码冗余，可读性不高

  将相同代码提取----》Person类
    Student，Employee  ---》 继承Person

    class Student(Person):
        pass

 特点:
   1. 如果类中不定义__init__，调用父类 super class的__init__
   2. 如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
   3. 如何调用父类__init__:
       super().__init__(参数)
       super(类名,对象).__init__(参数)
    4. 如果父类有eat(),子类也定义一个eat方法，默认搜索的原则：先找当前类，再去找父类
       s.eat()
       override： 重写（覆盖）
       父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5.子类的方法中也可以调用父类方法：
       super().方法名(参数)

'''
class Person:
    def __init__(self):
        print('person init')

    def eat(self):
        print('------------> person eat')

class Student(Person):
    def __init__(self):
        print('student init')
        super().__init__()

s = Student()
'''
运行结果：
student init
person init
'''


print('*'*30)
# 类，传参问题  super()  父类对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{} is eatting food, he is {}'.format(self.name,self.age))

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

class employee(Person):
    pass

s = Student('jack',18)
e = employee('tom', 20)
s.eat()
e.eat()
'''
运行结果：
jack is eatting food, he is 18
tom is eatting food, he is 20
'''
# 不同子类不同参数
'''
# super().__init__(name, age)
  super(Student, self).__init__(name, age)  # super(type, obj) -> bound super object; requires isinstance(obj, type).区别就是多了一步校验isinstance
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('--------->person init')
class Student(Person):
    def __init__(self, name, age, grade):
        # super().__init__(name, age)
        super(Student, self).__init__(name, age)
        self.grade = grade
        print('---------> student init')

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('---------> employee init')

s = Student('jack', 17, 1)
e = Employee('tom', 20, 1000)
'''
运行结果：
--------->person init
---------> student init
--------->person init
---------> employee init
'''
