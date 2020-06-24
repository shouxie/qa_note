# -*- coding:utf-8 -*-
#@Time : 2020/3/10 上午7:18
#@Author: 手写
#@File : __init__.py.py
# 标识符
# Python 标识符
# 在 Python 里，标识符由字母、数字、下划线组成。
#
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
#
# Python 中的标识符是区分大小写的。
#
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
#
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
#
# Python 可以同一行显示多条语句，方法是用分号 ; 分开，如：
# 下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
#
# 所有 Python 的关键字只包含小写字母。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py


'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
'''
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典
'''
# print('hello wolrd');
# print('hhh');
# _ = 'hello';
# print(type(_));
# print(type(1));
# # print(input());
# print(_*3);
# print(_*1.1);
# a = input();
# # a = int(a);
# # b = input();
# # b= int(b);
# # print(a+b);
a = '111'
b = 'hello'
c = 'world'
print('adddd%ssdf%s' %(a,b))
# print(1+'a')
age = 19.5
age1 = '19'
print('age is %0002d' % age)

salary = 99.91
print('salary is %.1f' % salary)
# ticket 49.5
# count 35
'''
电影 XXX
人数 xxx
单价 xxx
总票价 xxx
'''
movie = 'ttt'
ticket = 79.9
count = 35
print('电影:%s\n人数:%d\n:单价:%.1f\n总票价%.1f' %(movie,count,ticket,count*ticket))
messgae = '''
        电影:%s
        人数:%d
        单价:%.1f
        总票价:%.1f     
'''%(movie,count,ticket,count*ticket)
print(messgae)
name = 'qpp'
# age = 19
# salary='99.99'
# message = 'my name is {},age is {},my salary is {}'.format(name,age,salary)
# print(message)
#
# role = input('清输入角色')
# name = input('清输入名字')
# print('your name is {},角色是{}'.format(name, role))
print(id(name), name)
# 赋值运算符
name1 = name
print(id(name1), name1)
age = 1
age1 = 1
print(id(age))
print(id(age1))
print(age is age1)
# 源文件和交互式 执行结果不一样：小整数 大整数
'''
源文件：一起解释编译复用内存
交互式：小整数复用 大整数，定义一个变量会重新开辟内存
'''
num = 2000000
num1 = 2000000
print(id(num), id(num1))

print(bin(12))
print(bin(0x12ac))
print(int(0x12ac))
print(1 & 2)  # 0
print(0b1101 | 0b1010)  # 15
print(~0b1101)  # -14
print(~5)  # -6 0000
# -x=!x+1 在计算机中，负数以原码的补码形式表达。
print(~0b0101)  # 取反=> 1111 1010 减1-> 1111 1001      取反->0000 0110
print(~-4)  # -4 : - 0000 0100 -> 1111 1011 +1 -> 1111 1100 ==== 0000 0011 正数 不需要转换 为3
print(~5)  # 6: 0000 0101 -> 各位取反： 1111 1010 转为10进制数： ------> 1开头的为负数。转为： x=！（-x-1） 1111 1001 -》 0000 0110 -》 -6
# print(int(0b11110011))
print(3 ^ 5)
print(3 >> 1)
print(1 if (1>2) else 2)
print(1+2)
if True:
    print('hello')
# import random
# print(random.randint(1,10))
# ran = random.randint(1,10)
# your = int(input('请输入一个1-10的整数'))
# if (ran > your):
#     print('*'*10,'猜小了','*'*10,ran)
# else:
#     print('*'*10,'over','*'*10,ran)
# for i in range(8):
#     print('helloworld', i)
# for i in range(5):
#     print('my age is %d' %i)
# else:
#     print('my age is -0')
'''
for i in range(3):
    pass
for i in range(3):
    username = input('请输入用户名')
    password = input('请输入密码')
    if username == 'qpp' and password == '11':
        print('hello')
        break
    else:
        print('用户名或密码错误，只有三次机会请重新输入')
else:
    print('账户锁定')
'''
# 打印1-30 所有3的倍数
i = 1
while i <= 30:
    if not(i % 3):
        print('i:%d' % i)
    i += 1

# j = 1
# while j <= 30:
#     if j == 7:
#         continue
#     else:
#         print('i:%d' % j)
#     j += 3

list0 = ['hello', 'world', 1, 23, False]
# print('list is ', list0[0:4:2])
# print(list0*2)
# print(list0+[1])
# print(list0[-1:])

