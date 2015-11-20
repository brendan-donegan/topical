from collections import deque


class Topic:

    def __init__(self, title):
        self.title = title
        self.subscribers = []
        self.messages = deque()

    def subscribe(self, user):
        """
        Subscribe a user to the topic

        :param user: the user that wants to subscribe to the topic
        """
        pass

    def unsubscribe(self, user):
        """
        Unsubscribe a user from the topic and
        :param user: the user that wants to unsubscribe
        """
        pass

    def next_message(self, user):
        """
        Get the next message for the specified user

        :param user: the user that wants to get the message
        :return: The next message for that user
        """
        pass

    def is_user_subscribed(self, user):
        """
        Check if a user is subscribed to this topic

        :param user: The user to check the subscription status for
        :return: True if the user is subscribed, otherwise False
        """
        pass
