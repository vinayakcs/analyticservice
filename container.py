from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, Application
from api_hosting import app

tr = WSGIContainer(app)
application = Application([
(r".*", FallbackHandler, dict(fallback=tr)),
])

if __name__ == "__main__":
  application.listen(5000)
  IOLoop.instance().start()