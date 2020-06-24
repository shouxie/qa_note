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