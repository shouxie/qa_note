<!--
 * @Author: shouxie
 * @Date: 2020-06-23 18:24:07
 * @Description: 
--> 
### 1.1 路由规则

使用路由的案例
```python
@blue.route('/find')
def find():
return ""
```

#### 1.1.1 路由中path中的参数
语法：
```python
@app.route('/find/<converter:word>', methods=['GET'])
def find(word):
  return ''
```
converter 是参数的转换器，一般是指定的类型，如string，**int**，**float**，**path**，uuid，any。目前最新的版本不支持any()动作，直接写成``/find/<word>/`` word表示任意类型。



其中any 比较特殊，可以指定任意的类型转换器，如<any(int),string,uuid:word>
另外，path的转换器主要用于引用别的网址时使用。
```python
@app.route('/forward/<path:url>')
def forward(url):
  # 重定向url
  return redirect(url)
```
以上路由配置，对于/forward/http:www.baidu.com，这个路径，是合法的。如果将path转换器换成string有可能会出错。
path中可以接受多个参数

#### 1.1.2 路由的请求方法

路由中请求方法通过methods设置的，而且是list类型。
```python
@app.route('/find', methods=['GET'])
def find():
  pass
```
注册路由时没有指定methods，默认包含GET和OPTIONS。

常见的请求方法：

- GET 查询数据使用。可上传的参数大小限1M以内。参数是显示在我们的请求地址中
- POST 添加或者编辑数据时使用，可以上传超过1G的大数据。且以表单参数的方式上传，并不显示在请求地址中。相比GET参数比较安全且数据量大或文件。
- PUT 更新数据时使用，局部数据的修改，如修改用户的口令或头像
- PATCH 批量更新时候使用，整体的数据修改，如修改用户的收货地址等
- DELETE 删除数据操作。
- 其他的方法：OPTIONS，HEAD

如声明一个处理函数，用于删除银行信息，正确的路由配置

```python
@app.route('/del/<int:bank_id>', methods=['DELETE'])
def delete4id(bank_id):
  return '删除操作成功'
```
针对PUT/DELETE/POST/GET等url接口测试，可以使用requests库。

```
pip install requests
```
requests库中提供了相关的函数，函数的名称与请求方法是一一对应的，当然也可以使用requests.request()方法，是最全的方法。其他的函数都是在request()方法之上去重新封装的。
```python
# -*- coding:utf-8 -*-
#@Time : 2020/6/24 下午5:57
#@Author: 手写
#@File : test_bank.py

from unittest import TestCase

import requests

# 声明单元测试类
class TestBank(TestCase):
    # 声明单元测试方法 方法名要以test_开头
    def test_del(self):
        url = "http://localhost:5000/bank/delbank/1"
        method='DELETE'
        resp = requests.request(method,url)
        # 断言 最后一个参数表示断言失败的信息。
        self.assertIs(resp.status_code,200,'请求失败')

        print(resp.text)
```
也可以使用请求方法对应的requests库的相关函数``resp = requests.delete(url)``

#### 1.1.3 路由的反向解析
```python
from flask import url_for
from flask import Blueprint
blue = Blueprint('myBlueName',__name__)

@blue.route('/add/<bankName>')
def add(bankName):
  ...

@blue.route('/select')
def select():
  return '<a href=%s></a>进入下一个页面' % url_for('myBlueName.add', bankName='中国银行')
```
url_for('函数名'， **kwargs) 反向解析获取flask的路由注册的路径

url_for('蓝图名.函数名', **kwargs) 反向解析指定蓝图下的路由注册的路径

### 1.2 请求对象
```python
from flask import request
```
请求对象本质上是客户端发送的请求数据。在flask中由Werkzeug库（实现了Python的WSGI接口）封装的，包含请求的路径，请求的方法，请求的头，请求中包含的Cookie，请求的参数以及上传的数据。
一个请求对象包含的数据的属性一般都是字典dict类型。如：
request.args 查询参数，url路径中使用？分割的查询参数
request.form 表单参数，一般是post请求方法中包含的数据
- request.headers 请求头
- request.cookies cookie 数据
- request.files 上传的文件
- request.method 请求方法，且是大写字母表示
- request.url 请求的路径http://localhost:8000/find?page=1
- request.base_url http://localhost:8000/find去掉get参数的url 
- request.host_url http://localhost:8000
- request.path /find find/item
- request.remote_addr 客户端IP地址
  
