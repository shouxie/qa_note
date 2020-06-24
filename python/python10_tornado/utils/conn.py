# -*- coding:utf-8 -*-
#@Time : 2020/5/12 上午11:17
#@Author: 手写
#@File : conn.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql = 'mysql+pymysql://root:11111111@localhost:3306/pythonsql'

engine = create_engine(sql)
Base = declarative_base(bind=engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()