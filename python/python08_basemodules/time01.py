# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午3:33
#@Author: 手写
#@File : time01.py
import time

# 1. 时间戳
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

t = time.localtime()
print(t.tm_year) # 2020