from pyramid.response import Response
from pyramid.view import view_config

@view_config (route_name='home')
def home (request):
    return Response('<body>Visit <a href="/howdy">Hello</a></body>')

@view_config (route_name='hello')
def hello (request):
    return Response('<body><h1>Hello World!</h1><a href="/">Go Back</a></body>')
