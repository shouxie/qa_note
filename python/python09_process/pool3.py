# -*- coding:utf-8 -*-
# @Time : 2020/4/29 上午11:20
# @Author: 手写
# @File : pool3.py

from multiprocessing import Pool

'''
非阻塞式:全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用。

创建一个进程池，最大连接为5。每个进程执行一个任务
'''
list0 = []
import random
from time import sleep, time
from multiprocessing import Pool


def task(taskname):
    print('-----------> 执行任务： {}开始'.format(taskname))
    startTime = time()
    sleep(random.random())
    endTime = time()
    print('-----------> 执行任务： {}完成'.format(taskname), '用时{}'.format(str(endTime - startTime)))
    return '任务{} 用时{}'.format(taskname, str(endTime - startTime))


def handleCall(data):
    list0.append(data)


if __name__ == '__main__':
    # def __init__(self, processes=None, initializer=None, initargs=(),  processes: 最大进程数
    #                  maxtasksperchild=None, context=None):
    p = Pool(5)

    # built-in： def apply_async(self, func, args=(), kwds={}, callback=None, 非阻塞
    #         error_callback=None):
    #     '''
    #     Asynchronous version of `apply()` method.
    #     '''
    tasks = ['任务1', '任务2', '任务3', '任务4', '任务5', '任务6', '任务7']
    for i in tasks:
        # p.apply_async(task, args=(i,), callback=handleCall)

        # built-in： def apply(self, func, args=(), kwds={}):
        p.apply(task, args=(i,))
    # p.apply_async(task, args=('任务1',),  callback=handleCall)
    # p.apply_async(task, args=('任务2',), callback=handleCall)
    # p.apply_async(task,args=('任务3',), callback=handleCall)
    p.close()
    p.join()

    for l in list0:
        print('l:', l)

'''
运行结果：
非阻塞式
-----------> 执行任务： 任务1开始
-----------> 执行任务： 任务2开始
-----------> 执行任务： 任务3开始
-----------> 执行任务： 任务4开始
-----------> 执行任务： 任务5开始
-----------> 执行任务： 任务3完成 用时0.3876230716705322
-----------> 执行任务： 任务6开始
-----------> 执行任务： 任务4完成 用时0.43808794021606445
-----------> 执行任务： 任务7开始
-----------> 执行任务： 任务1完成 用时0.5240042209625244
-----------> 执行任务： 任务2完成 用时0.6877861022949219
-----------> 执行任务： 任务5完成 用时0.8197996616363525
-----------> 执行任务： 任务6完成 用时0.7132937908172607
-----------> 执行任务： 任务7完成 用时1.0014679431915283
l: 任务任务3 用时0.3876230716705322
l: 任务任务4 用时0.43808794021606445
l: 任务任务1 用时0.5240042209625244
l: 任务任务2 用时0.6877861022949219
l: 任务任务5 用时0.8197996616363525
l: 任务任务6 用时0.7132937908172607
l: 任务任务7 用时1.0014679431915283


pool中最大5个进程，当任务3完成的时候，任务6就可以开始了。每个任务做完都把用时抛出来，回调方法接收这个返回值，回调方法就是任务完成要执行的动作

阻塞式
-----------> 执行任务： 任务1开始
-----------> 执行任务： 任务1完成 用时0.21695709228515625
-----------> 执行任务： 任务2开始
-----------> 执行任务： 任务2完成 用时0.38028597831726074
-----------> 执行任务： 任务3开始
-----------> 执行任务： 任务3完成 用时0.8004181385040283
-----------> 执行任务： 任务4开始
-----------> 执行任务： 任务4完成 用时0.3384280204772949
-----------> 执行任务： 任务5开始
-----------> 执行任务： 任务5完成 用时0.48204588890075684
-----------> 执行任务： 任务6开始
-----------> 执行任务： 任务6完成 用时0.5169289112091064
-----------> 执行任务： 任务7开始
-----------> 执行任务： 任务7完成 用时0.3745450973510742
'''
