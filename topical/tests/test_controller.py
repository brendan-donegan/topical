import unittest

from topical import controller

class TestTopicController(unittest.TestCase):

    def setUp(self):
        self.topic_controller = controller.TopicController()

    def test_subscribe(self):
        user = 'brendand'
        topic = 'lolcatz'
        self.assertTrue(self.topic_controller.subscribe(user, topic))

    def test_unsubscribe(self):
        user = 'brendand'
        topic = 'lolcatz'
        self.assertTrue(self.topic_controller.unsubscribe(user, topic))

    def test_publish(self):
        topic = 'lolcatz'
        message = 'lolcatz r fun'
        self.assertTrue(self.topic_controller.publish(message, topic))