tuple = (1, 'hello', 1.10, -10, True, 'world')
# print(tuple[1:5])  # ('hello', 1.1, -10, True)
# print(tuple[0])  # 1
# print(tuple*3)  # (1, 'hello', 1.1, -10, True, 'world', 1, 'hello', 1.1, -10, True, 'world', 1, 'hello', 1.1, -10, True, 'world')
# print(tuple + (1, 2, 3))  # (1, 'hello', 1.1, -10, True, 'world', 1, 2, 3)
# print(tuple[0:4:2])  # (1, 1.1)
import math
# print(dir(math))
# print(abs(-1))  # 1
# print(math.ceil(10.1))  # 11
# print(cmp(1, 2))
a,b,c='a',"a",'''a'''
# print(id(a),id(b),id(c))
# print(r'\'111\'')  # \'111\'
# print('hello'[::-1])

hello = 'hello world'
#  逆序输出world 正序输出hello 逆序输出字符串 打印oll 打印llo wo
print(hello[-1:-6:-1])
print(hello[0:5])
print(hello[::-1])
print(hello[4:1:-1])
print(hello[2:8])

message = 'my name is hh'
msg = message.capitalize()
print(msg)  # My name is hh
msg = message.upper()
print(msg) # MY NAME IS HH
msg = message.lower()
print(msg) # my name is hh
msg = message.title()
print(msg) # My Name Is Hh

valityCode = 'Assfewoi23460jgjF8ib0jjgil2GYTLiKgbhO210'
import random
code = ''
for i in range(4):
    ran = random.randint(0, len(valityCode) - 1)
    code += valityCode[ran]
# print(code.lower())

j,code1 = 0,''
while j < 4:
    ran = random.randint(0,len(valityCode)-1)
    code1 += valityCode[ran]
    j +=1
# print(code1.lower())

str = 'hello wolrd'
# print('x' in str) # False
# print('o' in str) # True
# print('x' not in str) # True
# print(str.find('x'))
# print(str.rfind('o'))
# # print(str.index('x'))
# print(str.replace('l', '-',1))

# print('哈哈'.encode('utf-8')) # b'\xe5\x93\x88\xe5\x93\x88'
# print('哈哈'.encode('utf-8').decode())
# print(str.startswith('hell'))
# print(str.endswith('d'))
# your = input('请上传图片')
# if your.endswith('jpg') or your.endswith('png') or your.endswith('gif'):
#     print('yes')
# else:
#     print('no')

# print(str.replace(' ','').isalpha())
# str1 = '121'
# print(str1.isdigit())
# sum1 = 0
# for i in range(3):
#     inp = input('请输入数字')
#     if inp.isdigit():
#         sum1 += int(inp)
#     # else:
#     #     print('error')
#     #     break
# # else:
#     print('sum %d' % sum1)
# print('-'.join('hello')) # h-e-l-l-o
# list1 = ['h','e','1',0]
# print(' '.join(list1)) # TypeError: sequence item 3: expected str instance, int found list包含数字，不能直接转化成字符串。
# print(' '.join('%s' % id for id in list1)) # h e 1 0

str = '      hello      '
print(str.lstrip())
# print('    9   '.strip())
#
# list0 = ['1',2,3,'hello',4]
# list0.append('world')
# print(list0) # ['1', 2, 3, 'hello', 4, 'world']
# list0.extend('hello')
# print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o']
# list0.extend([3,4])
# print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4]
# list0 = list0+[0]
# print(list0) # ['1', 2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]
# del list0[0]
# print(list0) # [2, 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]
# print(1 in list0) # False
# list0.insert(1,'name')
# print(list0) # [2, 'name', 3, 'hello', 4, 'world', 'h', 'e', 'l', 'l', 'o', 3, 4, 0]
#
#
# # 产生10个不同随机数放入列表中
# import random
# ranList,i = [],0
# while i < 10:
#     ran = random.randint(0,15)
#     if (ran not in ranList):
#         ranList.append(ran)
#         i+=1
# print(ranList)

# max min sum
# maxVal = minVal = ranList[0]
# sum1 = 0
# for i in ranList:
#     if i < minVal:
#         minVal = i
#     if i > maxVal:
#         maxVal = i
#
#     sum1 += i
# print(maxVal,max(ranList),minVal,min(ranList),sum1,sum(ranList))
#
# print(sorted(ranList,reverse=True))
# # print(ranList.split())
# print(list(range(0,5)))  # [0, 1, 2, 3, 4]
# print('***'*12)
# print(enumerate(ranList))
aList = [123, 'xyz', 'zara', 'abc']
aTuple = 123, 'xyz', 'zara', 'abc'

print(aTuple)
a=1,2,3
print(a,type(a))
m,n = (1,2)
print(m,n)
a,*b=(1,2,3)
print(a,b, *b, *[1,2,3,4]) # 1 [2, 3] 2 3 1 2 3 4
a,*b = (1,)
print(a,b) # 1 []

