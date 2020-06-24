# -*- coding:utf-8 -*-
#@Time : 2020/5/14 下午2:22
#@Author: 手写
#@File : views.py

import tornado.web
import tornado.websocket

class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        error = ''
        self.render('login.html', error=error)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username in ['user1', 'user2'] and password == '11':
            self.set_cookie('username', username)
            self.render('chat.html', username=username)
        else:
            error = '用户名密码错误'
            self.render('login.html', error=error)

class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        self.write_message('hello')

    def on_message(self, message):
        username = self.get_cookie('username')
        self.write_message('%s:%s' % (username, message))