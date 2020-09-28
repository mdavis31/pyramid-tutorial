from pyramid.config import Configurator

def main (global_config, **settings):
    config = Configurator (settings=settings)
    config.include ('pyramid_mako')

    config.add_route ('home', '/')
    config.add_route ('hello', '/howdy')
    config.add_route ('hi', '/hi')
    config.scan ('.views')
    return config.make_wsgi_app ()

