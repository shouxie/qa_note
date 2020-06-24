# -*- coding:utf-8 -*-
#@Time : 2020/4/26 上午10:54
#@Author: 手写
#@File : index05多继承extends.py
'''
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
