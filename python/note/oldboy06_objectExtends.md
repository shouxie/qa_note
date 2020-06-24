# 继承

```python
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

```


## 多继承
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/26 上午10:54
#@Author: 手写
#@File : index05多继承extends.py
'''
新式类和经典类：https://www.jianshu.com/p/6f9d99f7ad54
python允许多继承，
 def 子类(父类1，父类2，..):
    pass

inspect模块主要提供了四种用处：

　　1.对是否是模块、框架、函数进行类型检查

　　2.获取源码

　　3.获取类或者函数的参数信息

　　4.解析堆栈
inspect.getmro： 元组形式返回cls类的基类（包括cls类），以method resolution顺序;通常cls类为元素的第一个元素

'''
class P1:
    def foo(self):
        print('p1 foo')

class P2:
    def foo(self):
        print('p2 foo')
    def bar(self):
        print('p2 bar')

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print('c2 bar')

class D(C1, C2):
    pass

d = D()
d.foo()
d.bar()
'''
运行结果：新式类
p1 foo
c2 bar

电脑自带的python2.7 运行结果：经典类
p1 foo
p2 bar
'''
import inspect
print(inspect.getmro(D))  # 等同于 print(D.__mro__)

'''
运行结果：
(<class '__main__.D'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.P1'>, <class '__main__.P2'>, <class 'object'>)
电脑自带的python2.7 运行结果：
(<class __main__.D at 0x102fb0c18>, <class __main__.C1 at 0x102fb0b48>, <class __main__.P1 at 0x102fb0a78>, <class __main__.P2 at 0x102fb0ae0>, <class __main__.C2 at 0x102fb0bb0>)

经典类：
实例d调用foo()时，搜索顺序是 D => C1 => P1

实例d调用bar()时，搜索顺序是 D => C1 => P1 => P2

换句话说，经典类的搜索方式是按照“从左至右，深度优先”的方式去查找属性。d先查找自身是否有foo方法，没有则查找最近的父类C1里是否有该方法，如果没有则继续向上查找，直到在P1中找到该方法，查找结束。

新式类：
实例d调用foo()时，搜索顺序是 D => C1 => C2 => P1

实例d调用bar()时，搜索顺序是 D => C1 => C2

可以看出，新式类的搜索方式是采用“广度优先”的方式去查找属性。
'''

```

## 多态

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/26 下午2:29
#@Author: 手写
#@File : index06.py

'''
 私有化：
    __age
    def __show(self):
        pass

    ---> _类名_属性

  私有化： 封装  将属性私有化，定义公有set和get方法
  def setAge(self,age):
      判断
  def getAge(self):
     return self.__age

  s.setAge(20)
  s.getAge()

  class Student:
      def __init__(self,age):
            self.__age=age

      @property
      def age(self):
        return ...

      @age.setter
      def age(self,age):
        self.__age=age

  s= Student()
  s.age=10
  print(s.age)


 继承：
   has a
   class Student:
     def __init__(self,name,book):
        pass

   is a
    父类   子类
    class Person:
        def run(self):
            ....

    class Student(Person):
        ....

        def study(self):
            ....

        def run(self):
            super().run()
            .....

    s= Student()
    s.study()
    s.run()


    1. __init__
    2. 重写方法

  多继承：（了解）
    class A:
        pass
    class B:
        pass
    class C(A,B):
        pass
    现在执行环境python3

    新式类: 广度优先

    D.__mro__  --->查看搜索顺序
    import inspect
    print(inspect.getmro(D))

'''

#   封装  继承  多态 ----》 面向对象
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat，也可以接收dog，还可以接收tiger
        # isinstance(obj,类)  ---》 判断obj是不是类的对象或者判断obj是不是该类子类的对象
        if isinstance(pet, Pet):
            print('{}喜欢养宠物:{}，昵称是:{}'.format(self.name, pet.role, pet.nickname))
        else:
            print('不是宠物类型的。。。。')


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称:{},年龄:{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠....')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看家高手....')


class Tiger:
    def eat(self):
        print('太可怕了，可以吃人...')


# 创建对象
cat = Cat('花花', 2)

dog = Dog('大黄', 4)

tiger = Tiger()

person = Person('家伟')

person.feed_pet(cat)
person.feed_pet(dog)
print('----------------------------')
person = Person('pengpeng')

person.feed_pet(tiger)

# Pet
#  pet  父类      cat   dog 子类
#  pet  大类型    cat  dog 小类型

```