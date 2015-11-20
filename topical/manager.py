from topical.topic import Topic

class TopicManager:

    def __init__(self):
        self.topics = {}

    def add_topic(self, topic_name):
        """
        Add a topic with the given name

        :param topic_name: The name of the topic
        """
        topic = Topic(topic_name)
        self.topics[topic_name] = topic

    def get_topic_by_name(self, topic_name):
        """
        Get the topic with the given name

        :param topic_name: The name of the topic
        :return: The Topic object or None if it does not exist
        """
        return self.topics.get(topic_name)
