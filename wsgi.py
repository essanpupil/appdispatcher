from app import create_app
from threading import Lock
from werkzeug.exceptions import NotFound


class SubdomainDispatcher(object):

    def __init__(self, domain, create_app):
        self.domain = domain
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, host):
        host = host.split(':')[0]
        assert host.endswith(self.domain), 'Configuration error'
        subdomain = host[:-len(self.domain)].rstrip('.')
        with self.lock:
            app = self.instances.get(subdomain)
            if app is None:
                app = self.create_app(subdomain)
                self.instances[subdomain] = app
            return app

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)


def make_app(subdomain):
    if subdomain not in ['circle', 'rectangle', 'triangle']:
        return NotFound()

    # otherwise create the application for the specific template
    return create_app('templates_{}'.format(subdomain))


application = SubdomainDispatcher('geometry.local', make_app)
