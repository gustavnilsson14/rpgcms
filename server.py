import os
import tornado.ioloop
import tornado.web
import tornado.autoreload
import sys
sys.path.append( 'orm' )
from handlers import *
from database import *

'''
import logging
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
'''
if len( sys.argv ) <= 1 :
    print "Please user the start.sh script for running this server, it ensures you get a proper database dump."
    exit(0)

if __name__ == "__main__":
    database = RpgDatabase()
    port = 1337
    public_root = os.path.join(os.path.dirname(__file__), 'public')
    application = tornado.web.Application([
        (r"/", PublicHandler, dict(database=database)),
        (r"/article", ArticleHandler, dict(database=database)),
        (r"/article/([a-zA-z_]+)", ArticleHandler, dict(database=database)),
        (r"/article/([a-zA-z_]+)/([0-9]+)", ArticleHandler, dict(database=database)),
        (r"/admin", AdminHandler, dict(database=database)),
        (r"/user", UserHandler, dict(database=database)),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': public_root}),
    ])
    application.listen(port)

    tornado.autoreload.start()
    tornado.autoreload.watch("handlers.py")
    for dir, _, files in os.walk('public'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]
    tornado.ioloop.IOLoop.current().start()
