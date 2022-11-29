#!/usr/bin/python3
""" Return the number of subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ returns total subscribers not active users"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
