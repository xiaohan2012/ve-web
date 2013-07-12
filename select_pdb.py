import tornado.web

class SelectPDBHandler(tornado.web.RequestHandler):
    def post(self, structure_id):
        print "structure id", structure_id
        