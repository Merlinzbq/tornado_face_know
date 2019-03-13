import os

import tornado.web
import tornado.ioloop

from app.views import LoginHandler, RegisterHandler, InitDbHandler


def make_app():
    return tornado.web.Application(handlers=[
        (r'/init_db/', InitDbHandler),
        (r'/login/', LoginHandler),
        (r'/register/', RegisterHandler),
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
