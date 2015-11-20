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
        self.assertIn(user, self.topic.subscribers)

    def test_unsubscribe(self):
        user = 'brendand'
        self.topic.subscribers = ['joe', 'bob', 'bill', 'brendand']
        self.topic.unsubscribe(user)
        self.assertNotIn(user, self.topic.subscribers)

    def test_add_message(self):
        self.topic.subscribers = ['brendand']
        self.topic.add_message('lolcatz r fun')
        self.assertEqual('lolcatz r fun', self.topic.messages[0].body)
        self.assertEqual(['brendand'], self.topic.messages[0].watchers)

    def test_next_message(self):
        add_message = Message('lolcatz r fun', ['brendand'])
        self.topic.messages.append(add_message)
        message = self.topic.next_message('brendand')
        self.assertEqual('lolcatz r fun', message)

    def test_next_message_read_all(self):
        add_message = Message('lolcatz r fun', ['brendand'])
        self.topic.messages.append(add_message)
        message1 = self.topic.next_message('brendand')
        self.assertEqual('lolcatz r fun', message1)
        message2 = self.topic.next_message('brendand')
        self.assertIsNone(message2)
