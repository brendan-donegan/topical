from topical.message import Message

class Topic:

    def __init__(self, title):
        self.title = title
        self.subscribers = []
        self.messages = []

    def subscribe(self, user):
        """
        Subscribe a user to the topic

        :param user: The user that wants to subscribe to the topic
        """
        if not self.is_subscribed(user):
            self.subscribers.append(user)

    def unsubscribe(self, user):
        """
        Unsubscribe a user from the topic
        :param user: The user that wants to unsubscribe
        """
        self.subscribers.remove(user)


    def add_message(self, body):
        """
        Publish a message to the topic

        :param body: The message body
        """
        message = Message(body, self.subscribers)
        self.messages.append(message)

    def remove_message(self, message):
        self.messages.remove(message)

    def next_message(self, user):
        """
        Get the next message for the specified user

        :param user: The user that wants to get the message
        :return: The next message for that user or None if that user is not
        """
        for message in self.messages:
            if message.intended_for(user):
                message.remove_watcher(user)
                return message.body
        return None

    def is_subscribed(self, user):
        """
        Check if a user is subscribed to this topic

        :param user: The user to check the subscription status for
        :return: True if the user is subscribed, otherwise False
        """
        return user in self.subscribers
