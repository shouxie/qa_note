<!--
 * @Author: shouxie
 * @Date: 2020-06-19 11:36:47
 * @Description: 
--> 
web应用服务
iso七层模型
http协议基于tcp/ip协议。安全性链接

## 一 web 应用服务的认知

web应用服务基于HTTP协议/规范，实现静态资源和动态资源的请求与处理。

#### HTTP（1.0，1.1，2.0）和HTML关系：
1. 客户端封装http请求（HttpRequest），向服务端发起请求
2. 服务器接收请求之后，分析资源请求的路径，请求参数（查询参数，表单参数，json，字节流（文件）），请求方法，请求头等。
3. 服务端根据资源的请求路径读取文件的内容并生成字节码数据。并封装响应对象（HttpResponse）。
4. 客户端接收服务端的响应数据，判断请求是否成功，如果成功则显示数据（html/json/等）。

web应用服务基于HTTP协议，HTTP协议基于TCP/IP协议。因此是安全性链接

#### iso七层模型

应用层 HTTP DHCP FTP HTTPS安全协议（ssl证书） TELNET
表示层 数据表示，安全，压缩
会话层 建立，管理，终止会话 session
传输层 TCP，UDP
网络层 进行逻辑地址寻址，实现不同网络之间的路径选择
数据链路层
物理层

#### TCP/IP四层模型
应用层
传输层
网络层
数据链路层

web应用服务器：
1. 客户端发起请求**HttpRequest**
2. 服务端（Apache/Nginx/...）接收请求，根据请求的资源信息，读取文件并封装到响应对象**HttpResponse**中。
3. 客户端接收资源，分析资源的类型然后渲染

## 二 python web开发框架

python本身实现web应用服务的接口（规范），便于我们开发动态资源请求。提供的开发模块是wsgiref。此模块是所有其他高级框架中最核心的，最基本的规范。如flask基于werkzeug库实现了wsgi通信协议

### WSGI

> WSGI：web server gataway interface-web服务网关接口，负责http协议的底层通信的。

参考：https://zhuanlan.zhihu.com/p/95942024
全称Python Web Server Gateway Interface，指定了web服务器和Python web应用或web框架之间的标准接口，以提高web应用在一系列web服务器间的移植性。 具体可查看 官方文档

从以上介绍我们可以看出：

WSGI是一套接口标准协议/规范；
通信（作用）区间是Web服务器和Python Web应用程序之间；
目的是制定标准，以保证不同Web服务器可以和不同的Python程序之间相互通信
你可能会问，为什么需要WSGI？

首先，我们明确一下web应用处理请求的具体流程：

用户操作操作浏览器发送请求；
请求转发至对应的web服务器
web服务器将请求转交给web应用程序，web应用程序处理请求
web应用将请求结果返回给web服务器，由web服务器返回用户响应结果
浏览器收到响应，向用户展示
可以看到，请求时Web服务器需要和web应用程序进行通信，但是web服务器有很多种啊，Python web应用开发框架也对应多种啊，所以WSGI应运而生，定义了一套通信标准。试想一下，如果不统一标准的话，就会存在Web框架和Web服务器数据无法匹配的情况，那么开发就会受到限制，这显然不合理的。

既然定义了标准，那么WSGI的标准或规范是？

web服务器在将请求转交给web应用程序之前，需要先将http报文转换为WSGI规定的格式。

WSGI规定，Web程序必须有一个可调用对象，且该可调用对象接收两个参数，返回一个可迭代对象：

environ：字典，包含请求的所有信息
start_response：在可调用对象中调用的函数，用来发起响应，参数包括状态码，headers等


### pythonweb开发框架：

1. Django（组件最全，最强大的框架，主要用于后端服务的管理，运维（Ansible/Openstack））
2. Flask（小巧灵活的框架，可以快速开发API接口。）
3. Tornado（基于协程和单线程单进程的框架实现非阻塞的网络框架）
4. Sanic 是性能最优的web非阻塞框架。

python wsgi案例：
```python
from wsgiref.simple_server import make_server

def app(envir, start_response):
  # 核心业务
  #  生成相应的对象
  start_response('HTTP/1.1 200 ok',[('content-type','text/html')]) # 响应头
  return [b'<h3>hello,wigi</h3>'.encode(encoding='utf-8')]
httpd = make_server('0.0.0.0',8000,app)
httpd.serve_foreve(poll_interval=0.5) # 轮询监听的间隔时间
```

## 三 Flask 框架的应用

### 安装环境
```
pip install flask -i https://mirrors.aliyun.com/pypi/simple
```

