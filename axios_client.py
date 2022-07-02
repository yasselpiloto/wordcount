import requests


class AxiosClient:

    def __init__(self, news_api_url):
        self.news_api_url = news_api_url

    # gets the Ids for the first n pages from the story stream
    def get_pages(self, pages = 1):
        results = []
        next_page = f'{self.news_api_url}/stream/content/'

        # iterates the first N pages of the story stream
        while len(results) < pages * 10 and next_page is not None:
            response = requests.get(next_page).json()
            results += response['results']
            next_page = response['next']

        return results

    # returns a dictionary with the wordcount and reading time for each story
    def get_summary(self, story_ids):
        result = {}

        for story_id in story_ids:
            response = requests.get(f'{self.news_api_url}/content/{story_id}/').json()
            result[story_id] = {'wordcount': response['wordcount']}

        return result


# parsed = requests.get('https://api.axios.com/api/render/content/aa030df2-0a82-4066-bfba-7aa2ef316b75/').json()
# print(print(json.dumps(parsed, indent=4, sort_keys=True)))
# print(parsed['wordcount'])