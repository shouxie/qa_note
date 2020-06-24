# -*- coding:utf-8 -*-
#@Time : 2020/4/29 下午12:07
#@Author: 手写
#@File : queue4.py

from multiprocessing import Queue


# built-in: def __init__(self, maxsize=-1):
q = Queue(5)
# built-in: def put(self, obj, block=True, timeout=None):
# q.put('1')
for i in range(4):
    q.put(str(i))

# print(q.qsize())
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.full())
print(q.empty())
q.get_nowait()

'''
NotImplementedError
 # Raises NotImplementedError on Mac OSX because of broken sem_getvalue()
'''