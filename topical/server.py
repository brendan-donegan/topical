from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def handle_topic_and_user(request):
    return Response(request.method + " " + str(request.matchdict))

def handle_topic(request):
    return Response(request.method + " " + str(request.matchdict) + " " + request.text)

def main():
    config = Configurator()
    config.add_route('topic_and_user', '/{topic}/{user}')
    config.add_route('topic', '/{topic}')
    config.add_view(handle_topic_and_user, route_name='topic_and_user')
    config.add_view(handle_topic, route_name='topic')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

if __name__ == '__main__':
    main()
