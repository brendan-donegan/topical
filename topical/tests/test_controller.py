import unittest

from topical import controller

class TestTopicController(unittest.TestCase):

    def setUp(self):
        self.topic_controller = controller.TopicController()
        self.test_user = 'brendand'
        self.test_topic = 'lolcatz'
        self.test_message = 'lolcatz r fun'

    def test_subscribe_user_to_topic(self):
        self.assertTrue(
            self.topic_controller.subscribe_user_to_topic(
                self.test_user,
                self.test_topic,
            )
        )

    def test_unsubscribe_user_from_topic(self):
        self.assertTrue(
            self.topic_controller.unsubscribe_user_from_topic(
                self.test_user,
                self.test_topic,
            )
        )

    def test_publish_message_to_topic(self):
        self.assertTrue(
            self.topic_controller.publish_message_to_topic(
                self.test_message,
                self.test_topic,
            )
        )

    def test_next_message_in_topic_for_user(self):
        self.assertEqual(
            self.topic_controller.next_message_in_topic_for_user(
                self.test_user,
                self.test_topic,
            )
        )
