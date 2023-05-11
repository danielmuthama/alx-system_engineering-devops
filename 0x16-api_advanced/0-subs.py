#!/usr/bin#!/usr/bin/python3
"""
a function that queries the Reddit API and
returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    r = requests.get(base_url, headers=headers, allow_redirects=False).json()

    if r.get('data') is None:
        return 0

    subscribers = r.get('data').get('subscribers')
    return subscribers