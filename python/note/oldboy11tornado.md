<!--
 * @Author: shouxie
 * @Date: 2020-05-07 14:38:40
 * @Description: 
 -->

# tornado

## request


### 命令行
define： 定义默认的命令行参数，type=int为校验
options: 获取命令行的参数
parse_command_line: 解析命令行
如果用户运行程序时使用了--help选项，程序将打印出所有你定义的选项以及你在define函数的help参数中指定的文本

```python

from tornado.options import define, options, parse_command_line

define('port', default=8080, type=int, help='hhh')
if __name__ == '__main__':
    parse_command_line()
    port = options.port

```

### 请求

处理请求的类继承自tornado.web.RequestHandler,重写get请求或者其他方式
self.write() 处理响应
tornado.web.Application() 创建一个应用，接收一个handles参数，类型是元组形式的列表，其中
(路由匹配规则（通常会包含正则）, 处理请求的类)

```python

import tornado.web

class mainHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')

if __name__ == '__main__':
    tornado.web.Application(handler=[
        (r'/', mainHandle)
    ])

```

```python
'''
@Author: shouxie
@Date: 2020-05-08 18:12:25
@Description: 
'''
# -*- coding:utf-8 -*-
#@Time : 2020/5/7 下午3:50
#@Author: 手写
#@File : 1.py

import tornado.web
import tornado.ioloop
from tornado.options import define, options,parse_command_line

# 定义默认端口
define('port', default=8080, type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello tornado')
        print(self)
        print(self.get_argument('name'))
        print(self.get_arguments('name'))
        print(self.get_query_arguments('name'))
        print(self.get_query_argument('name'))

    def post(self):
        self.write('hello tornado post')
        print(self.get_argument('name'), self.get_arguments('name'), self.get_body_arguments('name'), self.get_body_argument('name'))


class otherHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')
        # 设置返回状态码
        # self.set_status(404)
        # 设置cookie
        self.set_cookie('token', '123')
        self.clear_cookie('token')
        self.clear_all_cookies()

class ReverseHandle(tornado.web.RequestHandler):

    def get(self, *path):
        '''
        :param path:
        :return:
        '''
        print(path)

        # self.write(path[::-1])
        for i in path:
            self.write(str(i)[::-1]) # olleh321
        '''
        r'/reverser/(\w+)'
        http://localhost:3333/reverser/hello
        ====
        olleh
        
        r'/reverser/(\w+)/(\d+)'
        http://localhost:3333/reverser/hello/123
        print(path):
        ('hello', '123')
        '''


def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/', MainHandler),
            (r'/reverser/(\w+)/(\d+)', ReverseHandle),
            (r'/other', otherHandle)
        ]
    )

if __name__ == '__main__':
    # 解析命令行参数
    parse_command_line()
    app = make_app()
    # 监听命令行参数 port
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

```
### 获取参数

- get:
    - self.get_argument(参数名, defaultValue) # 获取参数最新的值
    - self.get_arguments(参数名) # 获取参数所有的值，并且放在列表中
    
        '''
        
        运行结果：
        
         http://localhost:8081/ : []
         
         http://localhost:8081/?greeting=1&greeting=2: ['1', '2']
        '''
    - self.get_query_arguments(参数名) # 只能用在get请求
    - self.get_query_argument(参数名, defaultValue) # 只能用在get请求
- post:
    - self.get_argument(参数名)
    - self.get_arguments(参数名) # 获取参数(也包含query)所有的值，并且放在列表中
    - self.get_body_argument(参数名)
    - self.get_body_arguments(参数名) # 获取body参数所有的值，并且放在列表中
```python
# -*- coding:utf-8 -*-
#@Time : 2020/5/8 下午6:36
#@Author: 手写
#@File : 2.py

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options, parse_command_line

define('port', default='8081', type=int, help='run on the given port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        print(self.get_arguments('greeting'))
        '''
         http://localhost:8081/ : []
         http://localhost:8081/?greeting=1&greeting=2: ['1', '2']
        '''
        self.write('{}, friendly user!'.format(greeting))

if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



```

