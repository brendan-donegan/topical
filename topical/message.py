class Message:

    def __init__(self, body, subscribers):
        self.body = body
        # Make sure to copy!
        self.watchers = list(subscribers)

    def remove_watcher(self, user):
        """
        Remove a user from the list of subscribers who
        are still waiting for the message

        :param user: The user to remove from the watchers list
        """
        self.watchers.remove(user)

    def intended_for(self, user):
        """
        Check if the message is intended for a specified user.

        :param user: The user to check for
        :return: True if the message is intended for the user otherwise False
        """
        return user in self.watchers
