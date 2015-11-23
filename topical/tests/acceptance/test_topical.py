import requests
import socket
import time
import unittest

from subprocess import Popen
from urllib.parse import urlsplit

TOPICAL_SERVER_URL = 'http://localhost:6550'

TEST_USER = 'brendand'
TEST_USER2 = 'nadnerb'
TEST_TOPIC = 'lolcatz'
TEST_TOPIC_NOT_EXISTING = 'star trek'
TEST_MESSAGE = 'lolcatz r fun'


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
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)

    def test_subscribe_to_topic_not_existing(self):
        """
        Verify that subscribing to a topic that doesn't exist is
        succesful
        """
        subscribe_response = requests.post(
            make_url(TEST_TOPIC_NOT_EXISTING, TEST_USER)
        )
        self.assertTrue(subscribe_response.ok)

    def test_subscribe_publish_and_read(self):
        """
        Verify that requesting a message for a topic returns a message if the
        user is subscribed to that topic and a message has been posted to it
        """
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)
        publish_response = requests.post(
            make_url(TEST_TOPIC), data=TEST_MESSAGE
        )
        self.assertTrue(publish_response.ok)
        next_message_response = requests.get(make_url(TEST_TOPIC, TEST_USER))
        self.assertEqual(next_message_response.text, TEST_MESSAGE)

    def test_unsubscribe_from_topic_subscribed_to(self):
        """
        Verify that unsubscribing from a topic the user is
        subscribed to returns success
        """
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)
        unsubscribe_response = requests.delete(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(unsubscribe_response.ok)

    def test_unsubscribe_from_topic_not_subscribed_to(self):
        """
        Verify that unsubscribing from a topic returns 404
        if the user is not already subscribed to that topic.
        """
        unsubscribe_response = requests.delete(make_url(TEST_TOPIC, TEST_USER))
        self.assertEqual(unsubscribe_response.status_code, 404)

    def test_next_message_for_topic_not_subscribed_to(self):
        """
        Verify that trying to get a message from a topic the user is not
        subscribed to returns a 404 error.
        """
        next_message_response = requests.get(make_url(TEST_TOPIC, TEST_USER))
        self.assertEqual(next_message_response.status_code, 404)

    def test_next_message_none_available(self):
        """
        Verify that trying to get a message from a topic that the user
        is subscribed to but no messages have been published to returns
        a 204 error
        """
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)
        next_message_response = requests.get(make_url(TEST_TOPIC, TEST_USER))
        self.assertEqual(next_message_response.status_code, 204)

    def test_unsubscribe_user_does_not_receive_messages(self):
        """
        Verify that unsubscribing a user from a topic means they don't get
        any more messages from that topic and a 404 is returned (as they
        aren't subscribed anymore.
        """
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)
        publish_response = requests.post(
            make_url(TEST_TOPIC), data=TEST_MESSAGE
        )
        self.assertTrue(publish_response.ok)
        unsubscribe_response = requests.delete(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(unsubscribe_response.ok)
        next_message_response = requests.get(make_url(TEST_TOPIC, TEST_USER))
        self.assertEqual(next_message_response.status_code, 404)

    def test_next_message_multiple_users(self):
        """
        Verify that if two users are waiting for a message then both
        receive it.
        """
        subscribe_response = requests.post(make_url(TEST_TOPIC, TEST_USER))
        self.assertTrue(subscribe_response.ok)
        subscribe_response2 = requests.post(make_url(TEST_TOPIC, TEST_USER2))
        self.assertTrue(subscribe_response2.ok)
        publish_response = requests.post(
            make_url(TEST_TOPIC), data=TEST_MESSAGE
        )
        self.assertTrue(publish_response.ok)
        next_message_first_response = requests.get(
            make_url(TEST_TOPIC, TEST_USER)
        )
        self.assertTrue(next_message_first_response.ok)
        self.assertEqual(next_message_first_response.text, TEST_MESSAGE)
        next_message_second_response = requests.get(
            make_url(TEST_TOPIC, TEST_USER2)
        )
        self.assertTrue(next_message_second_response.ok)
        self.assertEqual(next_message_second_response.text, TEST_MESSAGE)
