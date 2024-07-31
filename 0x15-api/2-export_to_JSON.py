#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee data. Status code: {response.status_code}")
        sys.exit(1)

    username = response.json().get('username')

    todo_url = f"{base_url}/{employee_id}/todos"
    response = requests.get(todo_url)
    if response.status_code != 200:
        print(f"Failed to retrieve todo data. Status code: {response.status_code}")
        sys.exit(1)

    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open(f'{employee_id}.json', 'w') as file:
        json.dump(dictionary, file, indent=4)
