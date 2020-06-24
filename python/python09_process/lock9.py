# -*- coding:utf-8 -*-
#@Time : 2020/4/30 上午11:21
#@Author: 手写
#@File : lock9.py
import threading
from time import sleep

lock = threading.Lock()

def task1():
    lock.acquire()
    print('---------> task1 start')
    sleep(2)
    print('---------> task1 end')
    lock.release()

def task2():
    lock.acquire()
    print('---------> task2 start')
    sleep(1)
    print('---------> task2 end')
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()

'''
不加lock:运行结果：
---------> task1 start
---------> task2 start
---------> task2 end
---------> task1 end
加lock:运行结果：
---------> task1 start
---------> task1 end
---------> task2 start
---------> task2 end
'''