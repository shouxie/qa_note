
 ##  进程(待详细补充，后续会详细总结os)

 > 进程是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础

- 进程特征

动态性：进程的实质是程序在多道程序系统中的一次执行过程，进程是动态产生，动态消亡的。
并发性：任何进程都可以同其他进程一起并发执行。
独立性：进程是一个能独立运行的基本单位，同时也是系统分配资源和调度的独立单位。
异步性：由于进程间的相互制约，使进程具有执行的间断性，即进程按各自独立的、不可预知的速度向前推进。

- 结构组成：程序、数据和进程控制块

- 进程与程序区别

程序是指令和数据的有序集合，其本身没有任何运行的含义，是一个静态的概念。
而进程是程序在处理机上的一次执行过程，它是一个动态的概念。
程序可以作为一种软件资料长期存在，而进程是有一定生命期的。
程序是永久的，进程是暂时的。


生活中，你可能一边听歌，一边写作业；一边上网，一边吃饭。。。这些都是生活中的多任务场景。电脑也可以执行多任务，比如你可以同时打开浏览器上网，听音乐，打开pycharm编写代码...。简单的说**多任务就是同一时间内运行多个程序**

- 单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us，切换到微信，在执行2us，再切换到陌陌，执行2us……。表面是看，每个任务反复执行下去，但是CPU调度执行速度太快了，导致我们感觉就行所有任务都在同时执行一样
（os里面，时间片原理）
- 多核CPU实现多任务原理：真正的秉性执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，os也会自动把很多任务轮流调度到每个核心上执行（待补充：进程调度算法：先来先服务，短作业优先等）

- 并发和并行
  - **并发**：当有多个线程在操作时,如果系统只有一个CPU,则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段,再将时间 段分配给各个线程执行，在一个时间段的线程代码运行时，其它线程处于挂起状。.这种方式我们称之为并发(Concurrent)。**同一时间段**
  - **并行**：当系统有一个以上CPU时,则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)。**同一时刻**
- 实现多任务的方式：
  - 多进程模式；
  - 多线程模式；
  - 协程。
  进程  >  线程  >  协程

## 同步/异步
同步（synchronous）： 所谓同步就是一个任务的完成需要依赖另外一个任务时，只有等待被依赖的任务完成后，依赖的任务才能算完成，这是一种可靠的任务序列。

简言之，要么成功都成功，失败都失败，两个任务的状态可以保持一致。

异步（asynchronous）：所谓异步是不需要等待被依赖的任务完成，只是通知被依赖的任务要完成什么工作，依赖的任务也立即执行，只要自己完成了整个任务就算完成了。至于被依赖的任务最终是否真正完成，依赖它的任务无法确定，所以它是不可靠的任务序列。

## python 中进程

### 进程创建
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/28 下午3:00
#@Author: 手写
#@File : process1.py

from multiprocessing import Process
# import time
from time import sleep
import os
def task1():
    while True:
        sleep(1)
        print('-------------> task1', 'task1的进程号是：{}, 父进程是：{}'.format(os.getpid(), os.getppid()))

def task2():
    while True:
        sleep(1)
        print('--------------> task2', 'task2的进程号是：{}, 父进程是: {}'.format(os.getpid(), os.getppid()))

if __name__ == '__main__':
    # built-in: def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
    p1 = Process(target=task1, name='task1')
    p1.start()
    p2 = Process(target=task2, name='task2')
    p2.start()
    print('-------------->main', 'main 进程号:{}'.format(os.getpid()))
    
    
'''
运行的时候会开启一个进程。
运行结果：
-------------->main main 进程号:11495
-------------> task1 task1的进程号是：11497, 父进程是：11495
--------------> task2 task2的进程号是：11498, 父进程是: 11495
'''
```
### 进程创建，传参
from multiprocessing import Process

  process = Process(target= 函数，name=进程的名字，args=（给函数传递的参数）)
  process 对象

  对象调用方法:
  process.start()    启动进程并执行任务
  process.run()  只是执行了任务但是没有启动进程
  terminate()   终止
  is_alive      判断进程是否存活
  ```python
  # 上述代码：
  def task1(sec):
    while True:
        sleep(sec)
        print('-------------> task1', 'task1的进程号是：{}, 父进程是：{}'.format(os.getpid(), os.getppid()))

  p1 = Process(target=task1, name='task1', args=(2,))
  ```
  ### 多进程对于全局变量访问
  **进程访问变量互不干扰**
  多进程对于全局变量访问，在每一个全局变量里面都放一个m变量，
  保证每个进程访问变量互不干扰。
  m = 1  # 不可变类型
  list1 = []  # 可变类型
  主进程启动子进程，启动之后无法控制是谁先谁后
  ```python
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
  ```

  ### 进程：自定义

  ```python
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


  ```

  ### 进程池
  > 当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
直到池中有进程结束，才会创建新的进程来执行。

 pool = Pool(max)  创建进程池对象
 pool.apply()  阻塞的
 pool.apply_async()  非阻塞的
 pool.close()  添加任务结束
 pool.join()  让主进程让步，让出cpu

```python
# -*- coding:utf-8 -*-
# @Time : 2020/4/29 上午11:20
# @Author: 手写
# @File : pool3.py

