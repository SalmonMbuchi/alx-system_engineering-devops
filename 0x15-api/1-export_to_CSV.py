#!/usr/bin/python3
"""pull data from api and export to csv format"""
import csv
import requests
import sys

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    link_2 = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(link).json()
    tasks = requests.get(link_2, params={'userId': sys.argv[1]}).json()

    username = user.get('username')
    userId = sys.argv[1]
    with open('{}.csv'.format(userId), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [my_writer.writerow([userId, username, t.get(
            'completed'), t.get('title')]) for t in tasks]
