# -*- coding:utf-8 -*-
#@Time : 2020/5/14 下午7:27
#@Author: 手写
#@File : 1-nodelist.py

'''
数据结构-单链表：
【data， 下一个的指针】 --- data， 下一个的指针】...

'''


# 节点类 【data， 下一个的指针】
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# 单链表
class SingleList:
    def __init__(self, node=None):
        # _head 首地址
        self._head = node

    # 判断为空
    def isEmpty(self):
        return self._head == None

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self._head = node
        else:
            current = self._head
            while current.next != None:
                current = current.next
            current.next = node

    def len(self):
        count = 0
        current = self._head
        while current != None:
            count += 1
            current = current.next
        return count

    def print_all(self):
        cur = self._head
        while cur != None:
            print(cur)
            cur = cur.next

    def pop(self, index):
        if index < 0 or index > self.len():
            raise IndexError('Index Error')
        elif index == 0:
            self._head = self._head.next
        else:
            cur = self._head
            while index - 1:
                cur = cur.next
                index -= 1
            # 当前指针的前一个指针直接指向当前指针的下一个指针，此时cur为前一个
            cur.next = cur.next.next

    def inert(self, index, item):
        if index < 0 or index > self.len():
            raise IndexError('index error: range is not valid')
        elif isinstance(item, Node):
            raise TypeError('type is not valid')
        else:
            if index == 0:
                node = Node(item)
                node.next = self._head
                self._head = node
            else:
                node = Node(item)
                cur = self._head
                while index - 1:
                    cur = cur.next
                    index -= 1
                    # 当前指针的前一个指针直接指向insert指针，insert指针指向当前指针的下一个指针，此时cur为前一个
                    # 【data next】 --insert--【 data next】 -- 【 data next】
                node.next = cur.next
                cur.next = node

    def update(self, index, newItem):
        pass
    def remove(self, item):
        pass



if __name__ == '__main__':
    slist = SingleList()
    print(slist.isEmpty()) # True
    slist.append(1)
    print(slist.len()) # 1
    # slist.print_all() # TypeError: __str__ returned non-string (type int)     def __str__(self): return str(self.data)
    slist.append(2)
    slist.append(3)
    slist.print_all() # 1 2 3

    slist1 = SingleList()
    for i in range(10):
        slist1.append(i)

    slist1.print_all()
    slist1.pop(5)
    slist1.print_all()

    print('--'*10)
    slist2 = SingleList()
    for i in range(10):
        slist2.append(i)
    slist2.inert(2, 'hello python')
    slist2.print_all()