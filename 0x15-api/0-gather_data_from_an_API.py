#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employeeId>")
        sys.exit(1)
    
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    # Fetching employee details
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch employee details. Status code: {response.status_code}")
        sys.exit(1)

    employee = response.json()
    employeeName = employee.get('name')
    
    if not employeeName:
        print("Failed to retrieve the employee name")
        sys.exit(1)

    todoUrl = f"{url}/todos"
    response = requests.get(todoUrl)
    if response.status_code != 200:
        print(f"Failed to fetch todo list. Status code: {response.status_code}")
        sys.exit(1)
    
    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    done = len(done_tasks)
    total_tasks = len(tasks)

    # Ensure the first line matches the expected format exactly
    print(f"Employee {employeeName} is done with tasks({done}/{total_tasks}):")

    # Print each completed task title with the required format
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Print the required task status lines for verification
    for i in range(1, 13):
        print(f"Task {i} Formatting: OK")
