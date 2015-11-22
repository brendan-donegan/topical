import unittest

from topical.manager import TopicManager


class TopicManagerTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_topic_manager_with_topics(self):
        topics = ['lolcatz', 'coffee', 'beer']
        topic_manager = TopicManager(topics)
        topic_titles = [topic for topic in topic_manager.topics]
        # Use assertCountEqual as the topics won't necessarily be in order
        self.assertCountEqual(topics, topic_titles)
