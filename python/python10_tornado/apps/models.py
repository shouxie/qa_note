# -*- coding:utf-8 -*-
#@Time : 2020/5/12 上午11:27
#@Author: 手写
#@File : models.py

from sqlalchemy import Column, Integer, String
from python10_tornado.utils.conn import Base

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    age = Column(Integer, default=18)

    def __repr__(self):
        return 'name: {}, age: {}'.format(self.name, self.age)

# 创建表
def create_table():
    Base.metadata.create_all()

# 删除表
def drop_table():
    Base.metadata.drop_all()