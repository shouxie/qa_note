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