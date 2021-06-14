#!/usr/bin/python3
"""task 0
    """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    head = {"User-Agent": "linux: didierrevelo:v1.0.0 by /u/didierrevelo"}
    reddit_req = requests.get(url, headers=head).json().get("data")
    if reddit_req is None:
        return 0
    return reddit_req.get("subscribers")
