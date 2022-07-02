import unittest
import responses

from axios_client import AxiosClient

STORY_STREAM_URL = 'https://test-url-0'


class TestAxiosClient(unittest.TestCase):

    def setUp(self):
        self.client = AxiosClient(STORY_STREAM_URL)
        responses.add(responses.GET, 'https://test-url-0',
                      json={
                          'count': 15,
                          'next': 'https://test-url-1',
                          'previous': None,
                          'results': [
                              'article-1',
                              'article-2',
                              'article-3',
                              'article-4',
                              'article-5',
                              'article-6',
                              'article-7',
                              'article-8',
                              'article-9',
                              'article-10',
                          ]
                      }
                      , status=200)

        responses.add(responses.GET, 'https://test-url-1',
                      json={
                          'count': 15,
                          'next': None,
                          'previous': 'https://test-url-0',
                          'results': [
                              'article-11',
                              'article-12',
                              'article-13',
                              'article-14',
                              'article-15',
                          ]
                      }
                      , status=200)

    @responses.activate
    def test_get_results_returns_an_article(self):
        results = self.client.get_articles(1)
        self.assertEqual(results[0], 'article-1')

    @responses.activate
    def test_get_results_returns_2_articles(self):
        results = self.client.get_articles(2)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], 'article-1')
        self.assertEqual(results[1], 'article-2')

    @responses.activate
    def test_get_results_returns_12_articles(self):
        results = self.client.get_articles(12)
        self.assertEqual(12, len(results))
        self.assertEqual(results[10], 'article-11')
        self.assertEqual(results[11], 'article-12')

