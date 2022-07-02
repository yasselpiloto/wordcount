import unittest
import json

from axios_client import AxiosClient

STORY_STREAM_URL = 'https://api.axios.com/api/render'


class IntegrationTestAxiosClient(unittest.TestCase):

    def setUp(self):
        self.client = AxiosClient(STORY_STREAM_URL)

    def test_get_stream_returns_one_page_by_default(self):
        print(json.dumps(self.client.get_content_summary(), indent=4, sort_keys=True))

    def test_get_stream_returns_5_pages(self):
        print(json.dumps(self.client.get_content_summary(5), indent=4, sort_keys=True))
