# -*- coding:utf-8 -*-
#@Time : 2020/5/11 下午6:53
#@Author: 手写
#@File : 5.py
from sqlalchemy import Column, Table, Integer, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:11111111@localhost:3306/pythonsql')

metadata = MetaData(engine)

student = Table('student', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(50)),
                Column('age', Integer),
                Column('address', String(10))
                )
metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()
Base = declarative_base()

