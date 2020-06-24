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

