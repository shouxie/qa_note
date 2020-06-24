# -*- coding:utf-8 -*-
# @Time : 2020/4/29 下午2:20
# @Author: 手写
# @File : thread7.py
import threading
from time import sleep

ticket = 100


def buy1():
    global ticket
    n = 0
    while n < 100:
        if ticket > 0:
            sleep(0.1)
            ticket -= 1
            print('buy01 ticket {}'.format(ticket))
            n += 1
        else:
            print('票没了')

def buy2():
    global ticket
    n = 0
    while n < 100:
        if ticket > 0:
            sleep(0.1)
            ticket -= 1
            print('buy02 ticket {}'.format(ticket))
            n -= 1
        else:
            print('票没了')


if __name__ == '__main__':
    t1 = threading.Thread(target=buy1, name='buy1')
    t2 = threading.Thread(target=buy2, name='buy2')
    t1.start()
    t2.start()
