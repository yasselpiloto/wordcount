import unittest

from axios_client import AxiosClient

STORY_STREAM_URL = 'https://api.axios.com/api/render/stream/content/'


class IntegrationTestAxiosClient(unittest.TestCase):

    def setUp(self):
        self.client = AxiosClient(STORY_STREAM_URL)

    def test_get_stream_returns_something(self):
        self.assertNotEqual(self.client.get_stream(), None)

    def test_get_stream_returns_200(self):
        self.assertEqual(self.client.get_stream().status_code, 200)

    def test_get_results_returns_10_stories(self):
        self.assertEqual(self.client.get_results(10), 10)

    def test_get_results_returns_20_stories(self):
        self.assertEqual(self.client.get_results(20), 20)