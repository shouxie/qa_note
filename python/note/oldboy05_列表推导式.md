<!--
 * @Author: shouxie
 * @Date: 2020-04-17 17:12:34
 * @Description: 
 -->
# 列表推导式
```python
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

```