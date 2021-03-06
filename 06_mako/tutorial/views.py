from pyramid.response import Response
from pyramid.view import view_config

@view_config (route_name='home', renderer='templates/index.mako')
def home (request):
    return {'name': 'Michael Davis'}

@view_config (route_name='hello')
def hello (request):
    return Response('<body><h1>Hello World!</h1><a href="/">Go Back</a></body>')

@view_config (route_name='hi')
def hi (request):
    return Response('<body><h1>Hello World!</h1><a href="/">Go Back</a></body>')


