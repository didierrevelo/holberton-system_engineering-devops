#!/usr/bin/python3
""" task 2 """
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    head = {"User-Agent": "linux: didierrevelo:v1.0.0 by /u/didierrevelo"}
    req_reddit = requests.get(url, headers=head).json()
    if 'error' in req_reddit:
        return None
    for titles in req_reddit['data']['children']:
        hot_list.append(titles['data']['title'])
    other = req_reddit['data']['after']
    if other is not None:
        recurse(subreddit, hot_list, other)
    return hot_list
