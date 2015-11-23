import requests
import socket
import time
import unittest

from subprocess import Popen
from urllib.parse import urlsplit

TOPICAL_SERVER_URL = 'http://localhost:6550'


def _wait_for_server(url, timeout=10):
    parts = urlsplit(url)
    sock = socket.socket()
    now = time.time()
    end = now + timeout
    while now < end:
        try:
            sock.connect((parts.hostname, parts.port))
        except ConnectionRefusedError:
            time.sleep(2)
            now = time.time()
        return True


def make_url(*args):
    url = TOPICAL_SERVER_URL
    for arg in args:
        url += '/{}'.format(arg)
    return url


class TopicalTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.server = Popen(['topical', '--port=6550'])
        _wait_for_server(TOPICAL_SERVER_URL)

    def tearDown(self):
        super().setUp()
        self.server.kill()

    def test_subscribe_to_topic(self):
        """
        Verify that subscribing to a topic returns succesfully.
        """
        subscribe_response = requests.post(make_url('lolcatz', 'brendand'))
        self.assertTrue(subscribe_response.ok)

    def test_subscribe_to_topic_not_existing(self):
        """
        Verify that subscribing to a topic that doesn't exist is
        succesful
        """
        subscribe_response = requests.post(make_url('star trek', 'brendand'))
        self.assertTrue(subscribe_response.ok)

    def test_subscribe_publish_and_read(self):
        """
        Verify that requesting a message for a topic returns a message if the
        user is subscribed to that topic and a message has been posted to it
        """
        user = 'brendand'
        topic = 'lolcatz'
        message = 'lolcatz r fun'
        subscribe_response = requests.post(make_url(topic, user))
        self.assertTrue(subscribe_response.ok)
        publish_response = requests.post(make_url(topic), data=message)
        self.assertTrue(publish_response.ok)
        next_message_response = requests.get(make_url(topic, user))
        self.assertEqual(next_message_response.text, message)

    def test_unsubscribe_from_topic_subscribed_to(self):
        """
        Verify that unsubscribing from a topic the user is
        subscribed to returns success
        """
        user = 'brendand'
        topic = 'lolcatz'
        subscribe_response = requests.post(make_url(topic, user))
        self.assertTrue(subscribe_response.ok)
        unsubscribe_response = requests.delete(make_url(topic, user))
        self.assertTrue(unsubscribe_response.ok)

    def test_unsubscribe_from_topic_not_subscribed_to(self):
        """
        Verify that unsubscribing from a topic returns 404
        if the user is not already subscribed to that topic.
        """
        user = 'brendand'
        topic = 'star wars'
        unsubscribe_response = requests.delete(make_url(topic, user))
        self.assertEqual(unsubscribe_response.status_code, 404)

    def test_next_message_for_topic_not_subscribed_to(self):
        """
        Verify that trying to get a message from a topic the user is not
        subscribed to returns a 404 error.
        """
        user = 'brendand'
        topic = 'star wars'
        next_message_response = requests.get(make_url(topic, user))
        self.assertEqual(next_message_response.status_code, 404)

    def test_next_message_none_available(self):
        """
        Verify that trying to get a message from a topic that the user
        is subscribed to but no messages have been published to returns
        a 204 error
        """
        user = 'brendand'
        topic = 'lolcatz'
        subscribe_response = requests.post(make_url(topic, user))
        self.assertTrue(subscribe_response.ok)
        next_message_response = requests.get(make_url(topic, user))
        self.assertEqual(next_message_response.status_code, 204)