### flask
创建server2.py
```python
from flask import flask

# 创建flask对象-httpd web服务对象
app = flask(__name__) # __name__ 可以是任意的小写字母表示flask应用对象名称

# 声明web服务的请求资源(指定资源访问的路由)
# RESTful 设计风格中关于资源的动作：'GET','POST','PUT','DELETE','PATCH'
@app.route('/hello' methods=['GET','POST'])

def hello():
  from flask import request
  # request 是请求对象（HttpRequest）包含请求资源的路径，请求方法，请求头，上传的表单数据，文件等信息
  # 获取请求中查询参数：
  # wsgi QUERT_STRING
  name = request.args.get('username')
  password = request.args.get('password')

  # 返回生成的html网页内容
  return '''
  <hi>用户登录的信息</h1>
  <h3>用户名： %s</h3>
  <h3>口令： %s</h3>
  ''' % (name, password)
# 启动flask的web服务器
app.run(host='0.0.0.0',port=5000)

```

#### Flask的MVC设计思想

1. 客户端发起请求之后，通过路由找到视图处理函数
2. 路由（请求资源）和视图处理函数 V（Controller），事先在app中声明
3. 在视图处理函数中根据业务需求，加载数据（Model）并渲染到模版中（view）
4. 将渲染之后的模版数据返回给客户端
   
#### Flask特有的MTV设计思想

MTV设计思想基于MVC，
- M：Model
- T：Template（View）
- V：View处理函数，Controller

```python
# -*- coding:utf-8 -*-
#@Time : 2020/6/19 下午6:47
#@Author: 手写
#@File : server2.py

from flask import Flask
from flask import request,render_template

# 创建Flask服务对象
app = Flask('hiFlask')

# 声明请求资源
@app.route('/hi', methods=['GET','POST'])
def hi():
    platform = request.args.get('platform', 'pc')
    if request.method == 'GET':
        return '''
        <h1>用户登录页面</h1>
        <form action="/hi" method="post">
            <input name="name"><br>
            <input name="pwd">
            <button>提交</button>
        </form>
        '''
    else:
        # 获取表单的参数
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        if all((name.strip() == 'qpp', pwd.strip() == '123')):
            return '''
            <h1>用户登录页面</h1>
            <h3>% s</h3>
            <h3>% s</h3>
            ''' % (name, pwd)
        else:
            return '''
            <h3>error<a href="/hi">重试</a></h3>
            '''

@app.route('/bank', methods=['GET','POST'])
def addBank():
    # 加载数据Model 交互操作
    # 渲染模板
    data = {
        'title': '绑定银行卡',
        'error_message': '暂无错误'
    }
    html = render_template('bank_edit.html',**data)
    return html

app.run('localhost', 5000)
```
不是静态的网页文件，而是一个动态的模板文件，页面中存在动态显示的变量，需要在视图函数中，指定数据渲染模板，渲染之后的html内容才是静态资源
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }} 的页面</title>
</head>
<body>
    <h2>{{ title }} 的页面</h2>
    <form action="">
        <label for="">银行名称</label>
        <input type="text" name="name"><br>
        <label for="">卡号</label>
        <input type="text" name="card_num"><br>
        <button>提交</button>
    </form>
<div class="error">
    <span>{{ error_message }}</span>
</div>
</body>
</html>
```

#### app.run函数的参数

```python
app.run('localhost',
        5000,
        True, # 默认未开启调试模式，True开启调试模式
        threaded=True, # 默认是单线程，即为False
        processes=4) # 默认只有一个进程
```
多进程和多线程不能同时开启，只能选择一种，如processes=4，同时threaded=True则会报错``cannot have a multithreaded and multi process server``
#### 请求request和响应response

#### flask-script
安装``pip install flask-script``

目录结构
```
-----mainapp
------------| __init__.py
------------| dao
------------------------|__init__.py
------------| static
------------| templates
------------| views
------------------------|__init__.py
-----server.py

```

```python
# mainapp/__init__py
from flask import Flask
app = Flask(__name__)
```
```python
# /server.py
from mainapp import app
from flask_script import Manager

if __name__ == '__main__':
  manager = Manager(app)
  manager.run()
```

执行``python server.py runserver -p/h/d``

#### flask-blueprint
blueprint 主要实现拆分多个视图函数，让同类或同一模块分到一view的脚本中。每一个模块有他自己的view处理函数的脚本

安装``pip3 install flask-blueprint``



```python
# /mainapp/views/bank.py
from flask import Blueprint
from flask import request
blue = Blueprint('bankBlue',__name__)
@blue.route('/bank', methods=['GET','POST'])
def bank():
  return '<h1>hi,bank</h1>'

@blue.route('/delbank', methods=['GET'])
def del_bank():
  bank_id = request.args.get('id')
  return '%s' % (bank_id)
```

```python
# mainapp/views/user.py
from flask import Blueprint
blue = Blueprint('userBlue', __name__)

@blue.route('/find', methods=['GET'])
def find_user():
  return 'hi,user'
```

```python
# /server.py
from flask_script import Manager
from mainapp import app
from mainapp.views import bank,user

if __name__ == '__main__':
  app.register_blueprint(bank.blue)
  app.register_blueprint(user.blue, url_prefix='/user')
  manager=Manager(app)
  manager.run()

```

在注册蓝图对象时，可以设置蓝图中路由访问的前缀。
```python
app.register_blueprint(user.blue,url_prefix='/user')
```

