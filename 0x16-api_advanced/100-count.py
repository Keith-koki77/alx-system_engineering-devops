#!/usr/bin/python3
"""
Python script for Task 4
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    if after is None:
        after = ""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;\
               x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                 allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                counts[word_lower] = counts.get(word_lower, 0) + 1

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_results(counts)


def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
