#!/usr/bin/python3
"""[summary]

    Returns:
        [type]: [description]
    """
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    User_Agent = {'User-agent': 'rouner'}
    subreddit_req = requests.get(url, headers=User_Agent).json().get('data')
    if subreddit_req is None:
        return 0
    subreddit_req.get('subscribers')
