from app import create_app, this_app
from threading import Lock
from werkzeug.wsgi import pop_path_info, peek_path_info


class PathDispatcher():
    def __init__(self, default_app, create_app):
        self.default_app = default_app
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, prefix):
        with self.lock:
            my_app = self.instances.get(prefix)
            if my_app is None:
                my_app = self.create_app(prefix)
                if my_app is not None:
                    self.instances[prefix] = my_app
            return my_app

    def __call__(self, environ, start_response):
        app = self.get_application(peek_path_info(environ))
        if app is not None:
            pop_path_info(environ)
        else:
            app = self.default_app
        return app(environ, start_response)


def make_app(prefix):
    if prefix in ['rectangle', 'circle', 'triangle']:
        return create_app(prefix)


application = PathDispatcher(this_app, make_app)
