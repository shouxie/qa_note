# -*- coding:utf-8 -*-
# @Time : 2020/5/15 上午10:45
# @Author: 手写
# @File : 2-doubleNodelist.py

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class DoubleList:

    def __init__(self, node=None):
        self._head = node

    def isEmpty(self):
        return self._head == None

    def append(self, item):
        node = Node(item)
        cur = self._head
        if self.isEmpty():
            self._head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        # pass
        node = Node(item)
        if self.isEmpty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def print_all(self):
        cur = self._head
        while cur != None:
            print(cur)
            cur = cur.next

    def remove(self, item):

        if self.isEmpty():
            raise ValueError('the list is empty')
        else:
            cur = self._head
            # 头节点
            if cur.data == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
            else:

                while cur != None:
                    if cur.data == item:
                        if cur.next != None:
                            cur.prev.next = cur.next
                            cur.next.prev = cur.prev
                            break
                        else:
                            pass
                            cur = None
                            # print(cur, cur.prev)
                            # cur.prev.next = None
                            # cur.prev.next = None
                            break
                    cur = cur.next

    def len(self):
        cur = self._head
        index = 0
        while cur != None:
            index += 1
            cur = cur.next
        return index


    def insert(self, index, item):
        if index < 0 or index > self.len():
            raise IndexError('error')
        elif index == 0:
            cur = self._head
            node = Node(item)
            cur.prev = node
            node.next = cur
            self._head = node
        else:
            cur = self._head
            node = Node(item)
            # while index < self.len():
            while index - 1:
                pass
            # pass


if __name__ == '__main__':
    dlist = DoubleList()
    dlist.append(1)
    dlist.append(2)
    dlist.add(3)
    dlist.add(6)
    dlist.print_all()
    print('---remove---' * 3)
    dlist.remove(2)
    dlist.print_all()
    print(dlist.len())
