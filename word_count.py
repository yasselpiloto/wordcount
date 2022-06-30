import requests


class WordCounter:

    def __init__(self, story_stream_url):
        self.story_stream_url = story_stream_url

    def get_stream(self):
        response = requests.get(self.story_stream_url)
        print(response)
        return response
