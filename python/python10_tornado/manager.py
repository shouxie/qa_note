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