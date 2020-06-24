### 文件操作:
```python
'''
 文件上传
 保存log

系统函数：
 open(file,mode,buffering,encodeing)

 读:
   open（path/filename,'rt'）---->返回值：stream (管道)

   container = stream.read()  ---->读取管道中内容

   注意： 如果传递的path/filename有误，则会报错：FileNotFoundError
    如果是图片则不能使用默认的读取方式,mode = 'rb'

    总结:
    read()  读取所有内容
    readline() 每次读取一行内容
    readlines() 读取所有的行保存到列表中
    readable()  判断是否可读的

'''

stream = open(r'C:\p1\aa.txt')

# container = stream.read()
# print(container)

result = stream.readable()  # 判断是否可以读取  True  False
print(result)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break


lines = stream.readlines()  # 保存到列表中
print(lines)
for i in lines:
    print(i)

stream = open(r'C:\p1\girl.jpg', 'rb')

container = stream.read()
# print(container)
```


### 写文件
```python
'''
stream = open(r'c:\p1\aa.txt', 'w')
mode 是’w‘ 表示就是写操作  每次都会将原来的内容清空，

方法:
     write(内容)   然后写当前的内容
    writelines(Iterable)  没有换行效果
    stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])  ---》自己加

如果mode='a'


'''

stream = open(r'c:\p1\aa.txt', 'a')

# s = '''
# 你好！
#     欢迎来到澳门博彩赌场，赠送给你一个金币！
#                 赌王: 高进
#
# '''

result = stream.write('hello')
# print(result)

stream.write('龙五')

stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])

stream.write('僵尸先生')

stream.close()  # 释放资源

# stream.write('龙五2号')
```
### 文件的复制
```python
'''
原文件： c:\p1\girl.jpg
目标文件： c:\p2\girl.jpg

with 结合open使用，可以帮助我们自动释放资源

'''
# stream = open(r'c:\p1\girl.jpg', 'rb')

with open(r'c:\p1\girl.jpg', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'c:\p2\girl.jpg', 'wb') as wstream:
        wstream.write(container)

print('文件复制完成！')
```
### 模块： os.py
```python
import random
'''
os.path:
os.path.dirname(__file__)获取当前文件所在的文件目录（绝对路径）
os.path.join(path,'')  返回的是一个拼接后的新的路径

'''

import os

# print(os.path)
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
# print(path)
# print(type(path))
# result = os.path.join(path, 'a1.jpg')
# print(result)
# p1\girl.jpg ---->保存在当前文件所在的目录

with open(r'c:\p1\girl.jpg', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind('\\')+1:]  # 截取文件名

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, filename)

    with open(path1, 'wb') as wstream:
        wstream.write(container)
```


练习：
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/15 下午7:54
#@Author: 手写
#@File : index.py

# mode default is 'r'
# read
obj = open('/users/qpp/test.txt')
print(obj.read()) # helloworld
obj.close()
# write
obj1 = open('/Users/qpp/test.txt', 'w')
print('*'*20)
obj1.write('hello')
obj1.write('world')
# helloworld
obj1.close()
# obj1.writelines('hello python') # ValueError: I/O operation on closed file.


obj2 = open('/users/qpp/test.txt', 'a')
obj2.write('hello')
obj2.write('qpp')
# helloworldhelloqpp
obj2.close()

# copy 先读，再写
with open('/users/qpp/test.txt') as obj3:
    result = obj3.read()
    with open('/users/qpp/important/test.txt', 'w') as obj4:
        obj4.write(result)



'''
os 模块
'''
import os
print(os.path) # <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/posixpath.py'>

# 获取当前目录
print(os.path.dirname(__file__)) # /Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files

print(type(os.path.dirname(__file__))) # <class 'str'>

currentDir = os.path.dirname(__file__)
currentPath = os.path.join(currentDir, 'index.py')
print(currentPath) # /Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files/index.py


