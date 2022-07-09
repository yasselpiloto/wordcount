import unittest
import responses

from axios_client import AxiosClient


class TestAxiosClient(unittest.TestCase):

    def setUp(self):
        self.client = AxiosClient()
        self.client.STORY_STREAM_URL = 'https://test-url-0'
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

        responses.add(responses.GET, 'https://test-url-0/content/article-3/', json={
            'headline': 'test headline article 3',
            'permalink': 'https://test-permalink-article-3',
            'wordcount': 413,
            "blocks": {
                "blocks": [{

                    "text": "Voyager Digital filed for Chapter 11 bankruptcy protection on Tuesday, enclosing documents containing many revelations, not least of which being the way the Toronto-based crypto lender describes its own business."
                },
                    {

                        "text": "Why it matters: That detail highlights the uniqueness of the current proceeding, one that will be watched keenly by regulators and investors as the firm embarks on a journey to untangle its books in the public eye, as a crypto shop."
                    },
                    {

                        "text": "Call it a \"Frankenstein bankruptcy,\" Robert Honeywell, restructuring partner at K&L Gates, tells Axios."
                    },
                    {

                        "text": "Voyager, unable tick of a description of its business from the listed choices—health care business, single-asset "
                                "real estate, railroad operator, stockbroker, commodity broker, clearing bank—nay, checked off \"none of the "
                                "above.\" "
                    },
                    {

                        "text": "Peculiar, because the type of bankruptcy proceeding for which it filed doesn't match the business described. "
                    },
                    {

                        "text": "\"And everyone else is in other classes. In a broker/dealer bankruptcy, customers get priority for their “securities accounts” and everyone else gets what’s left.\""
                    },
                    {

                        "text": "Context: Voyager appears to be trying to stay in-line with regulator expectations. "
                    },
                    {

                        "text": "Recall Coinbase in May had to soothe concerned customers about a potential bankruptcy after the SEC asked the company to update risk disclosures in filings to treat customers as \"unsecured creditors.\" "
                    },
                    {

                        "text": "That's how Voyager is treating customer accounts too. "
                    },
                    {

                        "text": "What they're saying: CEO Stephen Ehrlich tweeted following the bankruptcy filing and a statement posted to Voyager's website that customers with crypto in their accounts will be recouped in some way via the reorganization. "
                    },
                    {

                        "text": "Yes, but: The current restructuring plan is subject to change. Voyager's filing reads:"
                    },
                    {

                        "text": "In June, Voyager enlisted Moelis to gauge buyer appetite for their business or a cash injection and \"several parties indicated interest in participating in a potential in-court transaction.\""
                    },
                    {

                        "text": "Indeed, the bankruptcy filings indicate Voyager is still negotiating."
                    },
                    {

                        "text": "\"The real question is even if they filed as a Chapter 11, will customers who have yield bearing accounts with Voyager say 'I’m not just a normal unsecured creditor, I’m a securities holder,' even though, no regulator has said they are that,\" Honeywell said. "
                    },
                    {

                        "text": "Voyager Digital declined to comment. "
                    },
                    {

                        "text": "What's next: Assuming the proposed restructuring plan stays intact, Voyager would have to provide a fresh estimate of what their creditors are owed and put it to a vote. "
                    },
                    {

                        "text": "\"If no one challenges and everyone votes in favor, it might just sail through,\" Honeywell said."
                    },
                    {
                        "text": "What we're watching: \"Bankruptcies are highly contested battles and there is a whole industry of people who buy claims in order to fight in bankruptcy court,\" Honeywell said."
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

    @responses.activate
    def test_get_stories_readability_returns_score(self):
        story_details = self.client.get_content_summary()

        # article 1
        self.assertEqual(317, story_details['article-1']['word_count'])
        self.assertEqual(15.3, story_details['article-1']['readability'])

        # article 2
        self.assertEqual(125, story_details['article-2']['word_count'])
        self.assertEqual(15.5, story_details['article-2']['readability'])

        # article 3
        self.assertEqual(413, story_details['article-3']['word_count'])
        self.assertEqual(8.9, story_details['article-3']['readability'])
