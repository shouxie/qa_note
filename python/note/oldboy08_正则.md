<!--
 * @Author: shouxie
 * @Date: 2020-04-27 18:31:10
 * @Description: 
 -->
 ## 正则表达式的定义

 > 正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
 
##### 正则表达式的作用和特点
给定一个正则表达式和另一个字符串，我们可以达到如下的目的：
1. 给定的字符串是否符合正则表达式的过滤逻辑（称作“匹配”）；
2. 可以通过正则表达式，从字符串中获取我们想要的特定部分。

##### 正则表达式的特点是：
1. 灵活性、逻辑性和功能性非常强；
2. 可以迅速地用极简单的方式达到字符串的复杂控制。
3. 对于刚接触的人来说，比较晦涩难懂。

## python re模块

 ### match serach

match:只要从开头进行匹配，如果匹配不成功则就返回None
serach:进行正则字符串匹配方法，匹配的是整个字符串

```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午6:31
#@Author: 手写
#@File : re01.py

import re
msg = 'hello world'

result = re.compile('world')
print(result.match(msg)) # None

result1 = re.compile('hello')
print(result1.match(msg)) # <re.Match object; span=(0, 5), match='hello'>


result = re.match('hello', msg)
print(result) # <re.Match object; span=(0, 5), match='hello'>
result = re.search('hello', msg)
print(result) # <re.Match object; span=(0, 5), match='hello'>
res = re.search('world', msg)
print(res) # <re.Match object; span=(6, 11), match='world'>

print(res.span()) # 返回位置 (6, 11)
print(res.group()) # 使用group提取到匹配的内容 world
```

### 规则

[] 表示的是一个范围
search 只要有匹配的后面就不会继续进行检索，找到一个匹配的就会停止
findall 匹配整个字符串，找到一个继续向下找一直到字符串结尾

```python
print(re.search('[0-9][a-z]', '10a000000f')) # <re.Match object; span=(1, 3), match='0a'>

print(re.findall('[0-9][a-z]', '10a000000f')) # ['0a', '0f']
```

#### 正则符号
总结：
  . 任意字符除(\n)
  ^ 开头
  $ 结尾
  [] 范围  [abc]  [a-z]  [a-z*&￥]
  
  正则预定义：
  \s  空白 （空格）
  \b 边界
  \d 数字
  \w  word  [0-9a-zA-Z_]
  
  大写反面 \S  非空格  \D  非数字 。。。
  
  '\w[0-9]' ---> \w  [0-9] 只能匹配一个字母 
  
  量词：
   ``*  >=0``
   ``+  >=1``
   ``?  0,1``
   
   手机号码正则
   re.match('1[35789]\d{9}$',phone)
  
  {m} ： 固定m位
  {m,}  >=m
  {m,n}  phone > =m   phone<=n
‘+’用于将前面的模式匹配1次或多次（贪婪模式） >=1

```python
# a7a  a88a a7878a
msg = 'a7aopa88akjgka7878a'
print(re.findall('[a-z][0-9]+[a-z]',msg))  # ['a7a', 'a88a', 'a7878a']
```
\A：表示从字符串的开始处匹配
\Z：表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串。
\b：匹配一个单词边界，也就是指单词和空格间的位置。例如， 'py\b' 可以匹配"python" 中的 'py'，但不能匹配 "openpyxl" 中的 'py'。
\B：匹配非单词边界。 'py\b' 可以匹配"openpyxl" 中的 'py'，但不能匹配"python" 中的 'py'。
\d：匹配任意数字，等价于 [0-9]。  digit
\D：匹配任意非数字字符，等价于 [^\d]。not digit
\s：匹配任意空白字符，等价于 [\t\n\r\f]。 space
\S：匹配任意非空白字符，等价于 [^\s]。
\w：匹配任意字母数字及下划线，等价于[a-zA-Z0-9_]。
\W：匹配任意非字母数字及下划线，等价于[^\w]
\\：匹配原义的反斜杠\。
‘.’用于匹配除换行符（\n）之外的所有字符。
‘^’用于匹配字符串的开始，即行首。
‘$’用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾。

定义正则验证次数：
    ‘*’用于将前面的模式匹配0次或多次（贪婪模式，即尽可能多的匹配） >=0
    ‘+’用于将前面的模式匹配1次或多次（贪婪模式） >=1
    ‘？’用于将前面的模式匹配0次或1次（贪婪模式） 0 ，1
      '{m}'  用于验证将前面的模式匹配m次
       '{m,}'用于验证将前面的模式匹配m次或者多次  >=m
       '{m,n}'   用于验证将前面的模式匹配大于等于m次并且小于等于n次

    ‘*？，+？，？？’即上面三种特殊字符的非贪婪模式（尽可能少的匹配）。
    ‘{m,n}’用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次。
    ‘{m,n}？’即上面‘{m,n}’的非贪婪版本。


‘\\’：'\'是转义字符，在特殊字符前面加上\，特殊字符就失去了其所代表的含义，比如\+就仅仅代表加号+本身。
‘[]’用于标示一组字符，如果^是第一个字符，则标示的是一个补集。比如[0-9]表示所有的数字，[^0-9]表示除了数字外的字符。
‘|’比如A|B用于匹配A或B。
‘(...)’用于匹配括号中的模式，可以在字符串中检索或匹配我们所需要的内容。

Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；

非贪婪则相反，总是尝试匹配尽可能少的字符。

在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。

#### 分组

| 或者  
() 分组 （163|126|qq）  一组

()和[]区别：
(word|word|word)  区别   [163] 表示的是一个字母而不是一个单词

##### 分别提取

() 表示分组  group(1) 表示提取到第一组的内容   group(2)表示第二组的内容

#### 起名
```python
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result)
```

#### 起名的方式:  (?P<名字>正则) （？P=名字）

分组：()   ---> result.group(1) 获取组中匹配内容  
       在分组的时候还可以结合 |
```python
       result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
        print(result)
```
 
 不需要引用分组的内容：
```python
    result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>', msg)
    print(result)
    print(result.group(1))
```
引用分组匹配内容:
    1.number   \number 引用第number组的数据
```python
    msg = '<html><h1>abc</h1></html>'
    result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
    print(result)
```
    2.?P<名字>
```python
msg = '<html><h1>abc</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
print(result)
print(result.group(1))
```

    re模块：
    match    从开头匹配一次
    search   只匹配一次
    findall  查找所有
    sub(正则表达式，'新内容'，string)   替换
    split   result = re.split(r'[,:]','java:99,python:95')   在字符串中搜索如果遇到:或者,就分割
            将分割的内容都保存到列表中了

```python
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))
```