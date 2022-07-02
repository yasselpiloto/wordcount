import requests


class AxiosClient:

    def __init__(self, story_stream_url):
        self.story_stream_url = story_stream_url

    # gets the Ids for the first n articles from the story stream
    def get_articles(self, count):
        next_page = self.story_stream_url
        results = []

        # iterates pages of the story stream until enough article Ids are fetched
        while len(results) < count and next_page is not None:
            response = requests.get(next_page).json()
            results += response['results'][0:10]
            next_page = response['next']

        # removes article Ids that are in excess
        results = results[:-(len(results) - count)]

        return results