t1=(1,2)
t2 = (3,4)
print(t1+t2)
tuple3 = (('name', '123'),('age',12))
print(dict(tuple3)) # {'name': '123', 'age': 12}
tuple4 = [('name', '123', '456'),('age', 12,13)]
# print(dict(tuple4)) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
print({'age':1})
# print()
obj = {}
obj['name'] = 'zhangsan'
print(obj) # {'name': 'zhangsan'}
obj['age'] = 18
print(obj['name'])
for i in obj:
    print(i) # 遍历出来的是key
print('*'*12)
print(obj.items()) # dict_items([('name', 'zhangsan'), ('age', 18)])
print(obj.values()) # dict_values(['zhangsan', 18])
print(obj.keys()) # dict_keys(['name', 'age'])

for i in obj.items():
    print(i)
    # ('name', 'zhangsan')
    #  ('age', 18)
for key, value in obj.items():
    print(key,value)
    '''
    name zhangsan
    age 18
    '''

print(obj.get('age')) # 18

obj.clear()
print(obj)
obj['name'] = 'zhangsan'
obj['age'] = 19
obj['ferght'] = 100
print(obj.copy())
print(obj.get('aaa',1), obj)  # 1 {'name': 'zhangsan', 'age': 19, 'ferght': 100}
print(obj.setdefault('aaa',1),obj) # 1 {'name': 'zhangsan', 'age': 19, 'ferght': 100, 'aaa': 1}
# print(obj.has_key('name')) # py3 remove
print(obj.__contains__('name'))  # True

obj1 = {'name': 'lisi', 'age':20,'hhh':'hello'}
obj1.update(obj)
print(obj1) # {'name': 'zhangsan', 'age': 19, 'hhh': 'hello', 'ferght': 100, 'aaa': 1}

tuple5 = ('name','age')
list1 = ['name', 'age']
obj2 = {}
print(obj2.fromkeys(tuple5)) # {'name': None, 'age': None}
print(obj2.fromkeys(tuple5, 10)) # {'name': 10, 'age': 10}
print(obj2.fromkeys(list1))
obj2 = obj2.fromkeys(list1,10)
print(obj2.fromkeys(list1,10))
print(obj1)
obj1.pop('name')
print(obj1)
print('==='*10)
print(obj2) # {}
s1 = set()
list1 = [1,2,2,3,4]
print(set(list1))

s1 = set()
s1.add('hello')
s1.add('111')
s1.add(2)
print(s1) # {'111', 2, 'hello'}
s1.update((1,2))
print(s1) # {'111', 1, 2, 'hello'}
s1.add((1,2))
print(s1) # {1, 2, (1, 2), '111', 'hello'}

# 产生10个1～20的随机数，去重
import random
s = set()
# l = []
for i in range(10):
    ran = random.randint(1, 20)
    s.add(ran)
    # l.append(ran)
    # s.update(l)
# print(s, l)
print(s)

print('*'*20)

# 集合的交集，并集，差集合
s1 = {1,2,3,4}
s2 = {1,2,3,5,6,7}

s3 = s2 - s1
print(s3) # {5, 6, 7}
print(s2.difference(s1)) # {5, 6, 7}

s4 = s1 & s2
print(s1.intersection(s2)) # {1, 2, 3}
print(s4) # {1, 2, 3}

s5 = s1 | s2
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7}
print(s5) # {1, 2, 3, 4, 5, 6, 7}
 # 对称差集 ----- 两个集合中不同的元素
print(s1^s2) # {4, 5, 6, 7}

# 变量的值改变，是重新指向了一个地址空间
str = 'hello'
print(id(str)) # 4335977392
str = 'hello1'
print(id(str)) # 4335985392

li = [1,2,3]
print(li, id(li)) # [1, 2, 3] 4519372928
li.pop()
print(li,id(li)) # [1, 2] 4519372928

s = {1,2,3}
print(s,id(s)) # {1, 2, 3} 4527199616
s.discard(1)
print(s,id(s)) # {2, 3} 4527199616


print('*'*20)
# str int tuple list set dict
s = 'hello'
sint = '9'
print(int(sint), type(sint)) # 9 <class 'str'>
print(list(s)) # ['h', 'e', 'l', 'l', 'o']
print(set(s)) # {'h', 'e', 'l', 'o'}
# print(tuple(s))
# print(dict(s))  # 字典需要序列才能转

l = [1,2,3]
dict1 = {1:'a',2:'b'}
s1 = {1,2,3}
t = (1,2,3)
print(tuple(s))
# print(str(l))
# print(str(dict1))
# print(str(s1))
# print(str(t))