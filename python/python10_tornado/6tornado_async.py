# -*- coding:utf-8 -*-
#@Time : 2020/5/13 下午2:50
#@Author: 手写
#@File : 6tornado_async.py


import tornado
import tornado.web
import tornado.ioloop
import tornado.httpclient


class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        q=self.get_query_argument('q')
        ret = client.fetch(
            'http://qa.corp.daling.com/myapp/lastbetabds/index?job_server=ALL&job={}&online=ALL'.format(q), callback=self.on_response)
        print(ret)
        self.write('query success!')

    def on_response(self, response):
        print(response)
        self.write('callback')
        self.finish()

def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', AsyncHandler)
    ])

if __name__ == '__main__':

    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()