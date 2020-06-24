# -*- coding:utf-8 -*-
#@Time : 2020/5/14 下午2:20
#@Author: 手写
#@File : manager.py
import tornado.ioloop
import tornado.web
from app.views import LoginHandler
from app.views import ChatHandler
import os

template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'statics')


def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/login/', LoginHandler),
            (r'/chat/', ChatHandler)
        ],
        template_path= template_path,
        static_path=static_path
    )

if __name__ == '__main__':
    app = make_app()
    app.listen(8003)
    tornado.ioloop.IOLoop.current().start()