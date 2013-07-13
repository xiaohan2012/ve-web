import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="port number", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("server.html")
        
if __name__ == '__main__':
    from select_pdb import SelectPDBHandler
    
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r"/", IndexHandler),
            (r"/select-pdb/(\w+)", SelectPDBHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "assets"),
        debug = True
    )

    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
