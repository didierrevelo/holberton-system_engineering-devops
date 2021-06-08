#!/usr/bin/python3
"""taks 3
    """

import json
import requests


if __name__ == "__main__":
    jsonFile = 'todo_all_employees.json'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_all = 'https://jsonplaceholder.typicode.com/todos'
    request_user = requests.get(url_users).json()
    all_req = requests.get(url_all).json()
    json_format = {}
    for all_users in request_user:
        user_list = []
        for all_tasks in all_req:
            if all_users['id'] == all_tasks['userId']:
                user_infor_dict = {
                    "username": all_users['username'],
                    "task": all_tasks['title'],
                    "completed": all_tasks['completed'],
                }
                user_list.append(user_infor_dict)
        json_format[all_users['id']] = user_list
    with open(jsonFile, "w") as file:
        json.dump(json_format, file)
