# -*- coding:utf-8 -*-
#@Time : 2020/4/29 下午2:10
#@Author: 手写
#@File : thread6.py
from time import sleep
import threading

def download():
    print('download start')
    sleep(2)
    print('download end')

def listen():
    print('listen start')
    sleep(3)
    print('listen end')

if __name__ == '__main__':
    '''
    built-in:
    def __init__(self, group: None = ...,
                     target: Optional[Callable[..., None]] = ...,
                     name: Optional[str] = ...,
                     args: Iterable = ...,
                     kwargs: Mapping[str, Any] = ...,
                     *, daemon: Optional[bool] = ...) -> None: ...
                     
         __init__(self, group=None, target=None, name=None,
     args=(), kwargs=None, *, daemon=None):
    '''
    t1 = threading.Thread(target=download, name='download')
    t2 = threading.Thread(target=listen, name='listen')
    t1.start()
    t2.start()