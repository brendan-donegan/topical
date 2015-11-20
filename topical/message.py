class Message:

    def __init__(self, body):
        self.body = body
        self.watchers = []

    def add_watcher(self, user):
        pass

    def remove_watcher(self, user):
        pass

    def is_watching(self, user):
        pass