### url正则
Tornado在元组中使用正则表达式来匹配HTTP请求的路径。（这个路径是URL中主机名后面的部分，不包括查询字符串和碎片。）Tornado把这些正则表达式看作已经包含了行开始和结束锚点（即，字符串"/"被看作为"^/$"）。
如果一个正则表达式包含一个捕获分组（即，正则表达式中的部分被括号括起来），匹配的内容将作为相应HTTP请求的参数传到RequestHandler对象中
def get(self, input):
```python
# -*- coding:utf-8 -*-
#@Time : 2020/5/8 下午7:51
#@Author: 手写
#@File : 3.py

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define, parse_command_line

define('port', default=8081, help='aaa', type=int)


class ReverseHandle(tornado.web.RequestHandler):
    def get(self, path):
        self.write(path[::-1]) # http://localhost:8081/test  tset

class IndexHandle(tornado.web.RequestHandler):
    def get(self, *paths):
        for i in paths:
            print(i)


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/(\w+)', ReverseHandle),
        (r'/index/(\w+)/(\w+)', IndexHandle)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

### 设置状态码和cookie等

```python

import tornado.web

class otherHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')
        # 设置返回状态码
        # self.set_status(404)
        # 设置cookie
        self.set_cookie('token', '123')
        self.clear_cookie('token')
        self.clear_all_cookies()
```

### HTTP方法

get
post
delete
put
patch

PATCH和PUT方法的区别：
什么是局部更新？

比如我在一个restful的编辑页面，进行更新操作，用put和PATCH都能成功，可是不太理解什么叫局部。

patch方法用来更新局部资源，这句话我们该如何理解？

假设我们有一个UserInfo，里面有userId， userName， userGender等10个字段。可你的编辑功能因为需求，在某个特别的页面里只能修改userName，这时候的更新怎么做？

人们通常(为徒省事)把一个包含了修改后userName的完整userInfo对象传给后端，做完整更新。但仔细想想，这种做法感觉有点二，而且真心浪费带宽(纯技术上讲，你不关心带宽那是你土豪)。

于是patch诞生，只传一个userName到指定资源去，表示该请求是一个局部更新，后端仅更新接收到的字段。

而put虽然也是更新资源，但要求前端提供的一定是一个完整的资源对象，理论上说，如果你用了put，但却没有提供完整的UserInfo，那么缺了的那些字段应该被清空

补充:

最后再补充一句，restful只是标准，标准的意思是如果在大家都依此行事的话，沟通成本会很低，开发效率就高。但并非强制(也没人强制得了)，所以你说在你的程序里把方法名从put改成patch没有任何影响，那是自然，因为你的后端程序并没有按照标准对两个方法做不同处理，她的表现自然是一样的


### HTTP状态码

>可以使用RequestHandler类的set_status()方法显式地设置HTTP状态码。然而在某些情况下，Tornado会自动地设置HTTP状态码
404 Not Found
Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not Found）响应码。

- 400 Bad Request

   - 如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，Tornado将自动返回一个400（Bad Request）响应码。

- 405 Method Not Allowed

  - 如果传入的请求使用了RequestHandler中没有定义的HTTP方法（比如，一个POST请求，但是处理函数中只有定义了get方法），Tornado将返回一个405（Methos Not Allowed）响应码。

- 500 Internal Server Error

  - 当程序遇到任何不能让其退出的错误时，Tornado将返回500（Internal Server Error）响应码。你代码中任何没有捕获的异常也会导致500响应码。

- 200 OK

  - 如果响应成功，并且没有其他返回码被设置，Tornado将默认返回一个200（OK）响应码。


当上述任何一种错误发生时，Tornado将默认向客户端发送一个包含状态码和错误信息的简短片段。如果你想使用自己的方法代替默认的错误响应，你可以重写write_error方法在你的RequestHandler类中
```python
def write_error(self, status_code, **kwargs):
    self.write('status_code{}'.format(status_code))

```

### 切入点函数

initialize

prepare

on_finish

### 模板

### sqlalchemy

#### ORM技术：

> 即Object-Relationl Mapping，它的作用是在关系型数据库和对象之间作一个映射，这样，我们在具体的操作数据库的时候，就不需要再去和复杂的SQL语句打交道，只要像平时操作对象一样操作它就可以了 

- 持久化:
> 持久（Persistence），即把数据（如内存中的对象）保存到可永久保存的存储设备中（如磁盘）。持久化的主要应用是将内存中的数据存储在关系型的数据库中，当然也可以存储在磁盘文件中、XML数据文件中等等
- 持久层:
> 持久层（Persistence Layer），即专注于实现数据持久化应用领域的某个特定系统的一个逻辑层面，将数据使用者和数据实体相关联

在Python中，最有名的ORM框架是SQLAlchemy
————————————————————————

入门：
mysql





```mysql
create database pythonsql;
show tables;
create table persons(
id int(11) not NULL primary key auto_increment,
name varchar(50),
sex int(2),
phone varchar(20)
);

