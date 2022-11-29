#!/usr/bin/python3
""" Print titles of hot posts for a given subreddit """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/salmon)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    results = response.json().get('data')
    for i in results.get('children'):
        print(results.get('data').get('title'))
