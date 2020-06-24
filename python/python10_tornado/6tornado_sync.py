# -*- coding:utf-8 -*-
#@Time : 2020/5/13 下午2:50
#@Author: 手写
#@File : 6tornado_sync.py

import tornado
import tornado.web
import tornado.httpclient
import tornado.ioloop
import tornado.httpserver
import ssl

class SyncHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            client = tornado.httpclient.HTTPClient()
            q = self.get_query_argument('q')
            ret = client.fetch('http://qa.corp.daling.com/myapp/lastbetabds/index?job_server=ALL&job={}&online=ALL'.format(q))
            print(ret)
            self.write('query success!')
        except:
            pass
        client.close()

def make_app():
    return tornado.web.Application(handlers=[
        (r'/sync/', SyncHandler)
    ])

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8002)
    server.start(1)
    tornado.ioloop.IOLoop.current().start()

    # RuntimeError: Cannot run the event loop while another loop is running
    # 解释:HTTPClient内部写 loop.run_xxx，因为那是启动event loop的命令，通常只再最最最外面用一次，之后的代码都应假设 loop 已经在运转了。