insert into persons(id,name,sex,phone) values(1,'py1', 1, '18811502787');

```
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
'mysql+pymysql://root:11111111@localhost:3306/pythonsql?charset=utf8mb4',
echo=True
)

ret = engine.execute('select * from persons;')
print(ret.fetchall()) # [(1, 'py1', 1, '1881162207')]

```

#### sqlalchemy 增删改查

结构：
- apps
  - models.py # 模型，对应数据库
  - views.py # 处理请求RequestHandler
- utils
  - conn.py # 数据库连接操作
- manager.py # 入口

```python
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
```

```python
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



```

```python

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
```

```python

# -*- coding:utf-8 -*-
#@Time : 2020/5/12 上午11:07
#@Author: 手写
#@File : manager.py

import tornado
from tornado import ioloop
import tornado.web
from tornado.options import options, define, parse_command_line
from python10_tornado.apps.views import CreateHandler, DropHandler,AddHandler, BatchAddHandler, QueryHandler

define('port', default=8000, type=int)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/create', CreateHandler),
        (r'/drop', DropHandler),
        (r'/add', AddHandler),
        (r'/batchAdd', BatchAddHandler),
        (r'/query', QueryHandler)
    ])

if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
```

#### 几个概念


并发：同一个时间，单CPU只执行一个任务

并行：多CPU同时执行不同任务


同步和异步针对结果而言:

    同步: 对请求结果来说，上一步的操作必须执行完毕，下一步才能执行
    异步: 下一步的操作不需要等待上一步的完成


阻塞和非阻塞针对线程的状态而言:

	阻塞: 线程没有资源，因此挂起并不执行

	非阻塞： 线程有资源，一直运行

Tornado是异步非阻塞的框架

同步
```python

# -*- coding:utf-8 -*-
#@Time : 2020/5/13 下午2:50
#@Author: 手写
#@File : 6tornado_sync.py

import tornado
import tornado.web
import tornado.httpclient
import tornado.ioloop
import tornado.httpserver
import ssl

class SyncHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            client = tornado.httpclient.HTTPClient()
            q = self.get_query_argument('q')
            ret = client.fetch('http://qa.corp.daling.com/myapp/lastbetabds/index?job_server=ALL&job={}&online=ALL'.format(q))
            print(ret)
            self.write('query success!')
        except:
            pass
        client.close()

def make_app():
    return tornado.web.Application(handlers=[
        (r'/sync/', SyncHandler)
    ])

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8002)
    server.start(1)
    tornado.ioloop.IOLoop.current().start()

    # RuntimeError: Cannot run the event loop while another loop is running
    # 解释:HTTPClient内部写 loop.run_xxx，因为那是启动event loop的命令，通常只再最最最外面用一次，之后的代码都应假设 loop 已经在运转了。
```

异步：
```python

# -*- coding:utf-8 -*-
#@Time : 2020/5/13 下午2:50
#@Author: 手写
#@File : 6tornado_async.py


import tornado
import tornado.web
import tornado.ioloop
import tornado.httpclient


class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        q=self.get_query_argument('q')
        ret = client.fetch(
            'http://qa.corp.daling.com/myapp/lastbetabds/index?job_server=ALL&job={}&online=ALL'.format(q), callback=self.on_response)
        print(ret)
        self.write('query success!')

    def on_response(self, response):
        print(response)
        self.write('callback')
        self.finish()

def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', AsyncHandler)
    ])

if __name__ == '__main__':

    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()
```

用同步的语法实现异步
```python

# -*- coding:utf-8 -*-
#@Time : 2020/5/13 下午5:47
#@Author: 手写
#@File : 6tornado_async2.py

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpclient

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.web.gen.coroutine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        q = self.get_query_argument('q')
        ret = client.fetch('http://qa.corp.daling.com/myapp/lastbetabds/index?job_server=ALL&job={}&online=ALL'.format(q))
        print(ret)
        self.write('query success!')

def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler)
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()
```
