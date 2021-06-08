#!/usr/bin/python3
"""taks 2
"""

import json
import requests
import sys


if __name__ == "__main__":
    id_user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(id_user)
    request_user = requests.get(url).json()
    userid_argv = '?userId={}'.format(id_user)
    all_url = 'https://jsonplaceholder.typicode.com/todos{}'\
        .format(userid_argv)
    all_req = requests.get(all_url).json()
    all_total = len(all_req)

    info_list = []
    for all_tasks in all_req:
        tasks_dict = {
                "task": all_tasks['title'],
                "completed": all_tasks['completed'],
                "username": request_user['username'],
        }
        info_list.append(tasks_dict)
    json_format = {id_user: info_list}

    jsonFile = "{}.json".format(id_user)
    with open(jsonFile, "w") as file:
        json.dump(json_format, file)
