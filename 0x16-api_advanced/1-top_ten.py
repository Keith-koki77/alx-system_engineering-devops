#!/usr/bin/python3
"""
Python Script for Task 1
"""

import requests
import sys


def top_ten(subreddit):
    """
    Get 10 hottest posts of a subreddit
    """
    headers = {'User-agent': 'test23'}
    url = 'https://www.reddit.com/r/'
    posts = requests.get(url + '{}/hot.json?limit=10'.format(
        sys.argv[1]), allow_redirects=False, headers=headers)

    if posts.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])

    else:
        print(None)