# 结合os 复制
with open('/users/qpp/test.txt') as pipe_r:
    r_result = pipe_r.read()
    current_dir = os.path.dirname(__file__)
    current_path = os.path.join(current_dir, 'test1.txt')
    with open(current_path, 'w') as pipe_w:
        pipe_w.write(r_result)
```


#### os.path 
```python
# 判断是否是绝对路径
isabs = os.path.isabs('/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_file')
print(isabs) # True
 # 返回文件的绝对路径
print(os.path.abspath('test1.txt')) # /Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files/test1.txt
# 返回当前文件的绝对路径
print(os.getcwd()) # /Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files
path = '/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files/'
# 参数为绝对路径
# 判断是否为目录
print(os.path.isdir('/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files/')) # True
# 判断是否为文件
print(os.path.isfile('test1.txt')) # True

print(os.path.getsize('test1.txt')) # 18 (单位为字节)

# 分割成元组，第一个是目录，第二个是文件名
print(os.path.split(__file__)) # ('/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files', 'index.py')

# 分割成元组，第一个是目录加文件名，第二个是文件名后缀
print(os.path.splitext(__file__)) # ('/Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files/index', '.py')


print(os.path.dirname(__file__)) # /Users/qpp/important/project/daling-work-mark/努力做个测试吧/python/python03_files

```

#### os 创建，删除目录  mkdir makedirs rmdir removedirs

```python

# 查看目录下所有文件，放在一个列表中 可以传绝对路径，或者相对路径
print(os.listdir(path)) # ['test1.txt', 'index.py', '__init__.py']

os.mkdir('test') # FileExistsError: [Errno 17] File exists: 'test' 如果已经存在，会报错
'''
os.mkdir(path)
　　其参数path 为要创建目录的路径。
 # FileExistsError: [Errno 17] File exists: 'test' 如果已经存在，会报错
'''


# 创建多级目录。
os.makedirs('test1/test11')




os.rmdir('test') # OSError: [Errno 66] Directory not empty: 'test' 只能删除空文件夹

os.removedirs('test2')
'''
删除多级目录。
OSError: [Errno 66] Directory not empty: 'test' 只能删除空文件夹 
No such file or directory: 'test2' 如果不存在会报错
'''



os.rmdir('test1')
'''
 No such file or directory: 'test1' 如果不存在会报错
'''


# 删除一个文件
os.remove('test/1.txt')
'''
FileNotFoundError: [Errno 2] No such file or directory: 'test/1.txt' 如果不存在会报错
''' 
```


#### copy 
```python
# 目录1下面复制到目录2
print(os.listdir('rmdir_01')) # ['01.txt', 'rmdir_012', 'rmdir_011']

l = os.listdir('rmdir_01')
m_path = 'rmdir_01'
isexist = os.path.exists('rmdir_01')
if not isexist:
    os.mkdir('cpdir_01')
c_path = 'cpdir_01'
print(os.path.isfile(os.path.join(m_path, '01.txt')))
for i in l:
    path = os.path.join(m_path, i)
    pathc = os.path.join(c_path, i)
    print('origin data:', path)
    # if file
    if os.path.isfile(path):
        with open(path) as pipe_r:
            result = pipe_r.read()
            with open(pathc, 'w') as pipe_w:
                pipe_w.write(result)
            pass
    else:
        os.mkdir(pathc)
```
封装，递归调用
```python
def copy(src, tar):
    l = os.listdir(src)
    m_path = src
    # isexist = os.path.exists('rmdir_01')
    # if not isexist:
    #     os.mkdir('cpdir_01')
    c_path = tar
    for i in l:
        path = os.path.join(m_path, i)
        pathc = os.path.join(c_path, i)
        print('origin data:', path)
        # if file
        if os.path.isfile(path):
            with open(path) as pipe_r:
                result = pipe_r.read()
                with open(pathc, 'w') as pipe_w:
                    pipe_w.write(result)
                pass
        else:
            os.mkdir(pathc)
            copy(path, pathc)
copy('cpdir_01', 'rmdir_01')
```