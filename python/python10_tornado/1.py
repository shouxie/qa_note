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