from multiprocessing import Pool

'''
非阻塞式: 全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用。
阻塞式: 添加一个执行一个任务，如果一个任务不结束另一个任务就进不来

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
    p.close()# 添加任务结束
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

```

### 进程间通信

队列和管道属于进程之间的通信机制。

#### 队列

> 创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/29 下午12:07
#@Author: 手写
#@File : queue4.py

from multiprocessing import Queue


# built-in: def __init__(self, maxsize=-1):
q = Queue(5)
# built-in: def put(self, obj, block=True, timeout=None):
# q.put('1') 如果queue满了则只能等待，除非有‘空地’则添加成功
for i in range(4):
    q.put(str(i)) 

# print(q.qsize())
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.full()) # 判断队列是否满
print(q.empty())
q.get_nowait()

'''
mac 不能打印 print(q.qsize())
NotImplementedError
 # Raises NotImplementedError on Mac OSX because of broken sem_getvalue()
'''
```
#### 队列实现进程间通讯
```python
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

```

## 线程

> 进程是线程的容器
进程有很多优点，它提供了多道编程，让我们感觉我们每个人都拥有自己的CPU和其他资源，可以提高计算机的利用率.但是进程只能在一个时间干一件事，如果想同时干两件事或多件事，进程就无能为力了；进程在执行的过程中如果阻塞，例如等待输入，整个进程就会挂起，即使进程中有些工作不依赖于输入的数据，也将无法执行

进程由若干线程组成，一个进程至少一个线程；
一个标准的线程由线程ID，当前指令指针(PC），寄存器集合和堆栈组成。线程是进程中的一个实体，是被系统独立调度和分派的基本单位，线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的其它线程共享进程所拥有的全部资源。
一个线程可以创建和撤消另一个线程，同一进程中的多个线程之间可以并发执行。由于线程之间的相互制约，致使线程在运行中呈现出间断性。线程也有就绪、阻塞和运行三种基本状态。就绪状态是指线程具备运行的所有条件，逻辑上可以运行，在等待处理机；运行状态是指线程占有处理机正在运行；阻塞状态是指线程在等待一个事件（如某个信号量），逻辑上不可执行。每一个程序都至少有一个线程，若程序只有一个线程，那就是程序本身

### 线程和进程区别

地址空间和其它资源（如打开文件）：进程间相互独立，同一进程的各线程间共享。某进程内的线程在其它进程不可见。
通信：进程间通信IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信——需要进程同步和互斥手段的辅助，以保证数据的一致性。
调度和切换：线程上下文切换比进程上下文切换要快得多。
在多线程操作系统中，进程不是一个可执行的实体。


### 创建线程

```python
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
```
### 线程共享全局变量

```python
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

```

### GIL 全局解释器锁

> 为了让各个线程能够平均利用CPU时间，python会计算当前已执行的微代码数量，达到一定阈值后就强制释放GIL

```python
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
```

Gil锁  : 保证同一时刻只有一个线程能使用到cpu
互斥锁 : 多线程时,保证修改共享数据时有序的修改,不会产生数据修改混乱

### Lock

> 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

同步： 一个一个的完成，一个做完另一个才能进来。
效率就会降低。

使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。

多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。
但是当线程需要共享数据时，可能存在数据不同步的问题。
为了避免这种情况，引入了锁的概念。

lock =threading.Lock()

lock.acquire()  请求得到锁
  ......
lock.release()  释放锁

只要不释放其他的线程都无法进入运行状态

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/30 上午11:21
#@Author: 手写
#@File : lock9.py
import threading
from time import sleep

lock = threading.Lock()

def task1():
    lock.acquire() # 获取线程锁，如果已经上锁，则等待锁的释放
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
```

### 死锁

#### 死锁定义

多进程，多线程的并发执行虽然提升了系统资源的利用率，提高了系统的性能，但是并发执行也带来了新的问题-----死锁。

死锁是指多个进程（线程）在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞的现象（互相挂起等待），若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程

#### 常见的死锁
1. 线程将自己锁住

为了保证线程之间的同步和互斥，我们往往需要给其加锁，有时候，线程申请了锁资源，还没有等待释放，又一次申请这把锁，结果就是挂起等待这把锁的释放，但是这把锁是被自己拿着，所以就会永远挂起等待，就造成了死锁

2. 多线程竞争资源循环等待

有两个线程P1和P2，P1首先申请得到了锁L1,P2申请得到了锁L2,这个时候P1有向去申请锁L2，结果是被挂起等待P2释放锁L2,而P2恰好也想申请锁L1，结果是挂起等待P1释放锁L1，此时就造成两个线程互相僵持，造成死锁。

3. 进程推进顺序不当

有三个线程，P1，P2和P3，分别生产数据M1，M2，M3，同时分别接收别的线程产生的数据M3,M2,M1,如果线程推进的顺序正确，即三个线程都先生产数据，再接收，那么没有问题，但是一旦线程先接受数据，再生产数据，因为一开始没有数据产生，那么就会造成三个线程的死锁问题。

#### 死锁产生的四个必要条件
互斥条件：进程（线程）申请的资源在一段时间中只能被一个进程（线程）使用。
请求与等待条件：进程（线程）已经拥有了一个资源，但是又申请新的资源，拥有的资源保持不变 。
不可剥夺条件：在一个进程（线程）没有用完，主动释放资源的时候，不能被抢占。
循环等待条件：多个进程（线程）之间存在资源循环链。

#### 处理死锁

预防死锁：破坏死锁产生的四个条件之一，注意，互斥条件不能破坏。
避免死锁：合理的分配资源。
检查死锁：利用专门的死锁机构检查死锁的发生，然后采取相应的方法。
解除死锁：发生死锁时候，采取合理的方法解决死锁。一般是强行剥夺资源

#### 银行家算法

> 一个银行家如何将一定数目的资金安全地借给若干个客户，使这些客户既能借到钱完成要干的事，同时银行家又能收回全部资金而不至于破产，这就是银行家问题。这个问题同操作系统中资源分配问题十分相似：银行家就像一个操作系统，客户就像运行的进程，银行家的资金就是系统的资源。

在避免死锁的方法中最有名的就是银行家算法，它是DIJKstra E.W于1968年提出来的。
为什么叫做银行家算法呢，是因为这有点向银行的“借贷”服务，假如银行只有有限多的资金供给客户进行贷款服务，那么为了保证银行能有足够的资金运转，它在借钱之前要审核客户是否有能够在指定时间内偿还贷款的能力。
在研究我们的操作系统的资源分配策略时，也会出现类似的问题，我们系统中的有限资源要分配给各种进程，那么就要事先考察此进程是否有在指定期限内归还资源的能力。必须要保证它能在有限的时间内进行归还，拱其他进程使用。
大致实现方法：

当一个进程对资源的最大需求量不超过系统中的资源数时可以接纳该进程。
进程可以分期请求资源，当请求的总数不能超过最大需求量。
当系统现有的资源不能满足进程尚需资源数时，对进程的请求可以推迟分配，但总能使进程在有限的时间里得到资源。
当系统现有的资源能满足进程尚需资源数时，必须测试系统现存的资源能否满足该进程尚需的最大资源数，若能满足则按当前的申请量分配资源，否则也要推迟分配。
银行家算法：首先需要定义状态和安全状态的概念。系统的状态是当前给进程分配的资源情况。因此，状态包含两个向量Resource（系统中每种资源的总量）和Available（未分配给进程的每种资源的总量）及两个矩阵Claim（表示进程对资源的需求）和Allocation（表示当前分配给进程的资源）。安全状态是指至少有一个资源分配序列不会导致死锁。当进程请求一组资源时，假设同意该请求，从而改变了系统的状态，然后确定其结果是否还处于安全状态。如果是，同意这个请求；如果不是，阻塞该进程知道同意该请求后系统状态仍然是安全的。

银行家算法是从当前状态出发，逐个按安全序列检查各客户谁能完成其工作，然后假定其完成工作且归还全部贷款，再进而检查下一个能完成工作的客户，……。如果所有客户都能完成工作，则找到一个安全序列，银行家才是安全的
```python
'''
@Author: shouxie
@Date: 2020-02-13 12:52:42
@Description: 
'''
# 死锁
'''
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。

