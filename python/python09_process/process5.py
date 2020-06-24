# -*- coding:utf-8 -*-
# @Time : 2020/4/29 下午1:54
# @Author: 手写
# @File : process5.py

from multiprocessing import Process, Queue
from time import sleep


def download(q):
    print('download start')
    sleep(2)
    print('download end')
    q.put('1.png')


def save(q):
    image = q.get()
    print(image)


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=save, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
