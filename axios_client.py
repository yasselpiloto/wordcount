import requests


class AxiosClient:
    # using 300 words per minute coefficient according to: https://irisreading.com/what-is-the-average-reading-speed/
    WORDS_PER_MINUTE = 300
    STORY_STREAM_URL = "https://api.axios.com/api/render"

    # gets the ids for the stories in the first n pages from the stream
    def get_story_ids(self, pages=1):
        results = []
        next_page = f'{self.STORY_STREAM_URL}/stream/content/'

        # iterates the first N pages of the story stream
        while len(results) < pages * 10 and next_page is not None:
            response = requests.get(next_page).json()
            results += response['results']
            next_page = response['next']

        return results

    # returns a dictionary with the wordcount and reading time for each story
    def get_story_summary(self, story_id):
        response = requests.get(f'{self.STORY_STREAM_URL}/content/{story_id}/').json()
        wordcount = 0

        for block in response['blocks']['blocks']:
            wordcount += len(block['text'].split())

        words_per_minute = wordcount // self.WORDS_PER_MINUTE

        return {
            'permalink': response['permalink'],
            'headline': response['headline'],
            'word_count': wordcount,
            'reading_time': "<1" if words_per_minute == 0 else words_per_minute
        }

    def get_content_summary(self, pages=1):
        story_ids = self.get_story_ids(pages)
        result = {}

        for story_id in story_ids:
            result[story_id] = self.get_story_summary(story_id)

        return result