避免死锁：
解决：
1. 重构代码
2. 使用timeout参数

'''

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    # def __init__(self,name):
    #     pass
    def run(self):  # start()
        if lockA.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了A锁')  #
            time.sleep(0.1)
            if lockB.acquire(timeout=5):  # 阻塞
                print(self.name + '又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()
        if lockB.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()

```
#### 生产者与消费者

```python
'''
生产者与消费者：两个线程之间的通信

Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，
LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原理
（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步。

'''

import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put("生产者产生数据：%d" % num)
        print("生产者产生数据：%d" % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者获取到：%s" % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == "__main__":
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print("END")

'''
线程：Thread

1. 创建线程
   A.t =  Thread(target=func,name='',args=(),kwargs={})  新建状态
     t.start()  ---->就绪状态
     
     run()
     join()   
   B. 自定义线程
        class MyThread(Thread):
           def __init__(self,name):
              super().__init__()
              self.name=name
        
            def run(self):
                任务
                
        t = MyThread('name')
        t.start()
   
    
2. 数据共享
        进程共享数据与线程共享数据区别：
          进程是每个进程中都有一份
          线程是共同一个数据  ----》 数据安全性问题
        
        GIL  ----》 伪线程 
        
        lock = Lock()
        lock.acquire()
        ......
        lock.release()
        
        -----> 只要用锁：死锁
        避免死锁
3. 线程间通信： 生产者与消费者
   生产者：线程
   消费者：线程
   import queue
   
   q = queue.Queue()
     # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()
    
   q.put()
   q.get()
   
扩展： GIL

'''

```