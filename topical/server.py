from argparse import ArgumentParser

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPNoContent
import yaml

from topical.controller import TopicController

# TODO: Get this out of the module level
with open('topical.yml', 'r') as stream:
    topics_config = yaml.load(stream)
topic_controller = TopicController(topics_config['topics'])


def subscribe(request):
    """
    Handle request to subscribe user to a topic
    """
    topic_controller.subscribe_user_to_topic(
        request.matchdict['user'],
        request.matchdict['topic'],
    )
    return Response()


def unsubscribe(request):
    """
    Handle request to unsubscribe user from topic
    """
    result = topic_controller.unsubscribe_user_from_topic(
        request.matchdict['user'],
        request.matchdict['topic'],
    )
    if not result:
        raise HTTPNotFound()
    return Response()

def retrieve_message(request):
    """
    Handle request to retrieve next message in topic
    """
    message = topic_controller.next_message_in_topic_for_user(
        request.matchdict['user'],
        request.matchdict['topic'],
    )
    if message is None:
        raise HTTPNoContent()
    return Response(message)

def publish(request):
    """
    Handle request to publish mesage to topic
    """
    topic_controller.publish_message_to_topic(
        request.matchdict['topic'],
        request.text
    )
    return Response()


def main():
    parser = ArgumentParser('A publish/subscribe message server.')
    parser.add_argument('--port', '-p',
                        default=8080,
                        type=int,
                        help='The port to run on.')
    args = parser.parse_args()
    config = Configurator()
    # Add route for handling requests with a topic and a user
    config.add_route('topic_and_user', '/{topic}/{user}')
    # Add route for handling requests with just a user
    config.add_route('topic', '/{topic}')
    config.add_view(subscribe,
                    route_name='topic_and_user',
                    request_method='POST')
    config.add_view(unsubscribe,
                    route_name='topic_and_user',
                    request_method='DELETE')
    config.add_view(retrieve_message,
                    route_name='topic_and_user',
                    request_method='GET')
    config.add_view(publish,
                    route_name='topic',
                    request_method='POST')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', args.port, app)
    print('running on port {port}'.format(port=args.port))
    server.serve_forever()

if __name__ == '__main__':
    main()
