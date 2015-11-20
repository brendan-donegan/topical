import unittest

from topical.topic import Topic
from topical.message import Message

class TestTopic(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.topic = Topic('lolcatz')

    def test_subscribe(self):
        user = 'brendand'
        self.topic.subscribe(user)
        self.assertIn(self.topic.subscribers, user)

    def test_unsubscribe(self):
        user = 'brendand'
        self.topic.subscribers = ['joe', 'bob', 'bill', 'brendand']
        self.topic.unsubscribe(user)
        self.assertNotIn(self.topic.subscribers, user)

    def test_add_message(self):
        message = Message('lolcatz r fun')
        self.topic.add_message(message)
        self.assertIn(self.topic.messages, message)
