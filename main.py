from word_count import WordCounter

STORY_STREAM_URL = "https://api.axios.com/api/render/stream/content/"

if __name__ == '__main__':
    WordCounter(STORY_STREAM_URL).get_stream()
