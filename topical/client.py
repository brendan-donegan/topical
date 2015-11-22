import requests

from argparse import ArgumentParser


SERVER_URL = 'http://localhost:6543/' # TODO: Replace with yaml config


def _make_url(*args):
    return SERVER_URL + '/'.join(args)



def subscribe(args):
    subscribe_response = requests.post(_make_url(args.topic, args.user))


def unsubscribe(args):
    unsubscribe_response = requests.delete(_make_url(args.topic, args.user))


def publish(args):
    pass


def retrieve(args):
    


def main():
    parser = ArgumentParser('Subscribe to topics, post messages to '
                            'them and read messages from them.',
                            add_help=False)
    user_parser = ArgumentParser(add_help=False, parents=[parser])
    user_parser.add_argument('user')
    parser.add_argument('topic')
    subparsers = parser.add_subparsers(title='actions')
    subscribe_parser = subparsers.add_parser(
        'subscribe',
        parents=[user_parser],
        help='Subscribe to a topic'
    )
    subscribe_parser.set_defaults(func=subscribe)
    unsubscribe_parser = subparsers.add_parser(
        'unsubscribe',
        parents=[user_parser],
        help='Unsubscribe from topic'
    )
    unsubscribe_parser.set_defaults(func=unsubscribe)
    publish_parser = subparsers.add_parser(
        'publish',
        parents=[parser],
        help='Publish a message to a topic'
    )
    publish_parser.add_argument(
        'message',
        help='The message to publish'
    )
    publish_parser.set_defaults(func=publish)
    retrieve_parser = subparsers.add_parser(
        'retrieve',
        parents=[user_parser],
        help='Retrieve the next message in the topic for the user'
    )
    retrieve_parser.set_defaults(func=retrieve)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
