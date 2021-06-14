#!/usr/bin/python3
""" Function that queries Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ this function returns a list containing
    the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {'User-Agent': 'apposvendorandversion'}
    req_subreddit = requests.get(url, headers=headers).json()
    if 'error' in req_subreddit:
        return None
    for titles in req_subreddit['data']['children']:
        hot_list.append(titles['data']['title'])
    next = req_subreddit['data']['after']
    if next is not None:
        recurse(subreddit, hot_list, next)
    return hot_list
