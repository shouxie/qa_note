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
        print(self.get_query_argument('greeting'), self.get_query_arguments('greeting'))

    def post(self):
        a = self.get_argument('a')
        self.write(a)
        # 1['1', '1']
        # 1['1']
        print(self.get_argument('a'), self.get_arguments('a'), self.get_body_argument('a'), self.get_body_arguments('a'))


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

