# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午2:04
#@Author: 手写
#@File : index.py

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
from food import *

p = Person('jack')
apple = Food('apple')
p.eat(apple)
'''
jack is eating apple
'''
print('*'*30)

# import module
# from module import func, Person, module
# print(module.module)
#
# p = module.Person('jack')
#
# module.func(1,2,3)
'''
运行结果
module
1
----------> person init
func (1, 2, 3) 1 2 3
'''

# from module import func, Person, module
from module import *
# print(module)
p = Person('qpp')
func(1,2,3, 4)
'''
运行结果
module
1
----------> person init
func (1, 2, 3, 4) 1 2 3 4
'''

import sys

print(sys.path)
'''
['/Users/qpp/important/project/daling-work-mark/xxxxxxx/python/python07_modules', '/Users/qpp/important/project/daling-work-mark/xxxxxx', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']

'''
print(sys.version) # [Clang 6.0 (clang-600.0.57)]
print(sys.argv)  # 运行程序时的参数，argv是一个列表