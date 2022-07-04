from axios_client import AxiosClient
import json
import argparse

if __name__ == '__main__':

    # parse arguments passed from standard input
    parser = argparse.ArgumentParser(description="A news word counter")
    parser.add_argument("pages", nargs="?", metavar="pages", type=int, help="Number of pages to analyze")
    args = parser.parse_args()

    pages = 1 if args.pages is None else args.pages

    # print word count and reading time for each article in the first N pages
    print(json.dumps(AxiosClient().get_content_summary(pages), indent=4, sort_keys=True))
