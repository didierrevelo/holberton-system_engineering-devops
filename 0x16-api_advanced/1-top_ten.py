#!/usr/bin/python3
"""task 1
    """
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    head = {"User-Agent": "linux: didierrevelo:v1.0.0 by /u/didierrevelo"}
    reddit_req = requests.get(url, headers=head).json()
    if 'error' in reddit_req:
        print("None")
        return 0
    dict = reddit_req.get('data')
    child_dict = dict.get('children')
    for titles in child_dict:
        print(titles.get('data').get('title'))
