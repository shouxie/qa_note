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




print('-'*70)



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

# 查看目录下所有文件，放在一个列表中
print(os.listdir(path)) # ['test1.txt', 'index.py', '__init__.py']

# os.mkdir('test') # FileExistsError: [Errno 17] File exists: 'test' 如果已经存在，会报错
'''
os.mkdir(path)
　　其参数path 为要创建目录的路径。
 # FileExistsError: [Errno 17] File exists: 'test' 如果已经存在，会报错
'''


# 创建多级目录。
# os.makedirs('test1/test11')




# os.rmdir('test') # OSError: [Errno 66] Directory not empty: 'test' 只能删除空文件夹

# os.removedirs('test2')
'''
删除多级目录。
OSError: [Errno 66] Directory not empty: 'test' 只能删除空文件夹 
No such file or directory: 'test2' 如果不存在会报错
'''



# os.rmdir('test1')
'''
 No such file or directory: 'test1' 如果不存在会报错
'''


# 删除一个文件
# os.remove('test/1.txt')
'''
FileNotFoundError: [Errno 2] No such file or directory: 'test/1.txt' 如果不存在会报错
'''

print('='*10)

# 目录1下面复制到目录2
# print(os.listdir('rmdir_01')) # ['01.txt', 'rmdir_012', 'rmdir_011']
#
# l = os.listdir('rmdir_01')
# m_path = 'rmdir_01'
# isexist = os.path.exists('rmdir_01')
# if not isexist:
#     os.mkdir('cpdir_01')
# c_path = 'cpdir_01'
# print(os.path.isfile(os.path.join(m_path, '01.txt')))
# for i in l:
#     path = os.path.join(m_path, i)
#     pathc = os.path.join(c_path, i)
#     print('origin data:', path)
#     # if file
#     if os.path.isfile(path):
#         with open(path) as pipe_r:
#             result = pipe_r.read()
#             with open(pathc, 'w') as pipe_w:
#                 pipe_w.write(result)
#             pass
#     else:
#         os.mkdir(pathc)

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
# copy('cpdir_01', 'rmdir_01')

print('err','*'*20)
try:
    [].pop()
except Exception as err:
    print(err) # pop from empty list



def func():
    try:
        n1 = int(input('输入数字:'))
        print(n1)
        return 1
    except ValueError:
        print('必须是数字....')
        return 2
    else:
        print('数字输入完毕！')   # 没有异常才会执行的代码块


# 调用函数
func()