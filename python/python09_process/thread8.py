# -*- coding:utf-8 -*-
#@Time : 2020/4/29 下午2:29
#@Author: 手写
#@File : thread8.py

import threading

n = 1

def func():
    global n
    for i in range(100000000):
        n += 1
        print(n)

if __name__ == '__main__':
    t1 = threading.Thread(target=func, name='func1')
    t2 = threading.Thread(target=func, name='func2')
    t1.start()
    t2.start()