```python
  # -*- coding:utf-8 -*-
#@Time : 2020/6/21 下午6:11
#@Author: 手写
#@File : user.py
from flask import Blueprint
from flask import request

# 创建蓝图的时候，第一个参数：name
# 第二个参数：必须视图__name__，表示导包的名称
blue = Blueprint('userBlue', __name__)

@blue.route('/find',methods=['GET','POST'])
def user():
    print('url', request.url)
    print('base_url', request.base_url)
    print('host_url', request.host_url)
    print('path', request.path)
    return '<h2>user</h2>'

'''
url http://localhost:5000/user/find?name=hello
base_url http://localhost:5000/user/find
host_url http://localhost:5000/
path /user/find

'''
```
### 1.3 响应对象 response
在服务端，当业务处理完成后，生成响应的数据并封装程响应对象。并传给python的WSGI由WSGI向客户端发送数据流。
1. 直接返回文本和状态码
   flask处理函数如果直接返回文本或附带一个状态码，则会自动封装一个简单的Response对象，且数据类型默认为text/html;charset=utf-8
   ```python
    @blue.route('/publish', methods=['POST'])
    def publish():
      return '预发布银行公告', 200
   ```
   如果返回的是一个html文本数据，可以使用render_template()函数，将写好的html模板经过渲染之后生成的html返回

2. 使用make_response(data,code)生成response对象
   这种方式是最常用的方式。通过生成的response响应对象，可以设置响应的headers相关的信息
   ```python
   # -*- coding:utf-8 -*-
    #@Time : 2020/6/21 下午5:53
    #@Author: 手写
    #@File : bank_dao.py

    from flask import  Blueprint
    from flask import request, jsonify,make_response
    from dao import bank_dao

    blue = Blueprint(
        'bankBlue',__name__
    )

    @blue.route('/publish', methods=['POST'])
    def publish():
        data = '{"id":1001,"age":20}'
        code = 200
        # 将数据和状态码封装到resp对象中
        response = make_response(data,code)
        # 根据数据类型设置响应头
        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return response
        # return 'hello' 200
   ```
   
3.jsonify() 快速生成json响应对象
此函数返回的也是一个response 对象，只不过response对象的headers已经设置了content-type属性为application/json
```python
@blue.route('/publish', methods=['POST'])
def publish():
    data = '{"id":1001,"age":20}'
    code = 200
    return jsonify(data,code)
    # return 'hello' 200
```
4 Response类 生成响应对象
```python
# -*- coding:utf-8 -*-
#@Time : 2020/6/21 下午5:53
#@Author: 手写
#@File : bank_dao.py

from flask import  Blueprint
from flask import request, jsonify,make_response
from dao import bank_dao
from flask import Response

blue = Blueprint(
    'bankBlue',__name__
)

@blue.route('/publish', methods=['POST'])
def publish():
    data = '{"id":1001,"age":20}'
    code = 200
    '''
     def __init__(
        self,
        response=None,
        status=None,
        headers=None,
        mimetype=None,
        content_type=None,
        direct_passthrough=False,
    ):
    '''
    response = Response(data, code, content_type='application/json')
```
创建Response对象方法中，可以省略code，同时也可以将content_type 改为mimetype
mimetype表示的文件的数据类型，和content_type表示的含义相同

5. redirect 重定向
6. 在一个请求中，由于业务处理的要求，在处理业务之后，需要进入新的页面，而这个页面之前已经声明他的路由，则需要使用重定向的方式进入到下一页
  注意：重定向也是响应对象，必须要返回。而且相对于浏览器或者客户端再次发送新的请求。
```python
@blue.route('/add', methods=['GET','POST'])
def addCard():
    if request.method == 'POST':
        bankId = request.form.get('bank')
        username = request.form.get('username')

        # return redirect('list')

        return redirect(url_for('bankBlue.publish'))
    return render_template()
```
### 1.4 请求异常
在请求处理过程中，验证某一数据出现的错误，可以中断请求。如果请求异常不是请求数据引起的，或者说请求资源不存在，或者服务器发生异常，此时可以捕获异常。
#### 1.4.1 abort() 中断
在请求处理函数中，可以直接调用abort()函数。

```python
# abort(403) 发出一个异常响应码
abort(Response('手机号不能被注册'), 401)
```
abort(status_code)
abort(Response(data,code,headers,...))

#### 1.4.2 捕获请求异常
通过相关的状态码获取请求异常，并指定处理函数来响应异常的信息
```python
from mainapp import app
'''
mainapp -- __init__.py
from flask import Flask
app = Flask(__name__)
'''
@app.errorhandler(404) # 指定状态码捕获
def notfounded(error):
    print(error)
    return '404'

@app.errorhandler()
```

如果处理业务中抛出相关的异常或者发生500异常则可以指定异常或状态码
```python
from flask import Flask
app = Flask(__name__)

@app.errorhandler(Exception)
def handleError(error):
  print(error) # 异常
  return 'error'
```
```python
from flask import Blueprint
blue = Blueprint('testBlue', __name__)
@blue.route('/find')
def find():
  raise Exception('异常')
```


