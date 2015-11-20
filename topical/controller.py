from topical.manager import TopicManager

class TopicController:

    def __init__(self):
        self.topic_manager = TopicManager()

    def subscribe_user_to_topic(self, user, topic):
        """
        Subscribe a user to a topic

        :param user: The user to subscribe
        :param topic: The topic to subscribe the user to
        :return: True if the operation was succesful, otherwise False
        """
        pass

    def unsubscribe_user_from_topic(self, user, topic):
        """
        Unsubscribe a user from a topic
        
        :param user: The user to unsubscribe
        :param topic: The topic to unsubscribe the user from
        :return: True if the operation was succesful, otherwise False
        """
        pass

    def next_message_in_topic_for_user(self, user, topic):
        """
        Get the next message for the user in the specified topic

        :param user: The user to get the next message for
        :param topic: The topic to get the next message from
        :return: The next message or None if no messages available
        """
        pass

    def publish_message_to_topic(self, topic, message):
        """
        Publish a message with the specified text to a specified topic

        :param topic: The topic to publish the message to
        :param message: The message to publish
        :return: True if the operation was succesful, otherwise False
        """
        pass
