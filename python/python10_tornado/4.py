# -*- coding:utf-8 -*-
#@Time : 2020/5/11 下午3:44
#@Author: 手写
#@File : 4.py

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base

create_tabel = '''
create table course(
id int primary key not NULL,
personName varchar(50),
course varchar(20)
);
'''



Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://root:11111111@localhost:3306/pythonsql?charset=utf8mb4',
    echo=True,
    max_overflow=5

)

engine.execute(create_tabel)

ret = engine.execute("select * from persons;")
print(ret.fetchall())


