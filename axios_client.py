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

    # returns an array of objects with the wordcount and reading time for each story
    def get_story_summary(self, story_id):
        response = requests.get(f'{self.STORY_STREAM_URL}/content/{story_id}/').json()
        wordcount = 0
        difficult_words = []
        sentences = 0

        easy_words = set(line.strip() for line in open('easywords.txt'))

        for block in response['blocks']['blocks']:
            words = block['text'].lower().split()
            sentences += block['text'].count(".")
            wordcount += len(words)
            for word in words:
                if word not in easy_words and not word.isnumeric():
                    difficult_words.append(word)

        words_per_minute = wordcount // self.WORDS_PER_MINUTE

        readability_score = self.calculate_readability(difficult_words, sentences, wordcount)

        return {
            'permalink': response['permalink'],
            'headline': response['headline'],
            'word_count': wordcount,
            'reading_time': "<1" if words_per_minute == 0 else words_per_minute,
            'readability': readability_score
        }

    def calculate_readability(self, difficult_words, sentences, wordcount):
        return round((0.1579 * 100 * len(difficult_words) / wordcount) + (0.0496 * wordcount / sentences), 1) if wordcount > 0 else 0

    # returns a dictionary with story Ids as keys and the summary of reading time and word count as values
    def get_content_summary(self, pages=1):
        story_ids = self.get_story_ids(pages)
        result = {}

        for story_id in story_ids:
            result[story_id] = self.get_story_summary(story_id)

        return result
