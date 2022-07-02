import requests
import json

# using 300 words per minute coefficient according to: https://irisreading.com/what-is-the-average-reading-speed/
WORDS_PER_MINUTE = 300


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

            wordcount = 0
            for block in response['blocks']['blocks']:
                wordcount += len(block['text'].split())

            words_per_minute = wordcount // WORDS_PER_MINUTE
            result[story_id] = {
                'permalink': response['permalink'],
                'headline': response['headline'],
                'word_count': wordcount,
                'reading_time':  "<1" if words_per_minute == 0 else words_per_minute
            }

        return result