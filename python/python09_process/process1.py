# -*- coding:utf-8 -*-
#@Time : 2020/4/28 下午3:00
#@Author: 手写
#@File : process1.py

from multiprocessing import Process
# import time
from time import sleep
import os

num = 0
def task1(sec):
    while True:
        global num
        sleep(sec)
        num += 1
        print('-------------> task1, num : {}'.format(str(num)))

def task2():
    global num
    while True:
        sleep(1)
        num += 1
        print('--------------> task2, num:{}'.format(str(num)))

if __name__ == '__main__':
    # built-in: def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
    p1 = Process(target=task1, name='task1', args=(2,))
    p1.start()
    p2 = Process(target=task2, name='task2')
    p2.start()
    # 这里会先输出，因为父进程创建完成，子进程创建完成就干子进程的事了
    # print('-------------->main, main num : {}'.format(str(num)))

    while True:
        sleep(1)
        print('-------------->main, main num : {}'.format(str(num)))


'''
运行的时候会开启一个进程。
运行结果：
-------------->main main 进程号:11495
-------------> task1 task1的进程号是：11497, 父进程是：11495
--------------> task2 task2的进程号是：11498, 父进程是: 11495


-------------->main, main num : 0
--------------> task2, num:1
-------------->main, main num : 0
-------------> task1, num : 1
--------------> task2, num:2
-------------->main, main num : 0
--------------> task2, num:3
-------------->main, main num : 0
-------------> task1, num : 2
--------------> task2, num:4
-------------->main, main num : 0
--------------> task2, num:5
-------------->main, main num : 0
-------------> task1, num : 3
--------------> task2, num:6
-------------->main, main num : 0
--------------> task2, num:7
-------------->main, main num : 0
-------------> task1, num : 4
--------------> task2, num:8
'''