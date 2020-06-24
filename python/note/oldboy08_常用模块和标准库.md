<!--
 * @Author: shouxie
 * @Date: 2020-04-27 15:05:07
 * @Description: 
 -->
### time模块

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午3:33
#@Author: 手写
#@File : time01.py
import time

# 时间戳
print(time.time())
'''
time（）：
返回浮点型数字，单位是秒
floating point number
Return the current time in seconds since the Epoch.
运行结果：1587973794.9471931
'''

# 将时间戳转成字符串
print(time.ctime())
'''
运行结果：
Mon Apr 27 15:51:46 2020
'''
# 将时间戳转成元组
print(time.localtime())
'''
运行结果：
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=27, tm_hour=15, tm_min=55, tm_sec=29, tm_wday=0, tm_yday=118, tm_isdst=0)
'''

t = time.localtime()
print(t.tm_year) # 2020

# 将元组的转成时间戳
print(time.mktime(time.localtime()))
'''
运行结果：
1587974670.0
'''

# 将元组的时间转成字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))
'''
运行结果：
2020-04-27 16:06:17
'''

# 将字符串转成元组的方式
'''
def strptime(string, format):
'''
print(time.strptime('2020-04-29', '%Y-%m-%d'))
'''
运行结果：
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=120, tm_isdst=-1)
'''
```
### datetime
datetime模块：
    time   时间
    date   日期     （data 数据）
    datetime  日期时间   now()
    timedelta  时间差  timedelta(days='',weeks ='' ,...)

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午4:10
#@Author: 手写
#@File : datetime01.py

import datetime

print(datetime.time.hour)  # <attribute 'hour' of 'datetime.time' objects>

# date

# def __init__(self, year: int, month: int, day: int)
# 因为date是类，所以要求创建对象
d = datetime.date(2020, 4, 20)
print(d.day)  # 20
print(d.month)  # 4
print(d.year)  # 2020
print(d.ctime())  # Mon Apr 20 00:00:00 2020

print(d.today())  # 2020-04-27
print(datetime.date.today())  # 2020-04-27

# datetime
# 得到当前的日期和时间
print(datetime.datetime.now())  # 2020-04-27 17:07:02.855862

# timedelta
#def __new__(cls, days=0, seconds=0, microseconds=0,milliseconds=0, minutes=0, hours=0, weeks=0):

d_del = datetime.timedelta(days=1)
now = datetime.datetime.now()

print('now:',now) # now: 2020-04-27 17:10:19.376842
print('now+d_del',now+d_del) # now+d_del 2020-04-28 17:10:19.376842
```

### random

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午4:28
#@Author: 手写
#@File : random01.py

import random

# 0~1之间的随机小数
print('0~1之间的随机小数', random.random())
# 随机范围 randrange(start, end, step) 不包含end
print('随机范围，randrange', random.randrange(2, 10, 2))
# randint 包含end
print('randint', random.randint(1, 10))


list0 = [1,2,3,4]
# 随机选择列表的内容
print('random.choice', random.choice(list0))
# 打乱顺序
l = random.shuffle(list0)
print('l:',l,'list0:', list0)
```

### other(chr,ord)

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午5:28
#@Author: 手写
#@File : hashlib.py

# chr  ord


# ord： str ---》Unicode码
str = 'hello world'
# print(ord(str)) # TypeError: ord() expected a character, but string of length 11 found

print(ord('h')) # 104

print(ord('你')) # 20320

# chr: # Unicode码 ---》 str

print(chr(20320)) # 你

# print()  input()  list()  str()  set()  dict()  tuple()
# int()  chr() ord()  bin()  hex()  oct()  isinstance()
```

### hashlib

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午5:32
#@Author: 手写
#@File : hashlib01.py

import hashlib


# ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
#                       'blake2b', 'blake2s',
#                       'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
#                       'shake_128', 'shake_256')
# print(hashlib.md5('hello world')) # TypeError: Unicode-objects must be encoded before hashing

hashStr = hashlib.md5('hello world'.encode('utf-8'))
print(hashStr)  # <md5 HASH object @ 0x108181550>

print(len(hashStr.hexdigest()), hashStr.hexdigest()) # 32 32 5eb63bbbe01eeed093cb22bb8f5acdc3


sha1 = hashlib.sha1('hello world'.encode('utf-8'))
sha1_r = sha1.hexdigest()
print(len(sha1_r), sha1_r) # 40 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed

sha256 = hashlib.sha256('hello world'.encode('utf-8'))
sha256_r = sha256.hexdigest()
print(len(sha256_r), sha256_r) # 64 b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

```