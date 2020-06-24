# -*- coding:utf-8 -*-
#@Time : 2020/4/17 下午5:21
#@Author: 手写
#@File : index.py
'''
格式：
[表达式 for 变量 in list if 表达式]
'''
list0 = ['lily', 'jack', 'tom', 'danda', 'senevn']

newList = [name for name in list0 if len(name) > 3]
print(newList) # ['lily', 'jack', 'danda', 'senevn']

newList = [i.capitalize() for i in list0 if len(i) > 3]
print(newList) # ['Lily', 'Jack', 'Danda', 'Senevn']

# 1-100 能被3整除的整数
result = [i for i in range(1,101) if not i%3]
print(result) # [3, 6, 9, 12, 15, ...]

# 0-10 奇数偶数组成元组列表
tuple0 = [(i,j) for i in range(0,5) if i % 2 for j in range(0,5) if not j % 2]
print(tuple0) # [(1, 0), (1, 2), (1, 4), (3, 0), (3, 2), (3, 4)]

# 想得到[3,6,8,9]
list0 = [[1,2,3],[2,3,6],[3,4,8],[4,5,9]]
res = [i[len(i)-1] for i in list0]
print(res) # [3, 6, 8, 9]


print('*'*60)

generator = (i+3 for i in range(0,10))
print(generator) # <generator object <genexpr> at 0x1046946d0>
print(generator.__next__()) # 3
print(next(generator))
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
# print(generator.__next__()) # StopIteration

def gen():
    n = 0
    while True:
        n += 1
        yield

g = gen()
print(g) # <generator object gen at 0x102f90740>
print(g.__next__()) # None
print(g.__next__()) # None

def gen1():
    n = 0
    while True:
        n += 1
        yield n

g1 = gen1()
print(g1) # <generator object gen at 0x102f906d0>
print(g1.__next__()) # 1
print(g1.__next__()) # 2

print('*'*60)
def gen2():
    i = 0
    while True:
        res = yield i
        print('res:',res)
        '''
        # 4
        # 6
        '''
        i += 1
g2 = gen2()
# g2.send(2) # TypeError: can't send non-None value to a just-started generator
print('send1========',g2.send(None)) # 0
print('send2========',g2.send(4)) # 1
print('send3========',g2.send(6)) # 2
'''
send1======== 0
res: 4
send2======== 1
res: 6
send3======== 2
'''
print(g2.__next__())
'''
res: None
3
'''
# print(g2.__next__())

