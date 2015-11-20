import unittest

from topical.topic import Topic
from topical.message import Message

class TestTopic(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.topic = Topic('lolcatz')

    def test_subscribe(self):
        user = 'brendand'
        topic.subscribe(user)
        self.assertIn(topic.subscribers, user)

    def test_unsubscribe(self):
        user = 'brendand'
        topic.subscribers = ['joe', 'bob', 'bill', 'brendand']
        topic.unsubscribe(user)
        self.assertNotIn(topic.subscribers, user)

    def test_add_message(self):
        message = Message('lolcatz r fun')
        topic.add_message(message)
        self.assertIn(topic.messages, message)
