class Message:

    def __init__(self, body, watchers):
        self.body = body
        self.watchers = watchers

    def remove_watcher(self, user):
        self.watchers.remove(user)

    def intended_for(self, user):
        return user in self.watchers
