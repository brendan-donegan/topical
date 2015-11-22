import unittest

from topical import controller, manager


class TestTopicController(unittest.TestCase):

    def setUp(self):
        self.test_user = 'brendand'
        self.test_topic_name = 'lolcatz'
        self.test_message = 'lolcatz r fun'
        self.topic_controller = controller.TopicController()
        test_topic_manager = manager.TopicManager()
        test_topic_manager.add_topic(self.test_topic_name)
        self.test_topic = test_topic_manager.get_topic_by_name(
            self.test_topic_name
        )
        self.topic_controller.topic_manager = test_topic_manager

    def test_subscribe_user_to_topic(self):
        self.assertTrue(
            self.topic_controller.subscribe_user_to_topic(
                self.test_user,
                self.test_topic_name,
            )
        )
        self.assertTrue(self.test_topic.is_subscribed(self.test_user))

    def test_unsubscribe_user_from_topic(self):
        self.test_topic.subscribe(self.test_user)
        self.assertTrue(
            self.topic_controller.unsubscribe_user_from_topic(
                self.test_user,
                self.test_topic_name,
            )
        )
        self.assertFalse(self.test_topic.is_subscribed(self.test_user))

    def test_unsubscribe_user_removes_message(self):
        self.test_topic.subscribe(self.test_user)
        self.test_topic.add_message(self.test_message)
        self.topic_controller.unsubscribe_user_from_topic(
            self.test_user,
            self.test_topic_name,
        )
        self.assertEqual(self.test_topic.messages, [])

    def test_unsubscribe_non_subscribed_user(self):
        self.assertFalse(
            self.topic_controller.unsubscribe_user_from_topic(
                self.test_user,
                self.test_topic_name
            )
        )

    def test_publish_message_to_topic(self):
        self.topic_controller.publish_message_to_topic(
            self.test_topic_name,
            self.test_message,
        )
        topic_message_bodies = [msg.body for msg in self.test_topic.messages]
        self.assertIn(self.test_message, topic_message_bodies)

    def test_next_message_in_topic_for_user(self):
        self.test_topic.subscribe(self.test_user)
        self.test_topic.add_message(self.test_message)
        self.assertEqual(
            self.topic_controller.next_message_in_topic_for_user(
                self.test_user,
                self.test_topic_name,
            ),
            self.test_message
        )

    def test_all_subscribers_receive_message_removed(self):
        self.test_topic.subscribe(self.test_user)
        self.test_topic.add_message(self.test_message)
        self.topic_controller.next_message_in_topic_for_user(
            self.test_user,
            self.test_topic_name,
        )
        self.assertEqual(self.test_topic.messages, [])
