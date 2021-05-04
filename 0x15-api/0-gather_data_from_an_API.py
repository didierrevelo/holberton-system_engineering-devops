#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
from requests import get
from sys import argv


if __name__ == "__main__":
    url_id = 'https://jsonplaceholder.typicode.com/users/{}'
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'

    response_id = get(url_id.format(argv[1]))
    response_todo = get(url_todo.format(argv[1]))

    json_id = response_id.json()
    json_todo = response_todo.json()

    completes = []
    name_user = json_id.get('name')

    tasks = len(json_todo)
    for search in json_todo:
        if search['completed']:
            completes.append(search)
    total = len(completes)

    print("Employee {} is done with tasks({}/{}):"
          .format(name_user, total, tasks))

    for name_tasks in completes:
        print('\t ' + name_tasks.get('title'))
