
# 面向对象
```python
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
```
使用类创建对象
对象=类()
### 属性
类属性和对象属性
### 方法

#### 普通方法
格式：
def 方法名(self):
  print(self) # 指对象

#### 类方法

 特点:
  1. 定义需要依赖装饰器@classmethod
  2. 类方法中参数不是一个对象，而是类
     print(cls)  # <class '__main__.Dog'>
  3. 类方法中只可以使用类属性
  4. 类方法中可否使用普通方法？  不能

类方法作用:
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作(功能)


类的属性私有化：
在属性名前面加__
```python
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
```


@classmethods
def func(cls):
  print(cls) # 指类

```python
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
        print(cls.name)  # AttributeError: type object 'Person' has no attribute 'name' cls 指的是类，类里面没有name属性

    def __init__(self):
        self.name = 'jack'

jack = Person()
print(jack.name)  # jack
jack.setName()    # <class '__main__.Person'>

Person.setName()  # <class '__main__.Person'>

```


#### 静态方法

装饰器 @staticmethod
静态方法不需要传递参数（self，cls）
只能访问类的属性和方法，对象的是无法访问的
加载时机同类方法


总结:
类方法  静态方法
不同：
  1. 装饰器不同
  2. 类方法是有参数的，静态方法没有参数

相同:
  1. 只能访问类的属性和方法，对象的是无法访问的
  2. 都可以通过类名调用访问
  3. 都可以在创建对象之前使用，因为是不依赖于对象

普通方法 与 两者区别:
不同:
   1. 没有装饰器
   2. 普通方法永远是要依赖对象，因为每个普通方法都有一个self
   3. 只有创建了对象才可以调用普通方法，否则无法调用。


#### 魔术方法

1. \__new__ # 申请内存时候调用，实例化调用 触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
2. \__init__ # 初始化调用，分配内存之后 触发时机： 在实例化对时触发
3. \__call__  # 把对象当作函数时调用，可传参，会默认调用此函数中东西 触发时机: 将对象当成函数使用的时候，会默认调用此函数中内容
4. \__call__ # delete的缩写 析构魔术方法 触发时机：当对象没有用（没有任何变量引用）的时候被触发
5. \__str__： 触发时机： 打印对象名 自动触发去调用__str__里面的内容 注意： 一定要在__str__方法中添加return，return后面内容就是打印对象看到内容
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/22 下午5:53
#@Author: 手写
#@File : methods.py

# 魔术方法

class Person:
    def __init__(self):
        print('---------> init')

    def __new__(cls):
        print('--------------> cls')

p = Person()

print(p)
# 打印结果
#  --------------> cls
#  None

'''
__new__ 是申请内存
'''

class Person:

    def __init__(self, name):
        self.name = name
        print('----------> init')

    def __new__(cls, *args):
        print('-------------> new')
        addr = object.__new__(cls)
        print('-------->', addr)
        return addr

p = Person('jack')
print(p)
print(p.name)
# 打印结果
# -------------> new
# --------> <__main__.Person object at 0x10b3699a0>
# ----------> init
# <__main__.Person object at 0x10b3699a0>
# jack

### __call__
'''
创建对象：
先执行__new__ 方法，addr = object.__new__(cls) 是申请内存空间，返回这个地址，才能执行__init__方法，创建对象完成
'''
print('*'*30)

p('hello') # 如果没有__call__, TypeError: 'Person' object is not callable
# --------->  call hello




###   __del__
print('*'*30)

import sys

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('-----------> del')

p = Person('jack')
p1 = p
p2 = p
print('-------------> p1:name',p1.name)  # 打印结果:-------------> p1:name jack

print('-------------> p2:name', p2.name)  # 打印结果:-------------> p2:name jack

p1.name = 'tom'
print('----->p \'s name is {}, ----->p1 \'s name is {}, ----->p2 \'s name is {}'.format(p.name, p1.name,p2.name))
# 打印结果:----->p 's name is tom, ----->p1 's name is tom, ----->p2 's name is tom

print(sys.getrefcount(p))
# 打印结果:4    解释： 为啥是4呢，因为p,p1,p2 都引用了p的内存地址，最后还打印了一下

#  打印结果: -----------> del   解释： 为啥最后打印了del呢，因为python解释器在代码执行结束会回收内存

del p1

print(sys.getrefcount(p))

del p2
print(sys.getrefcount(p))



print('hello')

#  打印结果: 先打印的hello，再打印的del     解释： 为啥最后打印了del呢，因为python解释器在代码执行结束会回收内存
# 4
# 3
# 2
# hello
# -----------> del


del p
# print(sys.getrefcount(p))  # 报错,因为把p删掉了

print('hello-------->end')

#  打印结果: 先打印的del，再打印的hello     解释： del 打印的时机是引用的地址被回收的时候打印，这个时候删除了p，这个地址也没了，所以会触发del
# -----------> del
# hello-------->end


#  __str__：
# 触发时机： 打印对象名 自动触发去调用__str__里面的内容
# 注意： 一定要在__str__方法中添加return，return后面内容就是打印对象看到内容

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名是:' + self.name + ',年龄:' + str(self.age)


p = Person('tom', 18)
print(p)

# 单纯打印对象名称，出来的是一个地址。地址对于开发者来书没有太大意义
# 如果想在打印对象名的时候能够给开发者更多一些信息量，

p1 = Person('jack', 20)
print(p1)



'''
总结：魔术方法
重点：
__init__ （构造方法，创建完空间之后调用的第一个方法）， __str__

了解:
__new__ 作用  开辟空间  

__del__ 作用  没有指针引用的时候会调用。99%都不需要重写

__call__  作用： 想不想将对象当成函数用。


大总结：
方法：
  普通方法  ---》 重点
      def 方法名(self,[参数]):
          方法体
          
      对象.方法()
      
      方法之间的调用：
      class A:
        def a(self):
            pass
        def b(self):
            # 调用a方法
            self.a()
  
  类方法: 
      @classmethod 
      def 方法名(cls,[参数]):
          pass
          
      类名.方法名()
      对象.方法名()
  
  静态方法: 
      @staticmethod
      def 方法名([参数]):
              pass
              
      类名.方法名()
      对象.方法名()
      
  魔术方法:
    自动执行方法
    
    print(p)  ---> __str__

'''
```
