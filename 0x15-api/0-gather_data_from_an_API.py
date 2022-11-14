#!/usr/bin/python3
"""pull data from api using requests module"""
import requests
import sys

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    link_2 = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(link).json()
    tasks = requests.get(link_2, params={'userId': sys.argv[1]}).json()

    completed = [t.get('title') for t in tasks if t.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format
          (user.get('name'), len(completed), len(tasks)))
    [print('\t {}'.format(c)) for c in completed]
