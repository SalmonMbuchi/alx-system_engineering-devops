#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    link_2 = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(link).json()
    tasks = requests.get(link_2, params={'userId': sys.argv[1]}).json()

    username = user.get('username')
    userId = sys.argv[1]
    with open('{}.json'.format(userId), 'w') as jsonfile:
        json.dump({userId: [{'task': t.get('title'), 'completed': t.get(
            'completed'), 'username': username} for t in tasks]}, jsonfile)
