from topical.manager import TopicManager


class TopicController:

    def __init__(self, topics=None):
        self.topic_manager = TopicManager(topics)

    def subscribe_user_to_topic(self, user, topic_name):
        """
        Subscribe a user to a topic

        :param user: The user to subscribe
        :param topic_name: The topic to subscribe the user to
        :return: True if the operation was succesful, otherwise False
        """
        topic = self.topic_manager.get_topic_by_name(topic_name)
        topic.subscribe(user)
        return topic.is_subscribed(user)

    def unsubscribe_user_from_topic(self, user, topic_name):
        """
        Unsubscribe a user from a topic

        :param user: The user to unsubscribe
        :param topic_name: The topic to unsubscribe the user from
        :return: True if the operation was succesful, otherwise False
        """
        topic = self.topic_manager.get_topic_by_name(topic_name)
        if not topic.is_subscribed(user):
            return False
        topic.unsubscribe(user)
        return True

    def next_message_in_topic_for_user(self, user, topic_name):
        """
        Get the next message for the user in the specified topic

        :param user: The user to get the next message for
        :param topic_name: The topic to get the next message from
        :return: The next message or None if no messages available
        """
        topic = self.topic_manager.get_topic_by_name(topic_name)
        return topic.next_message(user)

    def publish_message_to_topic(self, topic_name, message):
        """
        Publish a message with the specified text to a specified topic

        :param topic_name: The topic to publish the message to
        :param message: The message to publish
        """
        topic = self.topic_manager.get_topic_by_name(topic_name)
        topic.add_message(message)
