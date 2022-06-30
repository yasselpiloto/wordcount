import unittest

from word_count import WordCounter

STORY_STREAM_URL = "https://api.axios.com/api/render/stream/content/"


class IntegrationTestWordCount(unittest.TestCase):

    def test_get_stream_returns_something(self):
        word_counter = WordCounter(STORY_STREAM_URL)
        self.assertNotEqual(word_counter.get_stream(), None)

    def test_get_stream_returns_200(self):
        word_counter = WordCounter(STORY_STREAM_URL)
        self.assertEqual(word_counter.get_stream().status_code, 200)
