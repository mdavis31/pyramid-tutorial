from pyramid.config import Configurator

def main(global_config, **settings):
    print ("in here2")
    config = Configurator(settings=settings)
    config.add_route ('home', '/')
    config.add_route ('hello', '/howdy')
    config.scan ('.views')
    return config.make_wsgi_app ()
