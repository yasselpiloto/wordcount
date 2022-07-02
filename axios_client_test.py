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
                      }, status=200)

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
                      }, status=200)

        # content generated from https://www.lipsum.com/feed/html
        responses.add(responses.GET, 'https://test-url-0/content/article-1/', json={
            'headline': 'test headline article 1',
            'permalink': 'https://test-permalink-article-1',
            'wordcount': 317,
            'blocks': {
                'blocks': [
                    {
                        # 101 words
                        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed venenatis ipsum tortor, nec finibus orci semper ac. '
                                'Pellentesque faucibus mauris lectus, vitae pretium erat dictum vitae. Morbi eu congue lorem. In leo risus, '
                                'molestie eget malesuada sed, venenatis a nulla. Fusce ultrices non dui malesuada mollis. Vestibulum a ante et '
                                'turpis consequat finibus maximus sit amet est. Mauris vestibulum massa nisl, in vulputate libero placerat nec. '
                                'Phasellus vel urna urna. Integer commodo suscipit neque, sed sodales diam commodo in. Praesent vestibulum felis id '
                                'orci consequat hendrerit. Aenean ac faucibus nulla. Sed facilisis fringilla pulvinar. Ut et justo non mauris '
                                'interdum luctus. '
                    },
                    {
                        # 92 words
                        'text': 'Proin at justo dapibus, luctus elit quis, molestie augue. Vivamus felis ipsum, accumsan id fringilla in, '
                                'feugiat at urna. Sed felis metus, imperdiet eu volutpat varius, tristique quis nisi. Vivamus at sapien in tortor '
                                'egestas mollis sollicitudin non augue. Ut tempus et nisi quis consectetur. Nulla tincidunt, ipsum eget fringilla '
                                'ornare, turpis quam suscipit diam, condimentum maximus ligula ante nec enim. Duis sodales massa nec lacus auctor, '
                                'sit amet posuere justo lobortis. Ut massa erat, mollis id semper et, scelerisque sed nulla. Vivamus in sem et ex '
                                'laoreet tristique et id ligula. '
                    },
                    {
                        # 124 words
                        'text': 'Donec lobortis ipsum vitae neque pretium sodales. Proin aliquet placerat nulla, vel ornare sapien dignissim vel. '
                                'Maecenas sodales dolor orci, non vestibulum sapien cursus in. Ut vitae augue eu sem tempor laoreet. Aenean '
                                'egestas, dolor in lobortis viverra, urna enim bibendum quam, in vulputate urna elit sed quam. Nam porttitor '
                                'rhoncus nulla vitae volutpat. Proin vitae libero sed risus condimentum volutpat. Vestibulum ante ipsum primis in '
                                'faucibus orci luctus et ultrices posuere cubilia curae; Nunc a bibendum velit, id vulputate libero. Sed ac blandit '
                                'lacus, id fermentum tellus. Suspendisse eu suscipit mauris. In lobortis orci sodales, lobortis massa at, '
                                'elementum orci. Vestibulum sodales dictum tortor. Pellentesque ut magna finibus, vestibulum ante eget, '
                                'dictum nunc. In euismod nisi nec tellus rutrum, nec mollis lectus pretium. '
                    }
                ]
            }
        }, status=200)

        responses.add(responses.GET, 'https://test-url-0/content/article-2/', json={
            'headline': 'test headline article 2',
            'permalink': 'https://test-permalink-article-2',
            'wordcount': 125,
            'blocks': {
                'blocks': [
                    {
                        # 60 words
                        'text': 'Quisque vel purus ut erat accumsan placerat id non leo. Pellentesque vitae rutrum eros, venenatis commodo turpis. '
                                'Pellentesque elementum, libero finibus lacinia rutrum, arcu nisi imperdiet dui, ut tristique dolor turpis ut '
                                'lacus. Aenean dapibus eu orci nec sollicitudin. Maecenas sollicitudin commodo nunc vitae pulvinar. Nullam '
                                'sollicitudin mi id ligula elementum, sit amet ornare erat suscipit. Vivamus convallis scelerisque orci. '
                    },
                    {
                        # 65 words
                        'text': 'Fusce lectus nisi, pellentesque quis sodales ac, semper vitae purus. Cras hendrerit pharetra massa vel tempor. Sed '
                                'efficitur feugiat vestibulum. Maecenas ornare urna in sem tristique, nec hendrerit magna aliquet. Etiam '
                                'consectetur tellus sed ex tincidunt, ac volutpat magna consequat. Nullam lobortis elementum urna, sit amet tempor '
                                'massa. In hac habitasse platea dictumst. Curabitur rhoncus dui a pretium porttitor. Nam mollis magna id placerat '
                                'aliquet. '
                    }
                ]
            }
        }, status=200)

        # define a dummy json content for the rest of the stories
        empty_blocks = {
            'permalink': 'permalink',
            'headline': 'headline',
            'blocks': {'blocks': []}
        }
        responses.add(responses.GET, 'https://test-url-0/content/article-3/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-4/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-5/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-6/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-7/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-8/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-9/', json=empty_blocks, status=200)
        responses.add(responses.GET, 'https://test-url-0/content/article-10/', json=empty_blocks, status=200)

    @responses.activate
    def test_get_pages_returns_an_article(self):
        results = self.client.get_story_ids(1)
        self.assertEqual('article-1', results[0])

    @responses.activate
    def test_get_pages_returns_first_page_by_default(self):
        results = self.client.get_story_ids()
        self.assertEqual(len(results), 10)
        self.assertEqual('article-1', results[0])
        self.assertEqual('article-10', results[9])

    @responses.activate
    def test_get_pages_returns_first_page(self):
        results = self.client.get_story_ids(1)
        self.assertEqual(len(results), 10)
        self.assertEqual('article-1', results[0])
        self.assertEqual('article-10', results[9])

    @responses.activate
    def test_get_pages_returns_2_pages(self):
        results = self.client.get_story_ids(2)
        self.assertEqual(15, len(results))
        self.assertEqual('article-11', results[10])
        self.assertEqual('article-15', results[14])

    @responses.activate
    def test_get_pages_returns_max_available_pages(self):
        results = self.client.get_story_ids(5)
        self.assertEqual(15, len(results))
        self.assertEqual('article-11', results[10])
        self.assertEqual('article-15', results[14])

    @responses.activate
    def test_get_stories_length_returns_word_count(self):
        story_details = self.client.get_content_summary()

        # article 1
        self.assertEqual('https://test-permalink-article-1', story_details['article-1']['permalink'])
        self.assertEqual('https://test-permalink-article-1', story_details['article-1']['permalink'])
        self.assertEqual(317, story_details['article-1']['word_count'])
        self.assertEqual(1, story_details['article-1']['reading_time'])

        # article 2
        self.assertEqual('https://test-permalink-article-2', story_details['article-2']['permalink'])
        self.assertEqual('https://test-permalink-article-2', story_details['article-2']['permalink'])
        self.assertEqual(125, story_details['article-2']['word_count'])
        self.assertEqual('<1', story_details['article-2']['reading_time'])
