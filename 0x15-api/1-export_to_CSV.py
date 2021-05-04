#!/usr/bin/python3
"""Exports data in the CSV format.
"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    url_id = 'https://jsonplaceholder.typicode.com/users/{}'
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'

    response_id = get(url_id.format(argv[1]))
    response_todo = get(url_todo.format(argv[1]))

    json_id = response_id.json()
    json_todo = response_todo.json()

    name_user = json_id.get('username')
    csv_name =  argv[1] + '.csv'
    with open(csv_name, 'w') as file_csv:
            csv_w = writer(file_csv, quoting=QUOTE_ALL)
            for search in json_todo:
                csv_w.writerow([argv[1],
                                name_user,
                                search['completed'], search['title']])