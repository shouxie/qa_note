# -*- coding:utf-8 -*-
# @Time : 2020/4/29 上午11:01
# @Author: 手写
# @File : process2.py

from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            print('----------> 自定义进程{}, n: {}'.format(self.name, n))
            n += 1


def task():
    while True:
        print('---------> task')


if __name__ == '__main__':
    p = MyProcess('test')
    # p1 = Process(target=task, name='task')
    # p1.start()
    p.start()

