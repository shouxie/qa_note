<!--
 * @Author: shouxie
 * @Date: 2020-04-26 16:17:58
 * @Descriptio
 -->
## 单例模式


一般情况下，每次创建一个对象就会分配一个地址空间,单例模式保证只有一个地址空间存储对象
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/26 下午4:31
#@Author: 手写
#@File : index01_单例模式.py

class Person:

    __addr = None

    def __new__(cls):

        if cls.__addr is None:
            cls.__addr = object.__new__(cls)
            return cls.__addr

        else:
            return cls.__addr

p = Person()
p1 = Person()
print(p, p1)  # 执行结果：<__main__.Person object at 0x109625190> <__main__.Person object at 0x109625190>
```

## 模块

在python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件（.py）就是一个模块（module），
模块名就是文件名去掉后缀py。
这样做的好处是：
- 提高代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
- 解决了命名冲突，不同模块中相同的命名不会冲突

常用标准库：

| 标准库          | 说明                 |
| --------------- | -------------------- |
| builtins        | 内建函数默认加载     |
| math            | 数学库               |
| random          | 生成随机数           |
| time            | 时间                 |
| datetime        | 日期和时间           |
| calendar        | 日历                 |
| hashlib         | 加密算法             |
| copy            | 拷贝                 |
| functools       | 常用的工具           |
| os              | 操作系统接口         |
| re              | 字符串正则匹配       |
| sys             | Python自身的运行环境 |
| multiprocessing | 多进程               |
| threading       | 多线程               |
| json            | 编码和解码 JSON 对象 |
| logging         | 记录日志，调试       |

1. 自定义模块
2. 使用系统一些模块

导入模块:
1. import 模块名
    模块名.变量    模块名.函数    模块名.类
2. from 模块名 import 变量 | 函数 | 类
    在代码中可以直接使用变量，函数，类
3. from 模块名 import *
   该模块中所有的内容
   但是如果想限制获取的内容，可以在模块中使用__all__=[使用*可以访问到内容]
4. 无论是import还是from的形式，都会将模块内容进行加载
   如果不希望其进行调用。就会用到__name__
   在自己的模块里面__name__叫： __main__
   如果在其他模块中通过导入的方式调用的话：__name__: 模块名

```python
# module.py


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


########################################
import module
print(module.module)

p = module.Person('jack')

module.func(1,2,3)
'''
运行结果
module
1
----------> person init
func (1, 2, 3) 1 2 3
'''
#--------------------------------#
from module import func, Person, module
# from module import *
print(module)
p = Person('qpp')
func(1,2,3, 4)
'''
运行结果
module
1
----------> person init
func (1, 2, 3, 4) 1 2 3 4
'''


# 如果在module.py 里面加上
__all__ = ['Person', 'func']
# 报错：NameError: name 'module' is not defined
```
## 搜索路径
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

### sys模块
```python

import sys

print(sys.path)
'''
['/Users/qpp/important/project/daling-work-mark/xxxxxxx/python/python07_modules', '/Users/qpp/important/project/daling-work-mark/xxxxxx', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']

'''
print(sys.version) # [Clang 6.0 (clang-600.0.57)]
print(sys.argv)  # 运行程序时的参数，argv是一个列表
```
## 包 package

文件夹 包
非py文件  包：py文件
一个包中可以存放多个模块。
项目  > 包 > 模块 > 类  函数  变量

##### 格式：
from 包 import 模块
from 包.模块 import 类|函数|变量
from 包.模块 import *

```python

'''
food
     |--test.py
     |--__init__.py
     |-- ....
  user
     |-- test.py
     |--__init__.py
     ...
  index.py

'''
# from user.test import *
from user.test import Person
from food.test import *

p = Person('jack')
apple = Food('apple')
p.eat(apple)
'''
jack is eating apple
'''
```

## __init__.py文件

当导入包的时候，默认调用__init__.py文件
作用:
1. 当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
2. 此文件中函数，变量等的访问，只需要通过：包名.函数....
3. 结合__all__=[通过* 可以访问的模块]

from 模块 import *    表示可以使用模块里面的所有内容，如果没有定义__all__所有的都可以访问，
                       但是如果添加上了__all__,只有__all__=['',''] 列表中可以访问的

from 包 import *   表示该包中内容（模块）是不能访问，就需要在__init__.py文件中定义__all__ =[可以通过*访问的模块]

## 循环导入

循环导入：大型的python项目中，需要很多python文件，由于架构不当，可能会出现模块之间的相互导入
   A：模块
     def test():
        f()
   B: 模块
     def f（）：
        test()

  避免产生循环导入：
  1. 重新架构
  2. 将导入的语句放到函数里面
  3. 把导入语句放到模块的最后

```python
#  循环导入2.py
def func():
    print('-------循环导入2里面func----1---------')
    from 循环导入1 import task1
    task1()
    print('-------循环导入2里面func------2-------')

###############################
from 循环导入2 import func


def task1():
    print('-------task1-------')


def task2():
    print('--------task2---------')
    func()


#
if __name__ == '__main__':
    # 调用task1
    task1()
    task2()
```