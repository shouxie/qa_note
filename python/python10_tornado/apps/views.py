# -*- coding:utf-8 -*-
#@Time : 2020/5/12 上午11:11
#@Author: 手写
#@File : views.py

import tornado
import tornado.web
from python10_tornado.apps.models import create_table,drop_table, Student
from python10_tornado.utils.conn import session

class CreateHandler(tornado.web.RequestHandler):
    def get(self):
        create_table()
        self.write('create success!')

class DropHandler(tornado.web.RequestHandler):
    def post(self):
        drop_table()
        self.write('drop success!')

class AddHandler(tornado.web.RequestHandler):
    def post(self):
        stu = Student()
        stu.name = 'zhangsan'
        session.add(stu)
        session.commit()
        self.write('add success!')

class BatchAddHandler(tornado.web.RequestHandler):
    def post(self):
        stus = []
        for i in range(10):
            stu = Student()
            stu.name = 'xiaoming{}'.format(i)
            stus.append(stu)
        session.add_all(stus)
        session.commit()
        self.write('batch add success!')

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        stu = session.query(Student).filter(Student.name == 'zhangsan').all()
        stu1 = session.query(Student).filter_by(name = 'xiaoming0').all()
        print(stu, stu1) # 如果没有__repr__ 打印：[<python10_tornado.apps.models.Student object at 0x105f19520>] 加上__repr__：[name: zhangsan, age: 18]
        self.write('query success!')

    def delete(self):
        stu = session.query(Student).filter(Student.name == 'zhangsan').first()
        if stu:
            session.delete(stu)
            session.commit()
            self.write('delete success!')
        session.query(Student).filter_by(name='xiaoming0').delete()
        session.commit()
        self.write('delete xiaoming0 success!')

    def patch(self):
        stu = session.query(Student).filter(Student.name == 'xiaoming1').first()
        stu.age = 20
        session.add(stu)
        session.commit()
        self.write('patch success!')

    def post(self):
        session.query(Student).filter(Student.name == 'xiaoming1').update({'age': 21})
        session.commit()
        self.write('update success!')

