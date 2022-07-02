import unittest
import responses

from axios_client import AxiosClient

STORY_STREAM_URL = 'https://test-url-0'


class TestAxiosClient(unittest.TestCase):

    def setUp(self):
        self.client = AxiosClient(STORY_STREAM_URL)
        responses.add(responses.GET, 'https://test-url-0/stream/content/',
                      json={
                          'count': 15,
                          'next': 'https://test-url-1/stream/content/',
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

        responses.add(responses.GET, 'https://test-url-1/stream/content/',
                      json={
                          'count': 15,
                          'next': None,
                          'previous': 'https://test-url-0/stream/content/',
                          'results': [
                              'article-11',
                              'article-12',
                              'article-13',
                              'article-14',
                              'article-15',
                          ]
                      }
                      , status=200)

        responses.add(responses.GET, 'https://test-url-0/content/article-1/',json={'wordcount': 300}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-1/',json={'wordcount': 400}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-2/',json={'wordcount': 500}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-3/',json={'wordcount': 600}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-4/',json={'wordcount': 700}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-5/',json={'wordcount': 800}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-6/',json={'wordcount': 900}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-7/',json={'wordcount': 1000}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-8/',json={'wordcount': 1100}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-9/',json={'wordcount': 1200}, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-10/',json={'wordcount': 1300}, status=200)

    @responses.activate
    def test_get_pages_returns_an_article(self):
        results = self.client.get_pages(1)
        self.assertEqual('article-1', results[0])

    @responses.activate
    def test_get_pages_returns_first_page_by_default(self):
        results = self.client.get_pages()
        self.assertEqual(len(results), 10)
        self.assertEqual('article-1', results[0])
        self.assertEqual('article-10', results[9])

    @responses.activate
    def test_get_pages_returns_first_page(self):
        results = self.client.get_pages(1)
        self.assertEqual(len(results), 10)
        self.assertEqual('article-1', results[0])
        self.assertEqual('article-10', results[9])

    @responses.activate
    def test_get_pages_returns_2_pages(self):
        results = self.client.get_pages(2)
        self.assertEqual(15, len(results))
        self.assertEqual('article-11', results[10])
        self.assertEqual('article-15', results[14])

    @responses.activate
    def test_get_pages_returns_max_available_pages(self):
        results = self.client.get_pages(5)
        self.assertEqual(15, len(results))
        self.assertEqual('article-11', results[10])
        self.assertEqual('article-15', results[14])

    @responses.activate
    def test_get_stories_length_returns_word_count(self):
        stories = self.client.get_pages(1)
        story_details = self.client.get_summary(stories)
        self.assertEqual(300, story_details['article-1']['wordcount'])
        # self.assertEqual(1, story_details['avg_reading_time'])
