# 继承
```python
# -*- coding:utf-8 -*-
#@Time : 2020/4/24 下午3:24
#@Author: 手写
#@File : index03.py

# book student computer
'''
 知识点：
 1. has  a
    一个类中使用了另外一种自定义的类型

    student使用computer  book
2. 类型：
    系统类型：
       str  int  float
       list  dict  tuple  set
    自定义类型：
        算是自定义的类，都可以将其当成一种类型
        s = Student()
        s是Student类型的对象
a = 12 # 是把int类型中的一个12这个对象赋给a
self.book = book # 是把自定义类型Book实例化出来的book对象赋给self.book
'''
class Book:
    def __init__(self, bName, num):
        self.name = bName
        self.number = num

    def __str__(self):
        return '{}本{}书'.format(self.number, self.name)

class Computer:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def __str__(self):
        return '电脑是{}，品牌是{}'.format(self.name, self.brand)

class Student:

    def __init__(self, name, book, computer):
        self.name = name
        self.book = book
        self.computer = computer

    def myHave(self):
        print('{}有{},{}'.format(self.name,self.computer,self.book))


book = Book('盗墓笔记', 10)
computer = Computer('MAC', 'mac pro')
s = Student('zhangsan', book, computer)
s.myHave() # zhangsan有电脑是MAC，品牌是mac pro,10本盗墓笔记书

print('*'*30)

# 案例
class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网....')

    def __str__(self):
        return self.brand + '---' + self.type + "---" + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '----' + str(self.number)


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过此书！')
                break
        else:
            # 将参数book添加到列表中
            self.books.append(book)
            print('添加成功！')

    def show_book(self):
        for book in self.books:  # book就是一个book对象
            print(book.bname)

    def __str__(self):
        return self.name + "---" + str(self.computer) + '--------' + str(self.books)


# 创建对象
computer = Computer('mac', 'mac pro 2018', '深灰色')

book = Book('盗墓笔记', '南派三叔', 10)

stu = Student('songsong', computer, book)
print(stu)

# 看借了哪些书
stu.show_book()

book1 = Book('鬼吹灯', '天下霸唱', 8)

stu.borrow_book(book1)

print('---------------------')

stu.show_book()

list1 = [12, 'abc', [1, 2, 3], book, computer]

```