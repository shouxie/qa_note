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

    def write_error(self, status_code, **kwargs):
        self.write('status_code{}'.format(status_code))


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/(\w+)', ReverseHandle),
        (r'/index/(\w+)/(\w+)', IndexHandle)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()